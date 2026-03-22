from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./data/significantly.pdf")    # 报错因为 pdf 问题

for i, doc in enumerate(loader.lazy_load(), 1):
    print(doc.page_content[:200])  # 只看前200字，避免刷屏
    print("页码:", doc.metadata.get("page"))
    print("=" * 40)

