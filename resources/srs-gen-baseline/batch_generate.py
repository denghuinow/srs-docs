"""
批量生成文档脚本
读取指定文件夹中的所有 .md 文件，调用生成 API，并将结果保存为 JSON
"""

import os
import json
import time
import requests
import numpy as np
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

# 需要先启动服务
# (AI-Based-SRS-Generator) root@4090-xdh:~/project/srs/AI-Based-SRS-Generator/src# uv run uvicorn backend.main:app --reload

# 配置
API_BASE_URL = "http://127.0.0.1:8000"
INPUT_FOLDER = "resources/summary_ultra_short_sample10"  # 输入文件夹路径
COMPARE_FOLDER = None # 比较文件夹路径（可选）
OUTPUT_JSON = "resources/srs-gen-baseline/generated_documents.json"  # 输出 JSON 文件路径
DOC_TYPE = "SRS"  # 文档类型
STYLE = "professional"  # 风格

# 评估 API 配置（用于替代向量相似度计算）
EVAL_API_BASE_URL = "http://localhost:8001"

# Embedding API 配置（已废弃，保留用于向后兼容）
EMBEDDING_API_BASE_URL = "http://oneapi.wchat.cc/v1"
EMBEDDING_API_KEY = "sk-ImpZxN2xEHkGKrfzqInaCtOBbwbzdXul1eECm1nEOyyk26R8"
EMBEDDING_MODEL = "Qwen/Qwen3-Embedding-8B"


def read_md_files(folder_path: str) -> List[Dict[str, str]]:
    """
    读取文件夹中的所有 .md 文件
    
    Args:
        folder_path: 文件夹路径
        
    Returns:
        文件列表，每个元素包含文件名和内容
    """
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"文件夹不存在: {folder_path}")
    
    md_files = []
    for file_path in folder.glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:  # 只处理非空文件
                    md_files.append({
                        "filename": file_path.name,
                        "content": content
                    })
        except Exception as e:
            print(f"警告: 读取文件 {file_path.name} 失败: {e}")
    
    return md_files


def get_embedding(text: str, api_base_url: str, api_key: str, model: str) -> Optional[List[float]]:
    """
    获取文本的向量嵌入
    
    Args:
        text: 要向量化的文本
        api_base_url: Embedding API 基础 URL
        api_key: API 密钥
        model: 模型名称
        
    Returns:
        向量嵌入列表，如果失败返回 None
    """
    if not text or not text.strip():
        return None
    
    url = f"{api_base_url}/embeddings"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    print(f"对长度为{len(text)}取embedding")
    payload = {
        "input": text,
        "model": model
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        # OpenAI 格式的响应
        if "data" in result and len(result["data"]) > 0:
            return result["data"][0]["embedding"]
        else:
            print(f"  警告: Embedding API 返回格式异常")
            return None
    except requests.exceptions.RequestException as e:
        print(f"  警告: 获取向量嵌入失败: {e}")
        return None


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    计算两个向量的余弦相似度
    
    Args:
        vec1: 向量1
        vec2: 向量2
        
    Returns:
        余弦相似度 (0-1之间，1表示完全相同)
    """
    if not vec1 or not vec2 or len(vec1) != len(vec2):
        return 0.0
    
    vec1_array = np.array(vec1)
    vec2_array = np.array(vec2)
    
    # 计算余弦相似度
    dot_product = np.dot(vec1_array, vec2_array)
    norm1 = np.linalg.norm(vec1_array)
    norm2 = np.linalg.norm(vec2_array)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    similarity = dot_product / (norm1 * norm2)
    return float(similarity)


def find_comparison_file(original_filename: str, compare_folder: Path) -> Optional[str]:
    """
    根据原始文件名查找比较目录中的对应文件（文件名相同）
    
    Args:
        original_filename: 原始文件名
        compare_folder: 比较文件夹路径
        
    Returns:
        比较文件的完整路径，如果未找到返回 None
    """
    if not compare_folder or not compare_folder.exists():
        return None
    
    # 直接匹配相同文件名
    comparison_file = compare_folder / original_filename
    if comparison_file.exists():
        return str(comparison_file)
    
    return None


def read_comparison_file(file_path: str) -> Optional[str]:
    """
    读取比较文件内容
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件内容，如果读取失败返回 None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"  警告: 读取比较文件失败: {e}")
        return None


