
""" 字符串：不可变性（无法修改）、有序性、可迭代性 """

# str = 'hello-python'

# 获取
# print(str[0], str[-1])

# 无法赋值，会报错
# str[0] = 'A'

# 遍历
# for c in str:
#     print(c)

# 切片截取，和列表一样
# print(str[:5])
# print(str[6:])
# print(str[::2])
# print(str[::-1])

"""
常用方法：
  - find()，在字符串中查找子串，返回第一次出现的索引位置，找不到返回 -1，s.find('Python')
    - 注意：只有字符串在找不到时会返回 -1，像列表、元组找不到会直接报错
  - count()，统计子串在字符串中出现的次数，s.count('H')
  - upper()，将字符串中的所有字母转换为大写，s.upper()
  - lower()，将字符串中的所有字母转换为小写，s.lower()
  - split()，将字符串按指定分隔符分割成列表，s.split(' ')
  - strip()，去除字符串两端的空白字符或指定字符，s.strip() / s.strip('*')
  - replace()，将字符串中的指定子串替换为新的子串，s.replace('H', 'C')
  - startswith()，检查字符串是否以指定子串开头，返回布尔值，s.startswith('P')
  - endswith()，检查字符串是否以指定子串结尾，返回布尔值，s.endswith('n')
"""

# str = 'hello'
# print(str.find('l'))
# print(str.find('t'))
# print(str.startswith('h'))
# print(str.endswith('o'))
