import time
import streamlit
from rag import RagService
import config_data as config

# 标题
streamlit.title("智能客服")
streamlit.divider()  # 分隔符

if "message" not in streamlit.session_state:
    streamlit.session_state["message"] = [{"role": "assistant", "content": "Hello, what can i do for you?"}]

if "rag" not in streamlit.session_state:
    streamlit.session_state["rag"] = RagService()

for message in streamlit.session_state["message"]:
    streamlit.chat_message(message["role"]).write(message["content"])

# 在页面最下方提供用户输入栏
prompt = streamlit.chat_input()

if prompt:
    # 在页面输出用户的提问
    streamlit.chat_message("user").write(prompt)
    streamlit.session_state["message"].append({"role": "user", "content": prompt})

    ai_result_list = []

    with streamlit.spinner("Thinking..."):
        result_stream = streamlit.session_state["rag"].chain.stream({"input": prompt}, config.session_config)
        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk
        streamlit.chat_message("assistant").write_stream(capture(result_stream, ai_result_list))
        streamlit.session_state["message"].append({"role": "assistant", "content": "".join(ai_result_list)})