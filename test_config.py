"""
测试火山引擎豆包 API 配置

这个脚本用于验证 API 配置是否正确。
"""

import os
import sys

def test_api_key():
    """测试 API Key 是否正确配置"""
    print("=" * 50)
    print("测试 1: API Key 配置")
    print("=" * 50)
    
    try:
        from utils.api_key import api_key
        
        if api_key and api_key != "YOUR_API_KEY":
            print("✓ API Key 已配置")
            print(f"  API Key 前缀: {api_key[:10]}...")
            return True
        else:
            print("✗ API Key 未配置或无效")
            return False
    except Exception as e:
        print(f"✗ 导入失败: {e}")
        return False

def test_llm_config():
    """测试 LLM 配置"""
    print("\n" + "=" * 50)
    print("测试 2: LLM 配置")
    print("=" * 50)
    
    try:
        from utils.llm import get_llm_kwargs, model_names
        
        # 检查豆包模型是否在列表中
        if "doubao-seed-1-6-251015" in model_names:
            print("✓ 豆包模型已添加到模型列表")
        else:
            print("✗ 豆包模型未在模型列表中")
            return False
        
        # 测试获取配置
        model_name, llm_kwargs = get_llm_kwargs("doubao-seed-1-6-251015", "v0.1")
        
        print(f"✓ 模型配置成功")
        print(f"  模型名称: {model_name}")
        print(f"  API Base: {llm_kwargs.api_base}")
        print(f"  Temperature: {llm_kwargs.temperature}")
        print(f"  Max Tokens: {llm_kwargs.max_tokens}")
        
        # 检查 API base URL
        if "ark.cn-beijing.volces.com" in llm_kwargs.api_base:
            print("✓ API Base URL 配置正确")
            return True
        else:
            print("✗ API Base URL 不正确")
            return False
            
    except Exception as e:
        print(f"✗ 配置失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_connection():
    """测试 API 连接"""
    print("\n" + "=" * 50)
    print("测试 3: API 连接测试")
    print("=" * 50)
    
    try:
        # 尝试安装 openai 库（如果未安装）
        try:
            from openai import OpenAI
        except ImportError:
            print("正在安装 openai 库...")
            os.system("pip install -q openai")
            from openai import OpenAI
        
        from utils.api_key import api_key
        
        client = OpenAI(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            api_key=api_key,
        )
        
        print("正在测试 API 连接...")
        response = client.chat.completions.create(
            model="doubao-seed-1-6-251015",
            messages=[
                {
                    "role": "user",
                    "content": "Hello, please respond with 'OK' if you can understand me."
                }
            ],
            max_tokens=50,
            temperature=0.1
        )
        
        reply = response.choices[0].message.content
        print("✓ API 连接成功")
        print(f"  模型回复: {reply}")
        return True
        
    except Exception as e:
        print(f"✗ API 连接失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("\n开始测试火山引擎豆包 API 配置...\n")
    
    results = []
    
    # 运行所有测试
    results.append(("API Key 配置", test_api_key()))
    results.append(("LLM 配置", test_llm_config()))
    
    # 询问是否进行 API 连接测试
    print("\n是否进行 API 连接测试? (需要网络连接)")
    response = input("输入 'y' 或 'yes' 继续, 其他键跳过: ").lower().strip()
    
    if response in ['y', 'yes']:
        results.append(("API 连接", test_api_connection()))
    else:
        print("跳过 API 连接测试")
    
    # 总结
    print("\n" + "=" * 50)
    print("测试总结")
    print("=" * 50)
    
    for test_name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{test_name}: {status}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("\n🎉 所有测试通过! 配置正确。")
        return 0
    else:
        print("\n⚠️ 有测试失败，请检查配置。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
