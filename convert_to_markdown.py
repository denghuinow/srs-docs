#!/usr/bin/env python3
"""
将 req 文件夹中的文档转换为 Markdown 格式
支持格式：PDF、DOC、DOCX、HTML、HTM、RTF
"""

import os
import sys
from pathlib import Path
import re

def sanitize_filename(filename):
    """清理文件名，移除或替换不合法字符"""
    # 移除或替换不合法字符
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # 移除前导和尾随空格
    filename = filename.strip()
    return filename

def pdf_to_markdown(pdf_path):
    """将 PDF 文件转换为 Markdown"""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        markdown_content = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            if text.strip():
                markdown_content.append(text)
        
        doc.close()
        return "\n\n".join(markdown_content)
    except ImportError:
        try:
            import pdfplumber
            markdown_content = []
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        markdown_content.append(text)
            return "\n\n".join(markdown_content)
        except ImportError:
            try:
                from pypdf import PdfReader
                reader = PdfReader(pdf_path)
                markdown_content = []
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        markdown_content.append(text)
                return "\n\n".join(markdown_content)
            except Exception as e:
                return f"# PDF 转换错误\n\n无法转换 PDF 文件: {str(e)}\n\n请安装以下库之一：\n- PyMuPDF: pip install pymupdf\n- pdfplumber: pip install pdfplumber\n- pypdf: pip install pypdf\n"

def doc_to_markdown(doc_path):
    """将 DOC/DOCX 文件转换为 Markdown"""
    file_ext = doc_path.suffix.lower()
    
    # 处理 .docx 文件
    if file_ext == '.docx':
        try:
            import docx
            doc = docx.Document(doc_path)
            markdown_content = []
            
            for para in doc.paragraphs:
                if para.text.strip():
                    # 根据样式判断标题级别
                    style_name = para.style.name.lower()
                    if 'heading 1' in style_name or '标题 1' in style_name:
                        markdown_content.append(f"# {para.text}\n")
                    elif 'heading 2' in style_name or '标题 2' in style_name:
                        markdown_content.append(f"## {para.text}\n")
                    elif 'heading 3' in style_name or '标题 3' in style_name:
                        markdown_content.append(f"### {para.text}\n")
                    else:
                        markdown_content.append(f"{para.text}\n")
            
            return "\n".join(markdown_content)
        except Exception as e:
            return f"# DOCX 转换错误\n\n无法转换 DOCX 文件: {str(e)}\n"
    
    # 处理旧版 .doc 文件
    elif file_ext == '.doc':
        try:
            # 尝试使用 textract
            import textract
            text = textract.process(doc_path).decode('utf-8')
            return text
        except ImportError:
            try:
                # 尝试使用 antiword 通过系统命令
                import subprocess
                result = subprocess.run(['antiword', doc_path], 
                                      capture_output=True, 
                                      text=True,
                                      timeout=30)
                if result.returncode == 0:
                    return result.stdout
                else:
                    raise Exception("antiword 命令执行失败")
            except (FileNotFoundError, Exception):
                try:
                    # 尝试使用 LibreOffice 转换
                    import subprocess
                    import tempfile
                    import os
                    
                    with tempfile.TemporaryDirectory() as tmpdir:
                        output_path = os.path.join(tmpdir, "output.txt")
                        result = subprocess.run([
                            'libreoffice', '--headless', '--convert-to', 'txt',
                            '--outdir', tmpdir, doc_path
                        ], capture_output=True, timeout=60)
                        
                        if result.returncode == 0 and os.path.exists(output_path):
                            with open(output_path, 'r', encoding='utf-8', errors='ignore') as f:
                                return f.read()
                        else:
                            raise Exception("LibreOffice 转换失败")
                except Exception:
                    # 最后尝试：使用 catdoc（如果可用）
                    try:
                        import subprocess
                        result = subprocess.run(['catdoc', doc_path],
                                              capture_output=True,
                                              text=True,
                                              timeout=30)
                        if result.returncode == 0:
                            return result.stdout
                    except:
                        pass
                    
                    return f"# DOC 转换错误\n\n无法转换旧版 .doc 文件。\n\n请安装以下工具之一：\n- textract: pip install textract\n- antiword: sudo apt-get install antiword\n- LibreOffice: sudo apt-get install libreoffice\n- catdoc: sudo apt-get install catdoc\n"
        except Exception as e:
            return f"# DOC 转换错误\n\n转换过程中出错: {str(e)}\n"

