from SubPerson import Student
from SubPerson import Teacher
s1 = Student()
t1 = Teacher()
print(s1.greet())
s1.setGrade(9)
print(s1.getGrade())
print(t1.getName())
t1.setDegree('Master')
print(t1.getDegree())
t1.greet()