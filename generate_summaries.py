#!/usr/bin/env python3
"""
需求文档摘要生成工具
支持4种详细程度：超短摘要、简短摘要、平衡摘要、详尽摘要
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from typing import Dict, List, Optional
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# 加载环境变量
load_dotenv()

# 打印锁，用于线程安全的输出
print_lock = threading.Lock()

# 摘要级别配置
SUMMARY_LEVELS = {
    "minimal": {
        "name": "Minimal Summary",
        "folder": "minimal",
        "info_range": "2%-5%",
        "prompt_file": "minimal.md"
    },
    "ultra_short": {
        "name": "Ultra Short Summary",
        "folder": "ultra_short",
        "info_range": "5%-10%",
        "prompt_file": "ultra_short.md"
    },
    "short": {
        "name": "Short Summary",
        "folder": "short",
        "info_range": "10%-20%",
        "prompt_file": "short.md"
    },
    "balanced": {
        "name": "Balanced Summary",
        "folder": "balanced",
        "info_range": "20%-30%",
        "prompt_file": "balanced.md"
    },
    "detailed": {
        "name": "Detailed Summary",
        "folder": "detailed",
        "info_range": "30%-50%",
        "prompt_file": "detailed.md"
    }
}



def _load_prompt_template(prompt_file: str, prompt_version: str = "v1") -> str:
    """
    加载prompt模板

    Args:
        prompt_file: 模板文件名
        prompt_version: 提示词版本，默认为 v1

    Returns:
        模板内容
    """
    # 构建文件路径：prompts/{version}/{prompt_file}
    project_root = Path(__file__).parent
    template_path = project_root / "prompts" / prompt_version / prompt_file
    
    if not template_path.exists():
        # 如果指定版本不存在，尝试使用v1作为默认版本
        if prompt_version != "v1":
            with print_lock:
                print(f"⚠️  提示词文件不存在: {template_path}，尝试使用 v1 版本")
            template_path = project_root / "prompts" / "v1" / prompt_file
    
    if not template_path.exists():
        raise FileNotFoundError(
            f"模板文件不存在: {template_path}，请检查提示词版本和文件路径"
        )
    return template_path.read_text(encoding="utf-8")


def get_markdown_files(source_dir: Path) -> List[Path]:
    """获取所有Markdown文件"""
    return list(source_dir.glob("*.md"))


def read_file_content(file_path: Path) -> str:
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        with print_lock:
            print(f"❌ 读取文件失败 {file_path}: {e}")
        return ""


def generate_summary(
    client: OpenAI,
    content: str,
    level_config: Dict,
    model: str = None,
    temperature: float = None,
    prompt_version: str = "v1"
) -> str:
    """使用LLM生成摘要"""
    # 从文件加载提示词模板
    prompt_file = level_config["prompt_file"]
    prompt_template = _load_prompt_template(prompt_file, prompt_version)
    
    # 检查模板中是否包含 {srs_text} 占位符
    if "{srs_text}" in prompt_template:
        # 如果包含占位符，替换它并将整个内容作为 user message
        user_message = prompt_template.replace("{srs_text}", content)
        messages = [
            {"role": "user", "content": user_message}
        ]
    else:
        # 如果没有占位符，使用原有逻辑：模板作为 system prompt，内容作为 user message
        messages = [
            {"role": "system", "content": prompt_template},
            {"role": "user", "content": content}
        ]
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        with print_lock:
            print(f"❌ LLM调用失败: {e}")
        return ""


def save_summary(output_path: Path, summary: str):
    """保存摘要到文件"""
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(summary)
        with print_lock:
            print(f"✅ 已保存: {output_path}")
    except Exception as e:
        with print_lock:
            print(f"❌ 保存失败 {output_path}: {e}")


def process_file(
    file_path: Path,
    source_dir: Path,
    output_dirs: Dict[str, Path],
    client_config: Dict,
    model: str,
    temperature: float,
    selected_levels: Optional[List[str]] = None,
    force: bool = False,
    file_index: int = 0,
    total_files: int = 0,
    prompt_version: str = "v1"
):
    """处理单个文件，生成指定级别的摘要"""
    # 为每个线程创建独立的OpenAI客户端
    client = OpenAI(**client_config)
    
    with print_lock:
        if total_files > 0:
            print(f"\n[{file_index}/{total_files}] 📄 处理文件: {file_path.name}")
        else:
            print(f"\n📄 处理文件: {file_path.name}")
    
    # 读取文件内容
    content = read_file_content(file_path)
    if not content:
        with print_lock:
            print(f"⚠️  跳过空文件: {file_path.name}")
        return
    
    # 计算相对路径，保持目录结构
    relative_path = file_path.relative_to(source_dir)
    
    # 确定要处理的级别
    levels_to_process = selected_levels if selected_levels else list(SUMMARY_LEVELS.keys())
    
    # 为每个摘要级别生成摘要
    for level_key in levels_to_process:
        if level_key not in SUMMARY_LEVELS:
            continue
        
        level_config = SUMMARY_LEVELS[level_key]
        output_dir = output_dirs[level_key]
        output_path = output_dir / relative_path
        
        # 检查文件是否已存在
        if output_path.exists() and not force:
            with print_lock:
                print(f"  ⏭️  {file_path.name}: {level_config['name']}已存在，跳过")
            continue
        
        with print_lock:
            print(f"  🔄 {file_path.name}: 生成{level_config['name']} ({level_config['info_range']})...")
        
        # 生成摘要
        summary = generate_summary(
            client=client,
            content=content,
            level_config=level_config,
            model=model,
            temperature=temperature,
            prompt_version=prompt_version
        )
        
        if summary:
            # 保存摘要
            save_summary(output_path, summary)
            # 添加延迟以避免API限流（并发时每个线程独立延迟）
            time.sleep(0.5)
        else:
            with print_lock:
                print(f"  ⚠️  {file_path.name}: {level_config['name']}生成失败")


def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(
        description="需求文档摘要生成工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
摘要级别选项：
  minimal      - 极简摘要（2%-5%）
  ultra_short  - 超短摘要（5%-10%）
  short        - 简短摘要（10%-20%）
  balanced     - 平衡摘要（20%-30%）
  detailed     - 详尽摘要（30%-50%）
  all          - 所有级别（默认）
        """
    )
    parser.add_argument(
        "--level",
        nargs="+",
        choices=["minimal", "ultra_short", "short", "balanced", "detailed", "all"],
        default=["all"],
        help="选择要生成的摘要级别（默认：all）"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="限制处理的文件数量（用于测试）"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新生成已存在的摘要"
    )
    parser.add_argument(
        "--model",
        type=str,
        help="覆盖默认模型配置"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        help="覆盖默认温度参数"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="并发处理的工作线程数（默认：1，即顺序处理）"
    )
    parser.add_argument(
        "--prompt-version",
        type=str,
        default="v1",
        help="提示词版本（默认：v1）"
    )
    
    args = parser.parse_args()
    
    # 配置路径
    project_root = Path(__file__).parent
    source_dir = project_root / "resources" / "req_md"
    
    # 检查源目录
    if not source_dir.exists():
        print(f"❌ 源目录不存在: {source_dir}")
        sys.exit(1)
    
    # 确定要处理的级别
    if "all" in args.level:
        selected_levels = None  # None表示处理所有级别
        print("📝 将生成所有级别的摘要")
    else:
        selected_levels = args.level
        print(f"📝 将生成以下级别的摘要: {', '.join([SUMMARY_LEVELS[k]['name'] for k in selected_levels])}")
    
    # 创建输出目录（只创建需要的）
    output_dirs = {}
    levels_to_create = selected_levels if selected_levels else list(SUMMARY_LEVELS.keys())
    for level_key in levels_to_create:
        if level_key in SUMMARY_LEVELS:
            level_config = SUMMARY_LEVELS[level_key]
            output_dir = project_root / "resources" / "summary" / level_config["folder"]
            output_dir.mkdir(parents=True, exist_ok=True)
            output_dirs[level_key] = output_dir
            print(f"📁 输出目录: {output_dir}")
    
    # 初始化OpenAI客户端
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ 未找到 OPENAI_API_KEY，请检查 .env 文件")
        sys.exit(1)
    
    model = args.model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    temperature = args.temperature if args.temperature is not None else float(os.getenv("OPENAI_TEMPERATURE", "0.3"))
    
    base_url = os.getenv("OPENAI_BASE_URL")
    client_config = {
        "api_key": api_key,
    }
    if base_url:
        client_config["base_url"] = base_url
    
    print(f"🤖 使用模型: {model}")
    print(f"🌡️  温度参数: {temperature}")
    print(f"📝 提示词版本: {args.prompt_version}")
    if args.force:
        print("🔄 强制模式：将重新生成已存在的摘要")
    if args.workers > 1:
        print(f"⚡ 并发模式：使用 {args.workers} 个工作线程")
    
    # 获取所有Markdown文件
    md_files = get_markdown_files(source_dir)
    
    # 应用限制
    if args.limit:
        md_files = md_files[:args.limit]
        print(f"⚠️  测试模式：仅处理前 {args.limit} 个文件")
    
    total_files = len(md_files)
    
    if total_files == 0:
        print(f"❌ 在 {source_dir} 中未找到Markdown文件")
        sys.exit(1)
    
    print(f"\n📊 找到 {total_files} 个Markdown文件\n")
    
    # 处理每个文件
    if args.workers > 1:
        # 并发处理模式
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            # 提交所有任务
            future_to_file = {
                executor.submit(
                    process_file,
                    file_path=file_path,
                    source_dir=source_dir,
                    output_dirs=output_dirs,
                    client_config=client_config,
                    model=model,
                    temperature=temperature,
                    selected_levels=selected_levels,
                    force=args.force,
                    file_index=idx,
                    total_files=total_files,
                    prompt_version=args.prompt_version
                ): file_path
                for idx, file_path in enumerate(md_files, 1)
            }
            
            # 等待所有任务完成
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    future.result()  # 获取结果，如果有异常会抛出
                except Exception as e:
                    with print_lock:
                        print(f"❌ 处理文件 {file_path.name} 时发生错误: {e}")
    else:
        # 顺序处理模式（原有逻辑）
        for idx, file_path in enumerate(md_files, 1):
            print(f"\n[{idx}/{total_files}]", end=" ")
            process_file(
                file_path=file_path,
                source_dir=source_dir,
                output_dirs=output_dirs,
                client_config=client_config,
                model=model,
                temperature=temperature,
                selected_levels=selected_levels,
                force=args.force,
                file_index=idx,
                total_files=total_files,
                prompt_version=args.prompt_version
            )
    
    print("\n" + "="*60)
    print("✅ 所有摘要生成完成！")
    print("="*60)
    for level_key in (selected_levels if selected_levels else list(SUMMARY_LEVELS.keys())):
        if level_key in output_dirs:
            level_config = SUMMARY_LEVELS[level_key]
            output_dir = output_dirs[level_key]
            print(f"  {level_config['name']}: {output_dir}")


if __name__ == "__main__":
    main()
