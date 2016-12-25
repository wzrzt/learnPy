# encoding=utf-8*
'''
@author=wei_rain
'''

'''
一个Person类，
    属性包括:年龄，姓名，身高，性别；
    要求属性不能直接通过对象.属性名的方式访问，必须提供 set／get 方法获取每个属性。

'''


class Person:
    def __init__(self, age=24, name='Jack', height=1.75, gender='male'):

        self.__age = age
        self.__name = name
        self.__height = height
        self.__gender = gender

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def getHeight(self):
        return self.__height

    def getGender(self):
        return self.__gender

    def setHeight(self, height):
        self.height = height

