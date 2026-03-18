from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatTongyi(model="qwen3-max")

# messages = [
#     SystemMessage(content="你是一位高级工程师。"),
#     HumanMessage(content="极其简洁地介绍 langchain 框架"),
#     AIMessage(content="LangChain 是一个用于开发由大语言模型（LLM）驱动的应用程序的开源框架。"
#                       "它提供工具和组件来轻松构建端到端应用，例如聊天机器人、文档问答系统和智能代理。"
#                       "其核心优势在于简化了将 LLM 与外部数据源、计算逻辑和其他服务集成的过程。"),
#     HumanMessage(content="再简洁一点")
# ]
# 简洁版
messages = [
    ("system","你是一位高级工程师。"),
    ("human","极其简洁地介绍 langchain 框架"),
    ("ai","LangChain 是一个用于开发由大语言模型（LLM）驱动的应用程序的开源框架。"
        "它提供工具和组件来轻松构建端到端应用，例如聊天机器人、文档问答系统和智能代理。"
        "其核心优势在于简化了将 LLM 与外部数据源、计算逻辑和其他服务集成的过程。"),
    ("human","再简洁一点")
]

result = model.stream(input=messages)

for chunk in result:
    print(chunk.content, end="", flush=True)        # .content: 返回消息内容