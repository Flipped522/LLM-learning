import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有读取到 DEEPSEEK_API_KEY，请检查 .env 文件")

model = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url="https://api.deepseek.com",
    api_key=api_key,
    temperature=2,  # 采样温度
    # max_tokens=None,
    # max_retries=2
)

messages = [
    SystemMessage(content="请帮我补全故事，100个字以内"),
    HumanMessage(content="一只猫正在")
]

parser = StrOutputParser()

# 定义链
chain = model | parser

print(chain.invoke(messages))