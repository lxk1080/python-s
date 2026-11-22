
""" 元组（tuple）：和列表最大的区别就是，不可修改 """

# tup = (1, 2, 3, 4, 5, 3, 5)
# print(tup, type(tup), tup[0], tup[-1])

# 定义元组也可以不要括号
# tup2 = 1,2,3,4,5
# print(tup2, type(tup2))

# 空元组定义
# t1 = ()
# t2 = tuple()
# print(t1, t2, type(t1), type(t2))

# 常用的两个方法
# print(tup.index(5)) # 返回第一个匹配项的索引
# print(tup.count(5)) # 返回匹配到的个数

# 和列表一样，找不到元素会报错
# print(tup.index(10))

# 切片，和列表一样
# print(tup[::-1])

# 注意：如果元组里面只有一个值，那外面的小括号会被当成作用域形式的括号
# 注意：除了空元组，定义元组至少要有一个逗号

# t3 = (100)
# print(t3, type(t3)) # int 类型
# t4 = (100,)
# print(t4, type(t4)) # tuple 类型

""" 解包：和列表一样 """

# t = 1,2,3,4,5

# a, *b, c = t
# print(a, b, c)

""" 基于解包的变量交换：这个方式在 js 里面也是支持的，通过数组解构 [a, b] = [b, a] """

# a = 10
# b = 20
# a,b = b,a
# print(a, b)

"""
元组+解包：也常用于多个变量的单行定义
  - 其实在 js 里面也可以这么做，例如 let [a, b, c] = [10, 20, 30]，但是看起来不够优雅
"""

# name, age, hobby = '乔丹', 30, '打球'
# print(name, age, hobby)
