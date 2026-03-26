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
    accept_multiple_files=True,  # 允许多文件上传
)

# session_state 是一个字典
if "service" not in streamlit.session_state:
    service = KnowledgeBaseService()
    streamlit.session_state.service = service

if uploader_file:
    for file in uploader_file:
        file_name = file.name
        file_type = file.type
        file_size = file.size / 1024

        streamlit.subheader(f"文件名：{file_name}")
        streamlit.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

        text = file.getvalue().decode("utf-8")

        with streamlit.spinner("正在处理..."):
            time.sleep(1)
            result = streamlit.session_state["service"].upload_by_str(text, file_name)
            streamlit.write(result)
