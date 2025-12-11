# Google Colab 使用指南

本项目已配置为在 Google Colab 上使用火山引擎豆包模型 API。

## 快速开始

### 1. 在 Google Colab 中打开笔记本

点击下面的按钮在 Colab 中打开:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Wu-XiaoTian/myLLM/blob/main/colab_setup.ipynb)

或者手动上传 `colab_setup.ipynb` 到 Google Colab。

### 2. 配置 GPU 运行时

在 Colab 中:
1. 点击菜单 **运行时 (Runtime)** > **更改运行时类型 (Change runtime type)**
2. 在 **硬件加速器 (Hardware accelerator)** 中选择 **GPU**
3. 点击 **保存 (Save)**

### 3. 运行笔记本

按顺序运行笔记本中的所有单元格。笔记本会自动:
- 克隆代码仓库
- 安装依赖
- 配置 API Key
- 测试 API 连接
- 运行示例代码

## API 配置

项目已配置使用火山引擎豆包模型:
- **API Key**: `29d9f392-5151-47e4-b1f6-c007d69f4ae9`
- **API Base URL**: `https://ark.cn-beijing.volces.com/api/v3`
- **模型**: `doubao-seed-1-6-251015`

API Key 可以通过环境变量 `ARK_API_KEY` 设置，或使用 `utils/api_key.py` 中的默认值。

## 本地修改说明

以下文件已被修改以支持火山引擎 API:

### 1. `utils/api_key.py`
- 将 `OPENAI_API_KEY` 改为 `ARK_API_KEY`
- 添加了默认的火山引擎 API Key

### 2. `utils/llm.py`
- 在 `model_names` 列表中添加了 `doubao-seed-1-6-251015`
- 在 `get_llm_kwargs()` 函数中添加了豆包模型的配置分支
- 设置正确的 API base URL 和 headers

## 使用示例

### 基本用法

```python
from utils.llm import get_llm_kwargs, get_parsed_layout

# 配置模型
model = "doubao-seed-1-6-251015"
template_version = "v0.1"

# 获取配置
model_name, llm_kwargs = get_llm_kwargs(model, template_version)

# 生成布局
prompt = "A cat sitting on a table next to a red apple"
gen_boxes, bg_prompt, neg_prompt = get_parsed_layout(prompt, llm_kwargs)
```

### 直接使用火山引擎 API

```python
from openai import OpenAI
import os

api_key = os.getenv('ARK_API_KEY')

client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="doubao-seed-1-6-251015",
    messages=[
        {
            "role": "user",
            "content": "你好，请帮我生成一个图像布局。"
        }
    ]
)

print(response.choices[0].message.content)
```

## 注意事项

1. **GPU 要求**: 图像生成需要 GPU 支持，请确保 Colab 运行时配置为 GPU
2. **内存限制**: Colab 免费版有内存限制，生成大型图像可能会遇到问题
3. **会话时间**: Colab 会话会超时，长时间运行的任务需要注意
4. **API 限制**: 火山引擎 API 可能有调用频率限制
5. **网络连接**: 确保 Colab 可以访问火山引擎的 API 端点

## 故障排除

### API 连接失败
- 检查 API Key 是否正确
- 检查网络连接
- 确认火山引擎服务是否可用

### GPU 不可用
- 确认已在 Colab 中选择 GPU 运行时
- 检查 GPU 配额是否已用完

### 依赖安装失败
- 尝试重新运行安装单元格
- 检查 PyPI 是否可访问

## 进一步开发

如需修改代码或添加新功能:
1. Fork 本仓库
2. 在本地或 Colab 中进行修改
3. 测试修改
4. 提交 Pull Request

## 联系方式

如有问题，请在 GitHub 上提交 Issue。
