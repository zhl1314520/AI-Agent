from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/data.csv",
    csv_args={
        "delimiter": ",",       # 指定分隔符
        "quotechar": '"',       # 指定带有分隔符文本的引号包围是单引号还是双引号
        # 如果数据原本有表头，则不需要指定fieldnames
        "fieldnames": ['name', 'age', 'gender', 'hobby']
    },
    encoding="utf-8"
)

# 批量加载 .load() -> [Document, Document, ...]
documents = loader.load()
for document in documents:
    print(type(document), document)

# 懒加载  .lazy_load()
# for document in loader.lazy_load():
#     print(document)