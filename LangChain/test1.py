import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有读取到 DEEPSEEK_API_KEY，请检查 .env 文件")

# 定义模型
# 用户消息 HumanMessage
# 系统提示消息 SystemMessage 通常做为第一条消息传入
# AI 消息 AIMessage 用来返回给用户的消息
model = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url="https://api.deepseek.com",
    api_key=api_key
)

messages = [
    SystemMessage(content="请将用户输入的英文翻译成中文，只输出翻译结果。"),
    HumanMessage(content="hi!")
]

# result = model.invoke(messages)
# print(result)

# 定义输出解析组件
parser = StrOutputParser()
# print(parser.parse(result))

# 定义链
# chain = model | parser
# chain = RunnableSequence(first=model, last=parser)
chain = model.pipe(parser)

print(chain.invoke(messages))