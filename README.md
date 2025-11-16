# SRS 文档处理工具

本项目提供了用于处理软件需求规格说明书（SRS）的工具集。

## 功能

1. **文档格式转换** (`convert_to_markdown.py`)
   - 将 `req` 文件夹中的文档转换为 Markdown 格式
   - 支持格式：PDF、DOC、DOCX、HTML、HTM、RTF

2. **需求文档摘要生成** (`generate_summaries.py`)
   - 使用 LLM 对 `req_md` 中的需求文档文件生成摘要
   - 支持控制不同的需求摘要详细程度（代表现实中不同的需求访谈效果）

## 安装

```bash
# 安装依赖
pip install -r requirements.txt
# 或者使用 uv
uv sync
```

## 配置

### 使用 .env 文件配置（推荐）

1. 复制示例配置文件：
```bash
cp env.example .env
```

2. 编辑 `.env` 文件，设置你的配置：
```env
# 必需：API密钥
OPENAI_API_KEY=your-api-key-here

# 可选：模型配置
OPENAI_MODEL=gpt-4o-mini
OPENAI_TEMPERATURE=0.3
# OPENAI_BASE_URL=https://api.openai.com/v1
```

### 环境变量配置

也可以直接设置环境变量（不使用 `.env` 文件）：
```bash
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_MODEL="gpt-4o-mini"
export OPENAI_TEMPERATURE="0.3"
export OPENAI_MAX_TOKENS="4000"
```

### 配置参数说明

- `OPENAI_API_KEY`（必需）：OpenAI API 密钥
- `OPENAI_MODEL`（可选，默认：`gpt-4o-mini`）：使用的模型名称
  - 可选值：`gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo` 等
- `OPENAI_TEMPERATURE`（可选，默认：`0.3`）：模型温度参数（0.0-2.0）
  - 较低的值使输出更确定性和一致性，较高的值使输出更随机
- `OPENAI_BASE_URL`（可选）：API 基础 URL，用于兼容其他 OpenAI 兼容的 API

**注意**：摘要长度通过提示词自动控制，会根据原文档长度和摘要级别自动计算目标字符数，无需手动设置 token 限制。

## 使用方法

### 1. 文档格式转换

```bash
python3 convert_to_markdown.py
```

将 `req` 文件夹中的文档转换为 Markdown 格式，保存到 `req_md` 文件夹。

### 2. 生成摘要

#### 生成所有级别的摘要（默认）
```bash
python3 generate_summaries.py
# 或
python3 generate_summaries.py --level all
```

#### 生成特定级别的摘要
```bash
# 超短摘要（5% - 10%）
python3 generate_summaries.py --level ultra_short

# 简短摘要（10% - 20%）
python3 generate_summaries.py --level short

# 平衡摘要（20% - 30%）
python3 generate_summaries.py --level balanced

# 详尽摘要（30% - 50%）
python3 generate_summaries.py --level detailed

# 生成多个级别
python3 generate_summaries.py --level ultra_short short
```

#### 其他选项

```bash
# 测试模式（只处理前5个文件）
python3 generate_summaries.py --level short --limit 5

# 强制重新生成已存在的摘要
python3 generate_summaries.py --level short --force

# 使用自定义模型
python3 generate_summaries.py --model gpt-4

# 自定义温度参数
python3 generate_summaries.py --level balanced --temperature 0.5
```

## 摘要级别说明

| 级别标识 | 文件夹 | 摘要长度 | 说明 |
|---------|--------|----------|------|
| ultra_short | `summary_ultra_short` | 5% - 10% | 超短摘要，仅包含核心要点和关键需求 |
| short | `summary_short` | 10% - 20% | 简短摘要，包含主要功能和需求概述 |
| balanced | `summary_balanced` | 20% - 30% | 平衡摘要，包含详细的功能描述和主要需求 |
| detailed | `summary_detailed` | 30% - 50% | 详尽摘要，包含详细的功能、用例和需求说明 |

## 项目结构

```
srs-docs/
├── req/                    # 原始需求文档（PDF、DOC等）
├── req_md/                 # 转换后的Markdown文档
├── summary_ultra_short/    # 超短摘要（5%-10%）
├── summary_short/          # 简短摘要（10%-20%）
├── summary_balanced/       # 平衡摘要（20%-30%）
├── summary_detailed/       # 详尽摘要（30%-50%）
├── convert_to_markdown.py  # 文档转换脚本
├── generate_summaries.py   # 摘要生成脚本
├── env.example             # 环境变量配置示例
└── .env                    # 环境变量配置（需自行创建）
```

## 注意事项

1. 确保已安装所有依赖：`pip install openai python-dotenv`
2. 必须设置 `OPENAI_API_KEY` 环境变量或 `.env` 文件
3. 脚本会自动跳过已存在的摘要文件，使用 `--force` 可强制重新生成
4. 处理大量文件时，注意 API 调用频率限制
5. 长文档会自动截断处理，保留开头和结尾部分以确保结构完整

## 故障排除

### 问题：无法导入 dotenv
**解决方案**：安装 python-dotenv
```bash
pip install python-dotenv
```

### 问题：API 密钥错误
**解决方案**：检查 `.env` 文件或环境变量中的 `OPENAI_API_KEY` 是否正确设置

### 问题：模型不存在
**解决方案**：检查 `OPENAI_MODEL` 配置，确保使用有效的模型名称

