from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings(model="text-embedding-v1")

print(model.embed_query("这是一个测试"))
print(model.embed_documents(["这是一个测试", "这是一个测试2"]))