from langchain_community.chat_models import ChatTongyi
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document

model = ChatTongyi(model="qwen3-max")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "你是一个专业助手，请严格基于提供的参考资料回答问题。\n"
         "如果参考资料不足，请说明“根据已有资料无法回答”。\n\n"
         "参考资料：\n{context}"
        ),
        ("user", "用户提问：{input}")
    ]
)

embedding = DashScopeEmbeddings(model="text-embedding-v4")

texts = [
    "减肥就是要少吃多练",
    "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来",
    "跑步是很好的运动哦"
]

vector_store = FAISS.from_texts(texts, embedding)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 格式化函数（转换类型）
def format_func(docs: list[Document]):
    if not docs:
        return "无相关参考资料"

    return "\n\n".join(
        f"参考{i+1}：{doc.page_content}"
        for i, doc in enumerate(docs)
    )

def print_prompt(prompt):
    print(prompt.to_string())
    print("=" * 40)
    return prompt

"""
retriever:
  - 输入：用户的提问        类型： str
  - 输出：向量库的检索结果         list[Document]

prompt:
  - 输入：用户的提问 + 向量库的检索结果     dict
  - 输出：完整的提示词                   PromptValue
"""
chain = (
    # invoke首先进入 retriever，但是RunnablePassthrough会分流一部分。所以是invoke会同时进入retriever和 input 里面
    {"input": RunnablePassthrough(), "context": retriever | format_func}
    | prompt
    | print_prompt
    | model
    | StrOutputParser()
)

res = chain.invoke("怎么减肥？")
print(res)