def evaluate_documents(evaluated_srs: str, standard_srs: str,
                       eval_api_url: str = EVAL_API_BASE_URL) -> Optional[Dict]:
    """
    调用评估API比较两份SRS文档，返回评估得分
    
    Args:
        evaluated_srs: 待评审的SRS文档（生成的文档）
        standard_srs: 标准参考SRS文档（比较文档）
        eval_api_url: 评估API基础URL
        
    Returns:
        评估结果字典，包含：
        - Functional_Completeness: {score, analysis}
        - Interaction_Flow_Similarity: {score, analysis}
        - Total_Score: 总分
        - Summary: 总体评价
        如果评估失败返回 None
    """
    if not evaluated_srs or not standard_srs:
        return None
    
    print(f"  正在调用评估API进行文档评估...")
    
    url = f"{eval_api_url}/evaluate_srs"
    payload = {
        "standard_srs": standard_srs,
        "evaluated_srs": evaluated_srs
    }
    
    try:
        response = requests.post(url, json=payload, timeout=120)  # 2分钟超时
        response.raise_for_status()
        result = response.json()
        
        # 检查是否有错误
        if "error" in result:
            error_msg = result.get('error', '未知错误')
            raw_output = result.get('raw_output', '')
            raw_length = result.get('raw_output_length', 0)
            print(f"  ⚠️  评估API返回错误: {error_msg}")
            if raw_output:
                preview = raw_output[:200] if len(raw_output) > 200 else raw_output
                print(f"     原始输出预览: {preview}...")
                if raw_length > 200:
                    print(f"     (总长度: {raw_length} 字符)")
            return None
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"  ⚠️  调用评估API失败: {e}")
        return None


def calculate_similarity(generated_doc: str, comparison_doc: str,
                        api_base_url: str, api_key: str, model: str) -> Optional[float]:
    """
    计算生成文档和比较文档的余弦相似度（已废弃，保留用于向后兼容）
    
    Args:
        generated_doc: 生成的文档内容
        comparison_doc: 比较文档内容
        api_base_url: Embedding API 基础 URL
        api_key: API 密钥
        model: 模型名称
        
    Returns:
        余弦相似度 (0-1)，如果计算失败返回 None
    """
    if not generated_doc or not comparison_doc:
        return None
    
    print(f"  正在计算向量相似度...")
    
    # 获取两个文档的向量嵌入
    vec1 = get_embedding(generated_doc, api_base_url, api_key, model)
    if vec1 is None:
        return None
    
    vec2 = get_embedding(comparison_doc, api_base_url, api_key, model)
    if vec2 is None:
        return None
    
    # 计算余弦相似度
    similarity = cosine_similarity(vec1, vec2)
    return round(similarity, 4)  # 保留4位小数


def generate_document_stream(api_url: str, doc_type: str, summary: str, 
                             requirements: str, style: str = "professional") -> Dict:
    """
    调用流式生成文档 API，并组合成完整文档
    
    Args:
        api_url: API 基础 URL
        doc_type: 文档类型
        summary: 项目概述
        requirements: 需求描述
        style: 风格
        
    Returns:
        API 响应结果（包含完整文档内容）
    """
    url = f"{api_url}/api/generate/stream"
    payload = {
        "doc_type": doc_type,
        "summary": summary,
        "requirements": requirements,
        "style": style,
        "feedback_score": 3
    }
    
    try:
        # 发送流式请求
        response = requests.post(url, json=payload, stream=True, timeout=300)  # 5分钟超时
        response.raise_for_status()
        
        # 解析流式响应（每行一个 JSON 对象）
        document_content = ""
        doc_id = None
        doc_title = None
        
        for line in response.iter_lines():
            if line:
                try:
                    # 解码字节并解析 JSON
                    line_str = line.decode('utf-8')
                    chunk_data = json.loads(line_str)
                    
                    chunk_type = chunk_data.get("type")
                    
                    if chunk_type == "start":
                        # 记录文档 ID
                        doc_id = chunk_data.get("id")
                        print("  开始接收流式内容...", end="", flush=True)
                    elif chunk_type == "content":
                        # 累积内容
                        content_chunk = chunk_data.get("content", "")
                        document_content += content_chunk
                        print(content_chunk, end="", flush=True)  # 显示进度
                    elif chunk_type == "complete":
                        # 完成，获取标题
                        doc_id = chunk_data.get("id", doc_id)
                        doc_title = chunk_data.get("title", "")
                        print(" ✓")  # 换行
                        break
                    elif chunk_type == "error":
                        # 错误
                        error_msg = chunk_data.get("message", "未知错误")
                        print(f" ✗")  # 换行
                        raise Exception(f"流式生成错误: {error_msg}")
                        
                except json.JSONDecodeError as e:
                    # 如果不是有效的 JSON，可能是纯文本，忽略
                    continue
                except Exception as e:
                    print(f" ✗")  # 换行
                    raise e
        
        # 构建返回结果（兼容原格式）
        return {
            "id": doc_id or "",
            "content": document_content,
            "title": doc_title or f"{doc_type}: {summary[:50]}..."
        }
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"API 调用失败: {e}")


