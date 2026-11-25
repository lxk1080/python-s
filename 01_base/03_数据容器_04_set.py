
""" 集合（set）：无序、不重复、可修改，所有编程语言的 set 都是这特性 """

# s1 = {'a', 'b', 'a', 'c', 'b'}
# print(s1, type(s1)) # 每次输出顺序都不一样（无序）

# 定义空集合
# 注意：定义空集合不能使用空的大括号 {}，这是字典

# s2 = set()
# print(s2, type(s2))
# s3 = {}
# print(s3, type(s3))

"""
常用方法：
  - add()，添加元素到集合中，s1.add('t')
  - remove()，移除集合中的指定元素（指定元素不存在将报错），s1.remove('t')
  - pop()，随机删除集合中的元素并返回，e = s1.pop()
  - clear()，清空集合，s1.clear()
  - difference()，求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素），s1.difference(s2)
  - union()，求取两个集合的并集，s1.union(s2)
  - intersection()，求取两个集合的交集，s1.intersection(s2)
    - 取交集、并集、差集的这三个方法，在 js 的 set 中也有一模一样的方法名和功能
"""

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}

# print(s1.difference(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))

""" 取交集、并集、差集也可以使用运算符：这些在 js 里面都不支持 """

# print(s1 & s2) # 交集
# print(s1 | s2) # 并集
# print(s1 - s2) # 差集，从 s1 中去掉 s2 中也含有的元素

""" 集合推导式：和列表推导式差不多，就只有括号不一样 """

# print({s for s in s1 if s in s2}) # 交集

""" 利用 set 进行列表去重 """

# arr = [1,2,3,1,2,4,5,3,2]
# arr1 = [*set(arr)]
# print(arr1)

"""
案例：统计每个学生选了几门课
  - 为什么我要写这个案例？
    - 这个案例本身没啥，主要是它涉及到不同语言的编程思想
    - 一开始我是想通过 if item in set 去判断学生是否选了某课，如果选了就 选课数量+1，最终得到总共选了几课
    - 那为啥我没想到下面代码写的这个方式？主要是因为我在用 js 的编程思想
      - 因为如果是 js，上面条件判断的方式是可行的，当然合并为数组也行，但是实现也并不简洁
      - 如果是 js 合并为数组，那后面就是 data = arr.recude((prev, cur) => { prev[cur] = (prev[cur] || 0) + 1; return prev }, {})
      - 遍历一次，一次性获取所有学生的选课总数，但是在 python 里面，列表没有这种函数，所以我没想到要合并成列表
    - 所以根本问题就是：我没想到列表是有 list.count(item) 这个方法的，就像我所说，我在用 js 的编程思想，没用 python 的编程思想
    - 可以看到，python 在这方面总是有很简洁的语法，这也让我更加理解了为什么说 python 语言在处理数据方面非常强，适合处理大量数据
    - 之所以写这个案例在这，就是为了提醒自己，在写 python 时，需要优先想起它擅长处理数据的特性，不能再用 js 的特性去想如何处理数据
"""

# yuwen = {'曹操', '刘备', '张飞', '关羽', '小乔', '周瑜'}
# shuxue = {'袁绍', '董卓', '吕布', '曹操', '张飞', '鲁肃'}
# yingyu = {'孙权', '吕蒙', '貂蝉', '关羽', '董卓', '张飞'}
# yishu = {'周瑜', '小乔', '大乔', '刘备', '貂蝉', '孙尚香'}

# # set 取并集，去掉重复的，就是所有的学生
# all_students = yuwen | shuxue | yingyu | yishu

# # 列表不会去重，后续直接使用 list.count(item) 获取元素出现次数
# all_items = [*yuwen, *shuxue, *yingyu, *yishu]

# for student in all_students:
#     print(f'{student} 选了 {all_items.count(student)} 个课程')
