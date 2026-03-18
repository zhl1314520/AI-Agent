from openai import OpenAI

# 1.获取 client 对象，OpenAI 类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        # 系统角色:"总指挥"，优先级最高。能够（设定行为准则：告诉模型应该以什么身份说话），（约束输出格式）
        {"role": "system", "content": "你是一位高级工程师，不说废话，抓住重点，回答简洁明了"},
        # 用于模型上下文记忆的，不需要记忆就注释（开头一般不用）
        # {"role": "assistant", "content": "上轮模型的回复"},
        {"role": "user", "content": "目前 ChatGTP-plus 订阅一个月多少$?"}
    ],
    stream=True     # 流式输出模式
)

# 3. 处理结果
# print(response.choices[0].message.content)
# 流式输出
for chunk in response:
    content = chunk.choices[0].delta.content
    if content:  # 防止 None
        print(content, end="", flush=True)  # flush=True 刷新缓冲区
print()  # 最后换行（可选）