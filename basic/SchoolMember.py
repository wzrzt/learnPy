#encoding=utf-8*

class SchoolMember:  # 父类，学校成员
    school_name = 'Oldboy Linux edu.'  # 第一级变量，即类属性

    def __init__(self, name, gender, nationality='CN'):  # 构造函数
        self.name = name
        self.gender = gender
        self.nation = nationality

    def tell(self):  # 普通的类方法
        print('Hi, my name is %s , I am from %s' % (self.name, self.nation))


class Student(SchoolMember):  # 子类，学生，继承父类学校成员的相关属性
    def __init__(self, Name, Gender, Class, Score, Nation='US'):  # 子类下的方法
        SchoolMember.__init__(self, Name, Gender, Nation)  # 让父类使用子类传递过去的参数
        self.Class = Class
        self.Score = Score

    def payTuition(self, amount):  # 子类下的方法
        if amount < 6499:
            print('Get the fuck off...')
        else:
            print('Welcome onboard!')


class Teacher(SchoolMember):  # 子类，老师，继承父类学校成员的相关属性
    def __init__(self, Name, Gender, Course, Salary, Nation='FR'):
        SchoolMember.__init__(self, Name, Gender, Nation)
        self.course = Course
        self.Salary = Salary

    def teaching(self):
        print('I am teaching %s, i am making %s per month !' % (self.course, self.Salary))


S1 = Student('WangFanHao', 'Male', 'Python', 'C+', 'JP')  # 实例化一个子类对象，学生
S1.tell()  # 直接继承父类中的tell()方法
S1.payTuition(4999)  # 使用子类Student()自身中的类方法
print(S1.school_name)
  # 直接继承父类的一个属性

print('*' * 60)


S2 = Student('ShitTshirt', 'Male', 'Linux', 'B')
S2.tell()
S2.payTuition(6500)
# S2.age = 29
# print S2.age

print('*' * 60)


T1 = Teacher('Alex', 'Male', 'C++', 5000)  # 实例化一个子类对象，学生
T1.tell()  # 直接继承父类中的tell()方法
T1.teaching()  # 直接继承父类的一个属性

print('S1.name:', S1.name)   # 测试用，观察输出结果
print('S2.name:', S2.name)

print('T1.name:', T1.name)
