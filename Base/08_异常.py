
"""
处理异常
  - 语法：try...except...finally
  - 异常可以按照不同种类一一捕获，也可以胡子眉毛一把抓使用 Exception 捕获，Exception 是所有其它异常的父类
  - 异常的传递：异常在函数调用中层层上报的过程，直到有人处理它，或者程序崩溃
"""

try:
    print("-----start-----")
    # print(my_name)
    # print(1 / 0)
    # print('ABC'[10])
    print('ABC'.hello)
    print("-----end-----")
except NameError as e:
    print('名字不存在，请检查变量或函数名字，异常信息：', e)
except ZeroDivisionError as e:
    print('0 不能做被除数，异常信息：', e)
except IndexError as e:
    print('索引错误，异常信息：', e)
except Exception as e:
    print('程序运行出错了，错误信息：', e)
finally:
    print('执行结束！')

# 异常的传递：在最外层捕获异常即可

def fun1():
    print('fun1 running ... ')
    fun2()

def fun2():
    print('fun2 running ... ')
    fun3()

def fun3():
    print('fun3 running ... ')
    print([][0])

try:
    fun1()
except Exception as error:
    print('程序运行出错了：', error)
