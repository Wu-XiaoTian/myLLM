# 快速开始指南

## 🎯 Google Colab 快速使用

### 方法 1: 直接在 Colab 中打开

1. 访问: https://colab.research.google.com/
2. 选择 "GitHub" 标签
3. 输入仓库 URL: `https://github.com/Wu-XiaoTian/myLLM`
4. 选择 `colab_setup.ipynb` 文件
5. 点击 "在 Colab 中打开"

### 方法 2: 使用直接链接

点击这个链接直接打开:
```
https://colab.research.google.com/github/Wu-XiaoTian/myLLM/blob/main/colab_setup.ipynb
```

### 方法 3: 添加徽章到 README（推荐）

在你的 GitHub 仓库 README 中添加:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Wu-XiaoTian/myLLM/blob/main/colab_setup.ipynb)
```

## 📝 使用步骤

### 1. 设置 GPU 运行时

在 Colab 中:
- 菜单: **Runtime** → **Change runtime type**
- 选择 **GPU** 作为硬件加速器
- 点击 **Save**

### 2. 运行所有单元格

点击 **Runtime** → **Run all** 或逐个运行单元格

笔记本将自动:
- ✅ 克隆代码仓库
- ✅ 安装依赖包
- ✅ 配置 API Key
- ✅ 测试 API 连接
- ✅ 运行示例代码

## 🔑 API 配置说明

### 当前配置
- **API Provider**: 火山引擎 (Volcengine Ark)
- **Model**: `doubao-seed-1-6-251015`
- **API Key**: 已在 `utils/api_key.py` 中配置
- **Base URL**: `https://ark.cn-beijing.volces.com/api/v3`

### 环境变量配置 (可选)

如果你想使用不同的 API Key，可以在 Colab 中设置:

```python
import os
os.environ['ARK_API_KEY'] = 'your-api-key-here'
```

## 🧪 测试配置

在本地测试配置:

```bash
python test_config.py
```

这将运行三个测试:
1. ✅ API Key 配置检查
2. ✅ LLM 配置检查  
3. ✅ API 连接测试

## 📖 代码示例

### 使用豆包模型生成布局

```python
from utils.llm import get_llm_kwargs, get_parsed_layout

# 配置
model = "doubao-seed-1-6-251015"
template_version = "v0.1"

# 获取配置
model_name, llm_kwargs = get_llm_kwargs(model, template_version)

# 生成
prompt = "A cat sitting on a table next to a red apple"
gen_boxes, bg_prompt, neg_prompt = get_parsed_layout(prompt, llm_kwargs)

print(f"Generated boxes: {gen_boxes}")
print(f"Background prompt: {bg_prompt}")
```

### 直接调用 API

```python
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.getenv('ARK_API_KEY')
)

response = client.chat.completions.create(
    model="doubao-seed-1-6-251015",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## 🔍 文件说明

### 核心配置文件
- **`utils/api_key.py`**: API Key 配置
- **`utils/llm.py`**: LLM 模型配置和调用逻辑

### 新增文件
- **`colab_setup.ipynb`**: Google Colab 笔记本
- **`COLAB_README.md`**: 详细的 Colab 使用文档
- **`test_config.py`**: 配置测试脚本
- **`QUICKSTART.md`**: 本文件

## ⚠️ 注意事项

### GPU 要求
- 图像生成需要 GPU
- Colab 免费版提供 GPU，但有使用时间限制
- 推荐使用 T4 或更好的 GPU

### 内存限制
- Colab 免费版: ~12GB RAM
- 大型模型可能需要更多内存
- 如遇内存不足，尝试减小批次大小

### 会话管理
- Colab 会话会超时（通常 90 分钟无活动）
- 定期保存结果到 Google Drive
- 长时间运行建议使用 Colab Pro

### API 限制
- 火山引擎 API 可能有调用频率限制
- 检查你的 API 配额
- 避免在循环中频繁调用

## 🐛 故障排除

### API 连接失败
```
错误: Connection timeout
解决: 检查网络连接，确认 API 端点可访问
```

### GPU 不可用
```
错误: CUDA not available
解决: 在 Runtime 设置中切换到 GPU
```

### 依赖安装失败
```
错误: pip install failed
解决: 重新运行安装单元格，或手动安装失败的包
```

### 模型加载失败
```
错误: Model not found
解决: 检查模型名称是否正确，确认 API Key 有权限
```

## 📚 更多资源

- **完整文档**: [COLAB_README.md](COLAB_README.md)
- **原项目**: [LLM-grounded Diffusion](https://github.com/TonyLianLong/LLM-groundedDiffusion)
- **火山引擎文档**: [Volcengine Ark API](https://www.volcengine.com/docs/82379)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

请参考原项目的 License。
