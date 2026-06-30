from typing_extensions import Annotated

from langchain_core.tools import tool

# 定义工具
@tool
def add(
        a: Annotated[int, ..., "第一个整数"],
        b: Annotated[int, ..., "第二个整数"],
) -> int:
    """
    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a + b

print(add.invoke({"a":2, "b":3}))
print(add.name)
print(add.description)
print(add.args)