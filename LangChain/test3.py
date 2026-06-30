from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# LangChain 封装了更上层的方法，让我们初始化模型
deep_seek_model = init_chat_model("deepseek-v4-flash", model_provider="deepseek")

print(f"deepseek:{deep_seek_model.invoke("你是谁？")}")


# 定义可配置的模型(模型模拟器)
config_model = init_chat_model(temperature=0.3)
messages = [
    SystemMessage(content="请补全一段故事，100个字以内： "),
    HumanMessage(content="一只猫正在")
]

# .invoke() 的config参数才真正意义上定义了模型
print(f"config_model:{config_model.invoke(input=messages, config={"configurable" : {"model" : "deepseek-v4-flash"}}).content}")

model = init_chat_model(
    "deepseek-v4-flash",
    model_provider="deepseek",
    temperature=0.3,
    max_tokens=1024,
    configurable_fields=("max_tokens",),
    config_prefix="first",
)
messages = [
    SystemMessage(content="请补全一段故事，100个字以内： "),
    HumanMessage(content="一只猫正在")
]
result = model.invoke(
    messages,
    config={
        "configurable":{
            "first_max_tokens" : 100,
        }
    }
)

print(result.content)