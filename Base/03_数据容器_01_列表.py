
"""
列表：对应 js 的数组
  - 提供反向索引，-1、-2 从后往前数，js 中没有这个功能
  - 不能给一个不存在的索引赋值，js 中可以
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

""" 列表常用函数 """

arr = [1, 2, 3, 4]
print(len(arr))
print(sum(arr))