def html_to_markdown(html_path):
    """将 HTML 文件转换为 Markdown"""
    try:
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        
        markdown_content = h.handle(html_content)
        return markdown_content
    except ImportError:
        try:
            from bs4 import BeautifulSoup
            import re
            
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 移除脚本和样式
            for script in soup(["script", "style"]):
                script.decompose()
            
            # 获取文本内容
            text = soup.get_text()
            
            # 清理文本
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
        except ImportError:
            return f"# HTML 转换错误\n\n无法转换 HTML 文件。\n\n请安装以下库之一：\n- html2text: pip install html2text\n- beautifulsoup4: pip install beautifulsoup4\n"

def rtf_to_markdown(rtf_path):
    """将 RTF 文件转换为 Markdown"""
    try:
        from striprtf.striprtf import rtf_to_text
        
        with open(rtf_path, 'r', encoding='utf-8', errors='ignore') as f:
            rtf_content = f.read()
        
        text = rtf_to_text(rtf_content)
        return text
    except ImportError:
        try:
            import pyth.plugins.rtf15.reader as rtf_reader
            
            with open(rtf_path, 'rb') as f:
                rtf_content = f.read()
            
            doc = rtf_reader.read(rtf_content)
            text = doc.plaintext
            return text
        except ImportError:
            # 简单处理：移除 RTF 控制字符
            with open(rtf_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # 移除 RTF 控制序列
            text = re.sub(r'\\[a-z]+\d*\s?', '', content)
            text = re.sub(r'\{[^}]*\}', '', text)
            return text

def convert_file(input_path, output_path):
    """转换单个文件"""
    file_ext = input_path.suffix.lower()
    
    print(f"正在转换: {input_path.name} -> {output_path.name}")
    
    if file_ext == '.pdf':
        content = pdf_to_markdown(input_path)
    elif file_ext in ['.doc', '.docx']:
        content = doc_to_markdown(input_path)
    elif file_ext in ['.html', '.htm']:
        content = html_to_markdown(input_path)
    elif file_ext == '.rtf':
        content = rtf_to_markdown(input_path)
    else:
        print(f"  警告: 不支持的文件格式 {file_ext}")
        return False
    
    # 写入 Markdown 文件
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  错误: 无法写入文件 {output_path}: {str(e)}")
        return False

def main():
    """主函数"""
    req_dir = Path(__file__).parent / "req"
    output_dir = Path(__file__).parent / "req_md"
    
    if not req_dir.exists():
        print(f"错误: req 文件夹不存在: {req_dir}")
        sys.exit(1)
    
    # 创建输出目录
    output_dir.mkdir(exist_ok=True)
    print(f"输出目录: {output_dir}")
    
    # 获取所有文件
    supported_extensions = ['.pdf', '.doc', '.docx', '.html', '.htm', '.rtf']
    files = [f for f in req_dir.iterdir() if f.is_file() and f.suffix.lower() in supported_extensions]
    
    if not files:
        print("未找到可转换的文件")
        return
    
    print(f"找到 {len(files)} 个文件需要转换\n")
    
    success_count = 0
    failed_count = 0
    
    for input_file in files:
        # 生成输出文件名：原文件名 + .md 后缀
        output_filename = sanitize_filename(input_file.name) + ".md"
        output_file = output_dir / output_filename
        
        if convert_file(input_file, output_file):
            success_count += 1
        else:
            failed_count += 1
    
    print(f"\n转换完成!")
    print(f"成功: {success_count} 个文件")
    print(f"失败: {failed_count} 个文件")

if __name__ == "__main__":
    main()

