#!/usr/bin/env python3
"""
脚本用于从 generated_documents.json 中提取 document 字段，
并以 filename 为文件名保存到 srs-gen-baseline 文件夹中。
"""

import json
import os
from pathlib import Path


def extract_documents():
    # 定义路径
    json_file = Path(__file__).parent / "generated_documents.json"
    output_dir = Path(__file__).parent / "srs-gen-baseline"
    
    # 创建输出目录（如果不存在）
    output_dir.mkdir(exist_ok=True)
    
    # 读取JSON文件
    print(f"正在读取 {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取并保存文档
    saved_count = 0
    for item in data:
        filename = item.get('filename')
        document = item.get('document', '')
        
        if not filename:
            print(f"警告: 跳过缺少 filename 的项")
            continue
        
        # 构建输出文件路径
        output_path = output_dir / filename
        
        # 保存文档内容
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(document)
            saved_count += 1
            print(f"已保存: {filename}")
        except Exception as e:
            print(f"错误: 保存 {filename} 时出错: {e}")
    
    print(f"\n完成! 共保存 {saved_count} 个文档到 {output_dir}")


if __name__ == "__main__":
    extract_documents()

