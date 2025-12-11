# 🔧 Colab 导入问题修复

## 问题描述
在 Google Colab 中运行时出现以下错误：
```
ModuleNotFoundError: No module named 'utils.api_key'
```

## 原因分析
在 Colab 环境中，克隆代码后切换目录（`%cd myLLM`），但 Python 的 `sys.path` 没有自动包含当前目录，导致无法导入项目模块。

## 已实施的修复

### 1. 修改 `colab_setup.ipynb` ✅

**在第 3 步（设置 API Key）单元格中添加了路径配置:**

```python
# 设置火山引擎 ARK API Key 并配置 Python 路径
import os
import sys

# 设置 API Key
os.environ['ARK_API_KEY'] = '29d9f392-5151-47e4-b1f6-c007d69f4ae9'

# 添加当前目录到 Python 路径（重要！确保可以导入项目模块）
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

print("✓ API Key 已设置")
print(f"✓ Python 路径已配置: {current_dir}")
```

**新增了第 5.5 步（配置 Python 路径验证）:**

```python
# 添加当前目录到 Python 路径，确保能导入 utils 模块
import sys
import os

# 获取当前工作目录
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"✓ 已添加 {current_dir} 到 Python 路径")

# 验证可以导入 utils 模块
try:
    from utils.api_key import api_key
    print("✓ 成功导入 utils.api_key 模块")
    print(f"  API Key 前缀: {api_key[:10]}...")
except Exception as e:
    print(f"✗ 导入失败: {e}")
    print(f"  当前目录: {os.getcwd()}")
    print(f"  sys.path: {sys.path[:3]}")
```

### 2. 修改 `utils/llm.py` ✅

**添加了导入失败的 fallback 逻辑:**

对于豆包模型和其他模型，添加了更健壮的导入机制：

```python
# 对于 doubao 模型
elif "doubao" in model.lower():
    import os
    try:
        from utils.api_key import api_key
    except ImportError:
        # Fallback for Colab or environments where utils is not in path
        import sys
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.api_key import api_key
    # ... rest of config

# 对于其他模型（OpenAI等）
else:
    import os
    try:
        from utils.api_key import api_key
    except ImportError:
        # Fallback for Colab or environments where utils is not in path
        import sys
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.api_key import api_key
    # ... rest of config
```

## 使用方法

### 在 Google Colab 中

1. **按顺序运行所有单元格**，特别注意：
   - 第 1 步：克隆代码并切换目录
   - **第 3 步：设置 API Key 和配置路径（必须运行！）**
   - 第 5.5 步：验证路径配置
   - 第 6 步：运行示例代码

2. **重要提示**：
   - 每次重新启动 Colab 会话都需要重新运行第 3 步
   - 如果遇到导入错误，重新运行第 3 步和第 5.5 步

### 手动修复（如果仍有问题）

如果在任何单元格中遇到导入错误，添加这段代码到单元格开头：

```python
import sys
import os
if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())
```

## 测试验证

运行以下代码验证修复：

```python
# 测试 1: 检查路径
import sys
import os
print(f"当前目录: {os.getcwd()}")
print(f"Python 路径: {sys.path[:3]}")

# 测试 2: 尝试导入
try:
    from utils.api_key import api_key
    from utils.llm import get_llm_kwargs
    print("✓ 导入成功！")
except Exception as e:
    print(f"✗ 导入失败: {e}")
    
# 测试 3: 运行简单示例
try:
    model_name, llm_kwargs = get_llm_kwargs("doubao-seed-1-6-251015", "v0.1")
    print(f"✓ 配置成功！模型: {model_name}")
except Exception as e:
    print(f"✗ 配置失败: {e}")
```

## 提交状态

- ✅ 本地提交完成（commit: 72055a3）
- ⏳ 等待推送到 GitHub（网络连接问题）

**待办事项：**
```bash
# 当网络恢复后，运行以下命令推送更改
cd "D:\HuaweiMoveData\Users\12434\Desktop\计算机视觉\LLM-groundedDiffusion-main"
git push
```

## 总结

修复后的代码现在包含：
1. ✅ 自动路径配置（在第 3 步）
2. ✅ 路径验证（第 5.5 步）
3. ✅ 导入失败的 fallback 机制（utils/llm.py）
4. ✅ 清晰的错误提示

这应该能解决在 Google Colab 中的 `ModuleNotFoundError` 问题。
