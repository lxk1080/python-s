
# __all__ 是一个模块级别的特殊变量，用于指定 from 模块名 import * 时会导入哪些功能
# 这并不会影响其它的导入方式，只会影响 from 模块名 import * 这一种方式
# 如果不对 __all__ 进行定义，则默认所有功能都会被导入，注意：这和包不同，包内必须要定义，否则为空
__all__ = ['ZAHN_DUI', 'log_sep2', 'log_sep3']

NUM = 10
ZAHN_DUI = '刘备'

def log_sep1():
    print('-' * 30)

def log_sep2():
    print('*' * 30)

def log_sep3():
    print('#' * 30)

# __name__ 是 Python 中的内置变量，表示当前模块的名字
# 直接运行该模块，__name__ 的值为 '__main__'
# 当该模块被导入而执行时，__name__ 的值就是该模块名

# 直接运行该模块时执行，被导入时不执行
if __name__ == '__main__':
    log_sep1()
