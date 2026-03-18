from langchain_community.llms.tongyi import Tongyi


model = Tongyi(model="qwen-max")

# 调用invoke向模型提问(一次性返回完整结果)
# ret = model.invoke(input="简单介绍 langchain 框架")
# print(ret)


# 调用stream向模型提问(流式返回结果)
ret = model.stream(input="一句话说出目前 ChatGTP-plus 订阅一个月多少$?")
for chunk in ret:
    print(chunk, end="", flush=True)