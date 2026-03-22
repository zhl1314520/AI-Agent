from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# embedding
embedding = DashScopeEmbeddings()

# 加载数据
loader = CSVLoader(
    file_path="../Loader/data/info.csv",
    encoding="utf-8",
    source_column="source",
)

documents = loader.load()

# 初始化 Chroma（持久化关键在 persist_directory）
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory="./chroma_db"   # 本地存储目录
)

# 一定要手动持久化（部分版本需要）
vector_store.persist()

# 查询
result = vector_store.similarity_search(
    query="Python是不是简单易学呀",
    k=3
)

for doc in result:
    print(doc.page_content)
    print(doc.metadata)
    print("=" * 40)