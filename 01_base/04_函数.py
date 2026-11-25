
"""
函数：和 js 的 function 类似
  - 可以在函数内部首行写函数说明文档，将鼠标悬浮函数名上即可显示
"""

# 冒泡排序
def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j+1],list[j] = list[j],list[j+1]
    return list

# 选择排序
def select_sort(list):
    for i in range(len(list) - 1):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i],list[j] = list[j],list[i]
    return list

# 快速排序
def quick_sort(list):
    """ 快速排序
    :param list: list
    :return: list
    """
    if len(list) <= 1: return list
    middle = list.pop(0)
    left = []
    right = []
    for i in list:
        if i > middle:
            right.append(i)
        elif i <= middle:
            left.append(i)
    return [*quick_sort(left), middle, *quick_sort(right)]

# list = [2,3,8,5,1,6,5,4,3,9,7]

# print(bubble_sort(list))
# print(select_sort(list))
# print(quick_sort(list))

# # 函数说明文档
# print(help(quick_sort))

""" 求分数平均值 """

def calc_score(list):
    return round(sum(list) / len(list), 1) # 保留一位小数

# print(calc_score([89, 75, 66, 95, 93, 82]))

"""
函数作用域：
  - 作用域：函数内部可以获取全局变量，但函数内部无法直接修改全局变量，函数内部所有的变量定义都是独立于函数体内的，与外部无关
    - 如果是 js，则会改变外部的变量值：let a = 1; function change() { a = 100 }; change(); console.log(a); 此时 a 的值会变为 100
    - 如果 js 要想内部和外部无关，则需严格定义：let a = 1; function change() { let a = 100 }; change(); console.log(a); 内部定义使用 let 即可
  - python 提供 global 关键字，在函数内部声明 global var，此时 var = value，这个变量改的就是全局变量的值
    - 一般不建议在函数内部修改全局变量，因为这会让代码变得难以维护，当然一些特殊场景还是可以用，例如需要维护一些全局状态
"""

num = 10

def func1():
    print(num) # 获取全局变量 num

# func1()

def func2():
    print(num) # 会报错，因为函数内部定义了 num，但代码走到这一步时变量还未赋值
    num = 20

# func2()

def func3():
    num = 30 # 这里的变量 num 和外部的 num 没有任何关系，此处的变量只作用于函数内部
    print(num) # 30

# func3() # 函数执行，不会改变外部的 num 值
# print(num) # 10

def func4():
    global num # 声明这个 num 是全局变量
    num = 40 # 此时的赋值就是改的全局变量
    print(num) # 40

# func4() # 函数执行，内部声明了全局变量，所以全局 num 会被改变
# print(num) # 40

"""
函数传参：
  - 位置传参
  - 关键字传参
  - 默认参数
    - 默认参数必须要放到非默认参数之后
  - 不定长参数
    - 位置传参：*args，args 是元组
    - 关键字传参：**kwargs，kwargs 是字典
"""

def reg_stu(name, age, gender, city):
    return name, age, gender, city

# # 位置传参
# print(reg_stu('张三', 20, '女', '上海'))

# # 关键字传参
# print(reg_stu(name='张三', gender='女', city='上海', age=20))

# # 混用，必须位置传参在前，关键字传参在后
# print(reg_stu('张三', 20, gender='女', city='上海'))

def reg_user(name, age, type='novip'):
    return name, age, type

# print(reg_user('张三', 20))

def calc_sum(*args, **kwargs):
    if kwargs.get('a') is not None: print('a 有值')
    if kwargs.get('b') != None: print('b 有值')
    return sum([*args, kwargs.get('a'), kwargs.get('b')])

# print(calc_sum(1, 2, 3, 4, a=5, b=6))

# 这种定义方式，最后的 fixed 必须使用关键字传参，因为如果不使用关键字传参，参数都会被归为 nums
# js 里面不支持这种写法，不定参数只能写到最后面
def calc_avg(*nums, fixed):
    return round(sum(nums) / len(nums), fixed)

# print(calc_avg(3,9,7,7,3,5,fixed=2))

# 在 python 里，是想咋写就咋写，first 自动被截取第一个参数，last 必须使用关键字传参
def log_num(first, *args, last):
    return first, args, last

# print(log_num(1,2,3,4,5,last=6))

# 参数也可以是另一个函数
def func_a(x, y): return x + y
def func_b(x, y, func): return func(x, y)

# print(func_b(2, 3, func_a))

"""
匿名函数：相当于 js 的箭头函数
  - 没有名称的函数，需要通过 lambda 表达式来声明函数，可以简化简单函数的编写（单行表达式）
    - 不能换行，只能写单行，语法：lambda 参数 : 函数体
  - 比 js 的箭头函数还是差点意思，lambda 追求简洁，只能单行，不能写 return
    - 而 js 箭头函数写了大括号 {} 的话，还是可以写多行，写 return 的，在 js 中箭头函数往往会替代 function 使用
"""

# 和箭头函数一样的定义方式
getnum = lambda : 10
add = lambda x, y : x + y

# 闭包
def whatever():
    a = 10
    return lambda b : a + b

# what = whatever()
# print(what(10), what(20))

data = ['PHP', 'C', 'Python', 'Java', 'Javascript', 'Go']

# 作为回调函数使用，根据字符串长度排序
# 这个排序和 js 的排序还是有点不同的，这里可以理解为：先排数字，然后将数字替换为对应的字符串，就是一个映射关系
data.sort(key= lambda item : len(item))
# print(data)

# 由于 key 接收一个回调函数，所以也可以直接这么写
# sort 方法还可以设置是否反转参数
data.sort(key=len, reverse=True)
# print(data)

"""
案例练习：阶乘
  - 使用递归即可，属于动态规划算法
"""

def jiechen(num):
    if num <= 1: return num
    return num * jiechen(num - 1)

# print(jiechen(3))
