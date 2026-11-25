
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f'姓名：{self.name} 语文：{self.chinese} 数学：{self.math} 英语：{self.english}'

    def update_score(self, chinese = None, math = None, english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EduManagement:
    version = '1.0.0'
    name = '教务管理系统'

    def __init__(self):
        self.student_list = []

    # 添加学生
    def add_student(self):
        name = input('请输入学生姓名：')
        if name in [s.name for s in self.student_list if s.name == name]:
            return print('该学生已存在！')
        
        chinese = int(input('语文成绩：'))
        math = int(input('数学成绩：'))
        english = int(input('英语成绩：'))

        if chinese not in range(0, 101) or math not in range(0, 101) or english not in range(0, 101):
            return print('输入的成绩不合法！')

        student = Student(name, chinese, math, english)
        self.student_list.append(student)
        print('学生添加成功！')

    # 修改学生
    def update_student(self):
        name = input('请输入学生姓名：')
        s_list = [s for s in self.student_list if s.name == name]
        if len(s_list) == 0:
            return print('该学生不存在！')
        
        chinese = int(input('语文成绩：'))
        math = int(input('数学成绩：'))
        english = int(input('英语成绩：'))
        
        if chinese not in range(0, 101) or math not in range(0, 101) or english not in range(0, 101):
            return print('输入的成绩不合法！')
        
        student = s_list[0]
        student.update_score(chinese, math, english)
        print('学生信息修改成功！')

    # 查询学生
    def query_student(self):
        name = input('请输入学生姓名：')
        s_list = [s for s in self.student_list if s.name == name]
        if len(s_list) == 0:
            return print('该学生不存在！')
        student = s_list[0]
        print(student)

    # 查询所有学生
    def query_all_student(self):
        for s in self.student_list:
            print(s)

    # 删除学生
    def remove_student(self):
        name = input('请输入学生姓名：')
        s_list = [s for s in self.student_list if s.name == name]
        if len(s_list) == 0:
            return print('该学生不存在！')
        student = s_list[0]
        self.student_list.remove(student)
        print('学生删除成功！')

    # 运行教务系统
    def run(self):
        print(f'欢迎来到{EduManagement.name}！版本 V{EduManagement.version}')
        while True:
            print('--------------------------------------------------------------------------------------')
            print('-    1. 添加学生  2. 修改学生  3. 查询学生  4. 查询所有学生  5. 删除学生  6. 退出    -')
            print('--------------------------------------------------------------------------------------')

            operation = int(input('请输入操作：'))

            try:
                match operation:
                    case 1:
                        self.add_student()
                    case 2:
                        self.update_student()
                    case 3:
                        self.query_student()
                    case 4:
                        self.query_all_student()
                    case 5:
                        self.remove_student()
                    case 6:
                        print('再见~')
                        break
                    case _:
                        print('输入的指令不正确，请重新输入！')
            except ValueError:
                print('输入的数据有问题，请重新选择！')
            except Exception:
                print('程序运行出错了，请重新选择~')

""" 运行代码 """

if __name__ == '__main__':
    eduManagement = EduManagement()
    eduManagement.run()
