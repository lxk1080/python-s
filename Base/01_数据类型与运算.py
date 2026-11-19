
""" 字面量：注意这几个关键字，开头字母需要大写 """

# print(10)
# print('hello world')
# print(True)
# print(+True)
# print(False)
# print(+False)
# print(None)

""" 变量：和 js 一样，动态类型，python 里面没有常量的定义 """

# num = 110
# num = 'hello'
# print(num)

""" 一次性定义多个变量 """

# a,b = 10,20
# print(a,b)

""" 规范：变量不用驼峰，用蛇形命名法（以下划线连接），常量字母全大写，变量字母全小写 """

# USER_FIRST_NAME = 'Bob' # 常量
# user_num = 10 # 变量

""" 类型：获取类型和判断类型 """

# print(type(10))
# print(type('hello'))
# print(type(True))
# print(type(None))
# print(isinstance(10, int))
# print(isinstance('hello', str))

""" 三引号字符串：可以换行，会原封不动打印出来 """

# a = """ 
#     hello:
#         你好，欢迎学习！
#     """
# print(a)

""" 转义字符：\t 是制表符缩进，\n 是换行 """

# print('\t人生苦短！\n我学Python!\n\"哈哈\"')

"""
字符串拼接：3 种方式
  - 使用加号+拼接，int 类型需要手动转为 str 类型
  - 使用占位符 %s 拼接，% 表示我要占位，s 表示将变量转为字符串放入占位的位置
  - 使用 f'' 拼接，int 不需要做任何手动转换（内部如果有运算的话还是要转），推荐使用
"""

# name = 'python'
# version = '3.12'
# age = 35
# print('大家好，我是' + name + '，版本是' + version + '，今年' + str(age) + '岁')
# print('大家好，我是%s，版本是%s，今年%s岁' % (name,version,age))
# print(f'大家好，我是{name}，版本是{version}，今年{age}岁')

"""
算术运算符：列出了几个特殊的
  - js 也可以用 ** 表示次方的，但 // 不行，表示注释
  - 注意一：python 里面除法运算的结果都是浮点数（float）
  - 注意二：只要有浮点数参与运算，结果都是浮点数
"""

# print(10 // 3) # 整除（向下取整）
# print(10 ** 3) # 10 的 3 次方
# print(850/10) # 85.0
# print(10//2.0) # 5.0

"""
精度问题：计算机底层使用二进制存储数据，有些小数无法精确表示，python 同样也有精度问题
  - 使用进位退位法，可以解决此问题
"""

# print(0.3 - 0.2)
# print((0.3*10 - 0.2*10)/10)

""" 比较运算符：python 里没有三等号 """

# print(10 == 100 - 90)

""" 逻辑运算符：返回值为 或真与假 """

# print(0 or 10) # 10
# print(0 and 10) # 0
# print(not 10) # False
