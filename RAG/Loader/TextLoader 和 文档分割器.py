from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = TextLoader(file_path="./data/significantly.txt", encoding="utf-8")

docs = loader.load()  # [Document]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,           # 分段的最大字符数
    chunk_overlap=50,         # 分段之间允许重叠字符数
    separators=["\n\n", "\n", "。", "！", "?", ".", "!", "?", " ", ""],  # 文本自然段落分隔的依据符号
    length_function=len,      # 统计字符的依据函数
)

splitter_documents = splitter.split_documents(docs)
print(len(splitter_documents))
for document in splitter_documents:
    print("=" * 20)
    print(document)
    print("=" * 20)
