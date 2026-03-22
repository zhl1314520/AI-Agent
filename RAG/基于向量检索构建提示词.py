from langchain_community.chat_models import ChatTongyi
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 模型
model = ChatTongyi(model="qwen3-max")

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}。"),
        ("user", "用户提问：{input}")
    ]
)

# embedding
embedding = DashScopeEmbeddings(model="text-embedding-v4")

# 初始化 FAISS
vector_store = FAISS.from_texts(
    texts=["初始化数据"],   # 👈 必须至少一条
    embedding=embedding
)

# 添加数据
vector_store.add_texts([
    "减肥就是要少吃多练",
    "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来",
    "跑步是很好的运动哦"
])

# 用户提问
input_text = "怎么减肥？"

# 检索
result = vector_store.similarity_search(input_text, k=2)

# 拼接参考资料
reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

def print_prompt(prompt):
    print(prompt.to_string())
    print("=" * 40)
    return prompt

# chain
chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({
    "input": input_text,
    "context": reference_text
})

print(res)