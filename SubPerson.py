from Person import Person


class Student(Person):

    def __init__(self, age=24, name='Nick', height=1.85, gender='male', grade=9):
        Person.__init__(self)
        self.__grade = grade

    def setGrade(self, grade):
        self.__grade = grade

    def getGrade(self):
        return self.__grade

    def greet(self):
        print("Good morning, I'm", self.getName(), ".")


class Teacher(Person):

    def __init__(self, age, name, height, gender, degree='Master'):
        Person.__init__(self, age=30, name='Park', height=1.85, gender='male')
        self.degreee = degree
        self.age = age
        self.name = name
        self.height = height
        self.gender = gender


    def setDegree(self, degree):
        self.degree = degree

    def getDegree(self):
        return self.degree

    def greet(self):
        print("Good morning, I'm  a Mr. %s." % self.getName(), end = '')

# if __name__ == "__main__":
#     s1 = Student()
#     t1 = Teacher()
#     print(s1.greet())
#     s1.setGrade(9)
#     print(s1.getGrade())
#     print(t1.getName())
#     t1.setDegree('Master')
#     print(t1.getDegree())
#     print(t1.greet())
