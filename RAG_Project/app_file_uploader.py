"""
基于Streamlit完成WEB网页上传服务
    运行：
        1.cd D:\PyCharm\Project\agent\agentProject\RAG_Project
        2.streamlit run app_file_uploader.py
"""
import time

import streamlit
from knowledge_base import KnowledgeBaseService
# 添加网页标题
streamlit.title("知识库更新服务")

# file_uploader
uploader_file = streamlit.file_uploader(
    label="请上传txt文件",
    type=['txt'],
    accept_multiple_files=False,  # False表示仅接受一个文件的上传
)

# session_state 是一个字典
if "service" not in streamlit.session_state:
    service = KnowledgeBaseService()
    streamlit.session_state.service = service

if uploader_file is not None:
    # 提取文件的信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024  # KB

    streamlit.subheader(f"文件名：{file_name}")
    streamlit.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

    # get_value -> bytes -> decode('utf-8')
    text = uploader_file.getvalue().decode("utf-8")

    with streamlit.spinner("正在处理..."):          # 显示一个加载动画
        time.sleep(1)                           # 模拟处理时间 1s
        result = streamlit.session_state["service"].upload_by_str(text, file_name)
        streamlit.write(result)
