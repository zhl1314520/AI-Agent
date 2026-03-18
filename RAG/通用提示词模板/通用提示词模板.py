from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

"""
zero-shot思想：
    基于 PromptTemplate 直接完成
"""
prompt_template = PromptTemplate.from_template("我是{major}专业学生，今天有{number}节课，这个专业是工科。每天不超过{number}节课，一周有多少节课，直接回答")

# 调用 format 方法注入信息
prompt_text = prompt_template.format(major="计算机", number=3)

model = Tongyi(model="qwen-max")
result = model.stream(input=prompt_text)
for chunk in result:
    print(chunk, end="", flush=True)