#!/usr/bin/env python3
"""
文档标题提取工具
从 req_md 文件夹中的 Markdown 文档第一页提取标题
"""

import os
import json
import re
import argparse
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from typing import Dict

# 加载环境变量
load_dotenv()

# 提示词模板
EXTRACT_TITLE_PROMPT = """请从以下文档的第一页内容中提取文档标题。

要求：
1. 识别文档的主要标题（通常是文档名称或项目名称）
2. 返回简洁、准确的标题，不包含多余格式、日期、版本号等信息
3. 如果无法识别标题，返回 "未识别"

文档第一页内容：
{first_page_content}

请只返回标题文本，不要包含其他说明或格式。"""


def read_first_page(file_path: Path, lines: int = 100) -> str:
    """读取文件的前N行作为第一页内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_lines = []
            for i, line in enumerate(f):
                if i >= lines:
                    break
                first_lines.append(line)
            return ''.join(first_lines)
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return ""


def check_title_in_content(title: str, content: str) -> bool:
    """
    检查标题是否在内容中存在
    
    Args:
        title: 要检查的标题
        content: 内容文本
    
    Returns:
        如果标题在内容中存在（忽略大小写、换行、标点和多余空格）返回True
    """
    if not title or title == "未识别":
        return False
    
    # 标准化函数：去除标点、多余空格、换行符，统一为单个空格
    def normalize_text(text: str) -> str:
        # 将所有换行符、制表符等空白字符替换为空格
        text = re.sub(r'\s+', ' ', text)
        # 去除标点符号（保留字母数字和空格）
        text = re.sub(r'[^\w\s]', '', text)
        # 再次去除多余空格并转为小写
        text = re.sub(r'\s+', ' ', text).strip().lower()
        return text
    
    # 标准化标题和内容
    title_normalized = normalize_text(title)
    content_normalized = normalize_text(content)
    
    # 方法1: 检查完整标准化标题
    if title_normalized and title_normalized in content_normalized:
        return True
    
    # 方法2: 检查标题的所有单词是否都在内容中（允许顺序不同）
    title_words = [w for w in title_normalized.split() if len(w) > 2]  # 忽略太短的词
    if len(title_words) >= 2:
        # 检查至少80%的重要单词是否在内容中
        words_found = sum(1 for word in title_words if word in content_normalized)
        if words_found >= max(2, int(len(title_words) * 0.8)):
            return True
    
    # 方法3: 检查标题的核心部分（前几个重要单词）
    if len(title_words) > 3:
        # 取前几个重要单词（至少3个）
        core_words = title_words[:min(5, len(title_words))]
        core_title = ' '.join(core_words)
        if core_title in content_normalized:
            return True
        # 也检查这些核心单词是否都在内容中
        core_found = sum(1 for word in core_words if word in content_normalized)
        if core_found >= len(core_words) * 0.8:
            return True
    
    # 方法4: 对于短标题（<=3个单词），要求所有单词都在内容中
    if len(title_words) <= 3 and len(title_words) > 0:
        if all(word in content_normalized for word in title_words):
            return True
    
    return False


def extract_title(client: OpenAI, first_page_content: str, model: str, temperature: float) -> str:
    """使用LLM提取文档标题"""
    prompt = EXTRACT_TITLE_PROMPT.format(first_page_content=first_page_content)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
        )
        title = response.choices[0].message.content.strip()
        # 清理可能的引号或其他格式
        title = title.strip('"\'')
        return title
    except Exception as e:
        print(f"❌ LLM调用失败: {e}")
        return "未识别"


def process_files(
    req_md_dir: Path,
    output_path: Path,
    model: str,
    temperature: float,
    force: bool = False
):
    """处理所有Markdown文件，提取标题"""
    # 初始化OpenAI客户端
    client_config = {"api_key": os.getenv("OPENAI_API_KEY")}
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url:
        client_config["base_url"] = base_url
    client = OpenAI(**client_config)
    
    # 获取所有.md文件
    md_files = sorted(req_md_dir.glob("*.md"))
    total_files = len(md_files)
    
    if total_files == 0:
        print(f"⚠️  在 {req_md_dir} 中未找到任何 .md 文件")
        return
    
    print(f"📁 找到 {total_files} 个Markdown文件")
    
    # 如果输出文件已存在，尝试加载已有结果
    existing_titles = {}
    if output_path.exists() and not force:
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_titles = json.load(f)
            print(f"📖 加载已有结果: {len(existing_titles)} 个标题")
        except Exception as e:
            print(f"⚠️  加载已有结果失败: {e}")
    
    # 处理每个文件
    titles = existing_titles.copy()
    processed = 0
    skipped = 0
    validated = 0
    not_validated = 0
    
    for idx, file_path in enumerate(md_files, 1):
        filename = file_path.name
        
        # 检查是否已处理过
        if filename in titles and not force:
            # 即使跳过，也验证已有标题
            first_page = read_first_page(file_path, lines=100)
            if first_page:
                existing_title = titles[filename]
                is_valid = check_title_in_content(existing_title, first_page)
                if is_valid:
                    print(f"[{idx}/{total_files}] ⏭️  跳过（已存在）: {filename} - {existing_title} (已验证)")
                    validated += 1
                else:
                    print(f"[{idx}/{total_files}] ⏭️  跳过（已存在）: {filename} - {existing_title} (⚠️ 未验证)")
                    not_validated += 1
            else:
                print(f"[{idx}/{total_files}] ⏭️  跳过（已存在）: {filename}")
            skipped += 1
            continue
        
        print(f"[{idx}/{total_files}] 📄 处理: {filename}")
        
        # 读取第一页内容
        first_page = read_first_page(file_path, lines=100)
        if not first_page:
            print(f"  ⚠️  文件为空，跳过")
            titles[filename] = "未识别"
            skipped += 1
            continue
        
        # 提取标题
        print(f"  🔄 提取标题中...")
        title = extract_title(client, first_page, model, temperature)
        
        # 验证标题是否在第一页内容中存在
        is_valid = check_title_in_content(title, first_page)
        if is_valid:
            print(f"  ✅ 标题: {title} (已验证：存在于第一页)")
            validated += 1
        else:
            print(f"  ⚠️  标题: {title} (警告：未在第一页中找到)")
            not_validated += 1
        
        titles[filename] = title
        processed += 1
        
        # 添加延迟以避免API限流
        if idx < total_files:
            import time
            time.sleep(0.5)
    
    # 保存结果
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(titles, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 已保存 {len(titles)} 个标题到: {output_path}")
        print(f"   处理: {processed} 个文件，跳过: {skipped} 个文件")
        if processed > 0:
            print(f"   验证通过: {validated} 个，未通过: {not_validated} 个")
    except Exception as e:
        print(f"❌ 保存失败 {output_path}: {e}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="从Markdown文档第一页提取标题",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--req-md-dir",
        type=Path,
        default=Path(__file__).parent / "resources" / "req_md",
        help="req_md文件夹路径（默认: resources/req_md）"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "resources" / "titles.json",
        help="输出JSON文件路径（默认: resources/titles.json）"
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        help="使用的模型（默认: 从环境变量OPENAI_MODEL读取，或gpt-4o-mini）"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=float(os.getenv("OPENAI_TEMPERATURE", "0.3")),
        help="温度参数（默认: 从环境变量OPENAI_TEMPERATURE读取，或0.3）"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新处理所有文件（即使已存在结果）"
    )
    
    args = parser.parse_args()
    
    # 检查API密钥
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ 错误: 未设置 OPENAI_API_KEY 环境变量")
        print("   请在 .env 文件中设置，或使用环境变量")
        return 1
    
    # 检查输入目录
    if not args.req_md_dir.exists():
        print(f"❌ 错误: 输入目录不存在: {args.req_md_dir}")
        return 1
    
    # 处理文件
    process_files(
        req_md_dir=args.req_md_dir,
        output_path=args.output,
        model=args.model,
        temperature=args.temperature,
        force=args.force
    )
    
    return 0


if __name__ == "__main__":
    exit(main())

