
"""
字典（dict）：更像 js 的对象，而不是 Map
  - 字典中的 value 可以是任何类型的数据，而 key 只能为不可变类型数据（可变类型数据不可为 key，例如：list、set、dict 都不行）
    - 字符串、数字、元组，都是不可变数据，是可以作为 key 的
    - 这也是它更像 js 中对象的原因，因为 js 中 Map 的 key 可以是任何数据类型
  - 字符串类型的 key 不可以省略双/单引号
  - key 不能重复，如果重复，后面的值会覆盖前面的值，和 js 一样
"""

# d1 = { 'a': 1, 'b': 2, 'c': 3 }
# print(d1, d1['a'])

# d2 = { 1: 'a', 2: 'b', 3: 'c' }
# print(d2, d2[1])

# # 修改
# d1['d'] = 10
# d1[2.5] = 15
# d1['元','组'] = 20
# print(d1)

# # 空数组
# d3 = {}
# d4 = dict()
# print(d3, d4, type(d3))

"""
常用操作（增删改查）：
  - 添加：
    - dict[key] = value，往指定字典中添加 key-value 键值对，dict1['孙权'] = 688
  - 删除：
    - dict.pop(key)，删除字典中指定的 key，并返回该 key 对应的 value，score = dict1.pop('曹操')
    - del dict[key]，删除字典中指定的键值对，del dict1['张飞']
  - 修改：
    - dict[key] = value，修改字典中指定的 key 对应的值，dict1['孙权'] = 658
  - 查询：
    - dict[key]，根据 key 获取 value，dict1['关羽']
    - dict.get(key)，根据 key 获取 value，dict1.get("关羽")
    - dict.keys()，获取所有的 key，dict1.keys()
    - dict.values()，获取所有的 value，dict1.values()
    - dict.items()，获取所有的 key-value 键值对，dict1.items()
"""

# d1 = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

# # 删除
# value = d1.pop('d')
# print(value)

# # 获取所有的 key、value、key-value
# print(d1.keys(), type(d1.keys()))
# print(d1.values(), type(d1.values()))
# print(d1.items(), type(d1.items()))

# # 遍历
# for key,value in d1.items():
#     print(key, value)
