
"""
面向对象
  - 类名定义规范：大驼峰命名法
  - 魔法方法：以双下划线开头和结尾的特殊方法，用于定义类的特殊行为
    - 例如 __init__ 就是魔法方法（__init__ 等同于 js 的构造函数）
    - __str__，字符串表示的方法
    - __eq__，比较两个对象是否相等（equal）
    - __lt__，__le__，__gt__，__ge__
      - 支持比较两个对象的大小，小于(less than)，小于等于(less than or equal)，大于(greater than)，大于等于(greater than or equal)
    - 类属性：直接定义在类里面的属性，可以理解为静态属性，实例对象可以访问
      - 实例对象访问属性，先在自己身上找，找不到再去类属性里面找
      - 无法通过 (实例对象.类属性 = 值) 的方式修改类属性，这种写法实际是在编辑实例对象上的属性
      - 注意：在 js 里面，实例对象无法访问静态属性
"""

class Car:
    # 类属性
    wheel = 4
    tax_rate = 0.1
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price
    def __str__(self):
        return f'{self.color}-{self.brand}-{self.name}'
    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name
    # __lt__ 和 __gt__ 只用写一个就行，另一个会自动取反
    def __lt__(self, other):
        return self.price < other.price

    def start(self):
        print(f'{self.brand} {self.name} 启动！')

car1 = Car('red', 'BMW', 'x7', 80)
car2 = Car('red', 'BMW', 'x7', 80)

# 会以字典的形式打印出对象所有的属性
print(car1.__dict__)

car1.start()

# 默认会输出对象所在的内存地址相关信息
# 可以被 __str__ 改写
print(car1, car2)

# 默认会比较两个对象所在的内存地址，那肯定是不相等的
# 可以被 __eq__ 改写，self 是 car1，other 是 car2，other 也可以是其它值，但是要遵循 __eq__ 的定义
print(car1 == car2)

# 默认情况下会报错，无法比较大小
# 可以被 __lt__ 改写，self 是 car1，other 是 car2，other 也可以是其它值，但是要遵循 __lt__ 的定义
print(car1 < car1)
