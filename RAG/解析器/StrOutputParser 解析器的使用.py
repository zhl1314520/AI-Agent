from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import AIMessage

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "姓：{lastname}，刚生了{gender}。请起名，仅告知我名字无需其它内容。"
)

"""
chain = prompt | model | model
    如果是这样写的话，由于 model 模型的输出是 AIMessage 类型的，不能当作下一个 model 的输入，需要转为字符串
"""
chain = prompt | model | parser | model

res: AIMessage = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res.content)
print(type(res))