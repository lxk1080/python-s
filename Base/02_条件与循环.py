
""" if 条件语句 """

# num = int(input('请输入数字：'))

# if num > 0:
#     print(f'{num} 是正数')
# elif num < 0:
#     print(f'{num} 是负数')
# else:
#     print(f'{num} 是零')

"""
match...case 等同于 switch...case，只在 python3.10 后支持
  - 注意几个地方：
    - 可以使用 | 进行多值匹配，js 中需要 case v1: case v2: 写多次
    - 最后没匹配到使用 case _ 语法，js 中是使用 default
    - 匹配到后直接中断执行，而 js 如果不写 break 是不会中断的，还会接着匹配后面的
    - case...if 语法，新姿势：只有 if 条件成立时，才匹配这个 case
"""

# num = int(input('请输入数字：'))

# match num:
#     case 1:
#         print('星期一')
#     case 2 if num < 10:
#         print('星期二')
#     case 3:
#         print('星期三')
#     case 4:
#         print('星期四')
#     case 5:
#         print('星期五')
#     case 6|7:
#         print('周末')
#     case _:
#         print('没匹配到')

"""
循环语句
  - else 语句：循环正常结束后执行，如果循环异常结束（包括 break），则不会执行
  - for...in 就类似 js 的 for...of 语法，js 里的 for...in 拿的是元素的下标
  - range(start, end, step) 语句，start 默认 0，step 可以不写，范围不包含 end 本身
  - print 语句，默认自带一个换行符作为结束
    - 可以设置最后一个参数 end = '' 不换行，默认 end = '\n'，当然这个 end 也可以设置为其它的值
"""

# num = 5
# while num > 0:
#     print(num)
#     num -= 1
# else:
#     print('while循环完了')

# -----------------------------------------------

# for num in reversed(range(1, 6)):
#     print(num)
# else:
#     print('for循环完了')

# -----------------------------------------------

# for letter in 'qwerty':
#     print(letter)
# else:
#     print('letter循环完了')

# -----------------------------------------------

# for num in range(1, 10, 2): # 不包含 10 本身
#     print(num)

# -----------------------------------------------

# row = 5
# column = 10
# for i in range(row):
#     for j in range(column):
#         print('x', end = '-')
#     print()

# -----------------------------------------------
# 九九乘法表

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j} x {i} = {j * i}', end = '  ')
#     print()
