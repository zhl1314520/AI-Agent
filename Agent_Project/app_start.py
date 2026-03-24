"""
启动：
    cd..\agentProject> streamlit run Agent_Project/app_start.py
"""
import sys
import os

# 把项目根目录加入路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import time

import streamlit

from Agent_Project.agent.react_agent import ReactAgent

# 标题
streamlit.title("Customer Service for Smart Robot Vacuum Cleaners")
streamlit.divider()

if "agent" not in streamlit.session_state:
    streamlit.session_state["agent"] = ReactAgent()

if "message" not in streamlit.session_state:
    streamlit.session_state["message"] = []

for message in streamlit.session_state["message"]:
    streamlit.chat_message(message["role"]).write(message["content"])

# 用户输入提示词
prompt = streamlit.chat_input()

if prompt:
    streamlit.chat_message("user").write(prompt)
    streamlit.session_state["message"].append({"role": "user", "content": prompt})

    response_messages = []
    with streamlit.spinner("Thinking..."):
        res_stream = streamlit.session_state["agent"].execute_stream(prompt)

        def capture(generator, cache_list):     # 捕获

            for chunk in generator:
                cache_list.append(chunk)

                for char in chunk:
                    time.sleep(0.01)
                    yield char

        streamlit.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        streamlit.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
        streamlit.rerun()