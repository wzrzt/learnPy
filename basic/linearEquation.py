# -*- coding: utf-8 -*-
# -*- version: python3 -*-


class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getPerameters(self):
        return self.__a, self.__b, self.__c, self.__d, self.__e, self.__f

    def setPerameters(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def isSolvable(self):
        if (self.__a * self.__d - self.__b * self.__c) != 0:
            return 'true'
        else:
            return 'false'

    def getXY(self):
        if self.isSolvable() == 'true':
            x = (self.__e * self.__d - self.__b * self.__f)/(self.__a * self.__d - self.__b * self.__c)
            y = (self.__a * self.__f - self.__e * self.__c)/(self.__a * self.__d - self.__b * self.__c)
            return x, y

if __name__ == "__main__":
    nums = [0,0,0,0,0,0]
    nums[:] = eval(input("input the list called nums: "))
    a, b, c, d, e, f = nums[:]
    le1 = LinearEquation(a, b, c, d, e, f)
    print(le1.isSolvable())
    print(le1.getXY())

