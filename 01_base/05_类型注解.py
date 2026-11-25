
"""
类型注解：跟 ts 差不多
  - 类型推断：当不写类型注解时，Python 解释器会自动推断出变量、表达式或函数返回值的数据类型
    - 这在 ts 里面也有一样的功能
  - 类型注解主要是用于代码提示，非强制约束，即使类型赋值不匹配，运行时也不会报错
"""

a: int = 10
b: str = 'hello'
c: float = 6.3
d: bool = True
e: None = None # 注意：type(Node) 为 NodeType

l1: list[int] = [1, 2, 3]
t1: tuple[str, int, int] = ('h', 1, 2)
s1: set[str] = {'a', 'b', 'c'}
d1: dict[str, int] = { 'a': 1, 'b': 2, 'c': 3 }

def calc(scores: list[int]) -> float:
    return round(sum(scores) / len(scores), 1)

print(calc([26,63,89,62,45,87,56]))
