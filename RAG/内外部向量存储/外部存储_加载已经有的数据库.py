from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import DashScopeEmbeddings

embedding = DashScopeEmbeddings()

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

# 查询
result = vector_store.similarity_search("Python是不是简单易学呀", k=3)

for doc in result:
    print(doc.page_content)
    print("=" * 40)