def batch_generate_documents(input_folder: str, output_json: str, 
                            api_url: str = API_BASE_URL,
                            doc_type: str = DOC_TYPE,
                            style: str = STYLE,
                            compare_folder: Optional[str] = None,
                            eval_api_url: str = EVAL_API_BASE_URL,
                            embedding_api_base_url: str = EMBEDDING_API_BASE_URL,
                            embedding_api_key: str = EMBEDDING_API_KEY,
                            embedding_model: str = EMBEDDING_MODEL):
    """
    批量生成文档
    
    Args:
        input_folder: 输入文件夹路径
        output_json: 输出 JSON 文件路径
        api_url: API 基础 URL
        doc_type: 文档类型
        style: 风格
    """
    print(f"开始批量生成文档...")
    print(f"输入文件夹: {input_folder}")
    print(f"输出文件: {output_json}")
    print(f"API 地址: {api_url}")
    if compare_folder:
        print(f"比较文件夹: {compare_folder}")
        print(f"评估 API: {eval_api_url}")
    print("-" * 60)
    
    # 读取所有 md 文件
    md_files = read_md_files(input_folder)
    if not md_files:
        print(f"错误: 在 {input_folder} 中未找到任何 .md 文件")
        return
    
    print(f"找到 {len(md_files)} 个 .md 文件\n")
    
    # 检查 API 是否可用
    try:
        test_response = requests.get(f"{api_url}/docs", timeout=5)
        print(f"✓ API 服务可用\n")
    except Exception as e:
        print(f"⚠️  警告: 无法连接到 API 服务 ({api_url})")
        print(f"   请确保后端服务已启动")
        response = input("是否继续？(y/n): ")
        if response.lower() != 'y':
            return
    
    # 批量处理
    results = []
    total_start_time = time.time()
    
    for i, file_info in enumerate(md_files, 1):
        filename = file_info["filename"]
        content = file_info["content"]
        
        print(f"[{i}/{len(md_files)}] 处理文件: {filename}")
        print(f"  文件大小: {len(content)} 字符")
        
        # 记录开始时间
        start_time = time.time()
        
        try:
            # 调用流式生成 API（使用相同内容作为 summary 和 requirements）
            print(f"  正在生成文档（流式）...")
            result = generate_document_stream(
                api_url=api_url,
                doc_type=doc_type,
                summary=content,
                requirements=content,
                style=style
            )
            
            # 计算耗时（秒）
            time_cost = round(time.time() - start_time, 2)
            
            # 提取生成的文档内容
            generated_document = result.get("content", "")
            
            print(f"  ✓ 生成成功 (耗时: {time_cost} 秒)")
            print(f"  生成文档长度: {len(generated_document)} 字符")
            
            # 调用评估API比较文档（如果提供了比较文件夹）
            evaluation_result = None
            if compare_folder and generated_document:
                compare_folder_path = Path(compare_folder)
                comparison_file_path = find_comparison_file(filename, compare_folder_path)
                
                if comparison_file_path:
                    print(f"  找到比较文件: {Path(comparison_file_path).name}")
                    comparison_content = read_comparison_file(comparison_file_path)
                    if comparison_content:
                        evaluation_result = evaluate_documents(
                            evaluated_srs=generated_document,
                            standard_srs=comparison_content,
                            eval_api_url=eval_api_url
                        )
                        if evaluation_result is not None:
                            total_score = evaluation_result.get("Total_Score", 0)
                            func_score = evaluation_result.get("Functional_Completeness", {}).get("score", 0)
                            flow_score = evaluation_result.get("Interaction_Flow_Similarity", {}).get("score", 0)
                            print(f"  ✓ 评估完成:")
                            print(f"    功能完整性得分: {func_score}/50")
                            print(f"    交互流程接近性得分: {flow_score}/50")
                            print(f"    总分: {total_score}/100")
                        else:
                            print(f"  ⚠️  评估失败")
                    else:
                        print(f"  ⚠️  比较文件内容为空")
                else:
                    print(f"  ⚠️  未找到对应的比较文件")
            
            # 添加到结果列表
            result_item = {
                "time_cost": time_cost,
                "document": generated_document,
                "filename": filename,
                "doc_id": result.get("id", ""),
                "title": result.get("title", "")
            }
            
            # 如果有评估结果，添加到结果中
            if evaluation_result is not None:
                result_item["evaluation"] = evaluation_result
                result_item["total_score"] = evaluation_result.get("Total_Score", 0)
            
            results.append(result_item)
            
        except Exception as e:
            time_cost = round(time.time() - start_time, 2)
            print(f"  ✗ 生成失败: {e}")
            print(f"  耗时: {time_cost} 秒")
            
            # 即使失败也记录
            results.append({
                "time_cost": time_cost,
                "document": "",
                "filename": filename,
                "error": str(e)
            })
        
        print()
    
    # 计算总耗时
    total_time = round(time.time() - total_start_time, 2)
    
    # 保存结果到 JSON 文件（简化格式）
    # 保存 time_cost、document、filename 和评估得分（如果有）
    simplified_results = []
    for r in results:
        item = {
            "time_cost": r["time_cost"],
            "document": r["document"],
            "filename": r.get("filename", "")
        }
        # 如果有评估结果，添加总分到结果中
        if "total_score" in r:
            item["total_score"] = r["total_score"]
        simplified_results.append(item)
    
    try:
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(simplified_results, f, ensure_ascii=False, indent=2)
        print(f"✓ 结果已保存到: {output_json}")
    except Exception as e:
        print(f"✗ 保存结果失败: {e}")
        return
    
    # 保存详细版本（可选）
    detailed_output = output_json.replace('.json', '_detailed.json')
    output_data = {
        "generated_at": datetime.now().isoformat(),
        "total_files": len(md_files),
        "successful": len([r for r in results if r.get("document")]),
        "failed": len([r for r in results if "error" in r]),
        "total_time_cost": total_time,
        "results": results
    }
    
    try:
        with open(detailed_output, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        print(f"✓ 详细结果已保存到: {detailed_output}")
    except Exception as e:
        pass  # 详细版本保存失败不影响主流程
    
    # 打印摘要
    print("\n" + "=" * 60)
    print("批量生成完成！")
    print("=" * 60)
    print(f"总文件数: {len(md_files)}")
    print(f"成功: {output_data['successful']}")
    print(f"失败: {output_data['failed']}")
    print(f"总耗时: {total_time} 秒")
    print(f"平均耗时: {round(total_time / len(md_files), 2)} 秒/文件")
    print(f"结果文件: {output_json}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="批量生成文档脚本")
    parser.add_argument(
        "--input", "-i",
        default=INPUT_FOLDER,
        help=f"输入文件夹路径（默认: {INPUT_FOLDER}）"
    )
    parser.add_argument(
        "--output", "-o",
        default=OUTPUT_JSON,
        help=f"输出 JSON 文件路径（默认: {OUTPUT_JSON}）"
    )
    parser.add_argument(
        "--api-url",
        default=API_BASE_URL,
        help=f"API 基础 URL（默认: {API_BASE_URL}）"
    )
    parser.add_argument(
        "--doc-type",
        default=DOC_TYPE,
        help=f"文档类型（默认: {DOC_TYPE}）"
    )
    parser.add_argument(
        "--style",
        default=STYLE,
        help=f"风格（默认: {STYLE}）"
    )
    parser.add_argument(
        "--compare",
        default=COMPARE_FOLDER,
        help=f"比较文件夹路径（可选）"
    )
    parser.add_argument(
        "--eval-api-url",
        default=EVAL_API_BASE_URL,
        help=f"评估API基础 URL（默认: {EVAL_API_BASE_URL}）"
    )
    parser.add_argument(
        "--embedding-api-url",
        default=EMBEDDING_API_BASE_URL,
        help=f"Embedding API 基础 URL（已废弃，默认: {EMBEDDING_API_BASE_URL}）"
    )
    parser.add_argument(
        "--embedding-api-key",
        default=EMBEDDING_API_KEY,
        help=f"Embedding API 密钥（已废弃）"
    )
    parser.add_argument(
        "--embedding-model",
        default=EMBEDDING_MODEL,
        help=f"Embedding 模型名称（已废弃，默认: {EMBEDDING_MODEL}）"
    )
    
    args = parser.parse_args()
    
    # 创建输出目录（如果不存在）
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 执行批量生成
    batch_generate_documents(
        input_folder=args.input,
        output_json=args.output,
        api_url=args.api_url,
        doc_type=args.doc_type,
        style=args.style,
        compare_folder=args.compare,
        eval_api_url=args.eval_api_url,
        embedding_api_base_url=args.embedding_api_url,
        embedding_api_key=args.embedding_api_key,
        embedding_model=args.embedding_model
    )


if __name__ == "__main__":
    main()

