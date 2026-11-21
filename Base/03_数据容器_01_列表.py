
"""
列表：对应 js 的数组
  - 提供反向索引，-1、-2 从后往前数，js 中没有这个功能
  - 注意：不能给一个不存在的索引赋值，js 中可以
"""

# arr = [1, 2, 3, 4, 5, 6, 'A', True]

# 获取
# print(arr[0], arr[-1])

# 修改赋值
# arr[5] = 8

# 报错，不存在的索引
# arr[10] = 'B'

# 删除
# del arr[1]

# 遍历
# for item in arr:
#     print(item)

"""
切片语法：序列数据[开始索引=0:结束索引=列表长度:步长=1]
  - 切片不包含结束索引对应的元素
  - 可以使用反向索引
"""

# arr = [1, 2, 3, 4, 5, 6]

# print(arr[::])
# print(arr[0:5:1])
# print(arr[:5:1])
# print(arr[:5:])
# print(arr[:5])
# print(arr[0:5:2])
# print(arr[0:-1])

"""
常用方法：
  - append()，在列表的尾部追加元素，s.append(10086)
  - insert()，在指定索引之前，插入该元素，s.insert(0, 92)
  - remove()，移除列表中第一个匹配到的值，注意是值，s.remove(75)
  - pop()，删除列表中指定索引位置的元素（如果未指定索引，默认删最后一个），s.pop(2) / s.pop()
  - sort()，对列表进行排序（列表元素的数据类型一致，才可以进行排序），s.sort()
  - reverse()，反转列表元素，s.reverse()
"""

# arr = [2, 1, 3, 4, 5]

# arr.append(100)
# print(arr)
# arr.insert(0, 0)
# print(arr)
# arr.remove(100)
# print(arr)
# arr.pop()
# print(arr)
# arr.sort()
# print(arr)
# arr.reverse()
# print(arr)

""" 常用函数 """

# arr = [1, 2, 3, 4]

# print('长度', len(arr))
# print('求和', sum(arr))
# print('最小', min(arr))
# print('最大', max(arr))

""" 去重：可以使用 item in list 判断列表中是否包含这个元素 """

# arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# list = []
# for item in arr:
#     if item not in list:
#         list.append(item)
# print(list)

"""
列表合并：
  - 解包：将列表中的元素解开成一个个独立的元素，用 * 号表示，就等同于 js 的三点 ... 扩展运算符
  - 相加：直接将两个列表相加，也可以合并
"""

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [6, 7, 8, 9, 10]
# arr3 = [*arr1, *arr2]
# arr4 = arr1 + arr2
# print(arr3)
# print(arr4)

"""
列表推导式：按照一定的规则快速生成一个列表，语法：[要插入列表的数据 for i in 列表 if 条件]
"""

# arr = [i**2 for i in range(1, 11)] # 让数字 1~10 的平方组成一个列表
# print(arr)
# arr2 = [i**2 for i in range(1, 11) if i % 2 == 0] # 让数字 1~10 中的偶数的平方组成一个列表
# print(arr2)

"""
获取列表中元素的索引：
  - list.index(item) 返回第一个匹配项的索引
  - 通过 enumerate(list) 可以 for i,v 遍历，i 是索引，v 是元素值
"""

# arr = ['a', 'b', 'c', 'd', 'c']

# print(arr.index('c')) # 第一个匹配项的索引
# print([i for i, v in enumerate(arr) if v == 'c']) # 所有匹配项的索引
