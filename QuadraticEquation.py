# -*- coding: utf-8 -*-
# -*- version: python3 -*-
import math

class QuadraticEquation:
#  这是一个二次方程, 形式为 a * x^2 + b * x + c = 0
    def __init__(self, a=1.0, b=1.0, c=0.0):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDescriminant(self):
        print("b^2 - 4 * a * c = %s" % (self.__b ** 2 - 4 * self.__a * self.__c))

    def getRoot(self):
        if (self.__b ** 2 - 4 * self.__a * self.__c) >= 0:
            print((0 - self.__b - math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c))/(2 * self.__a),
                  (0 - self.__b + math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c))/(2 * self.__a))
        else:
            return "The Equation has none roots"

if __name__ == "__main__":
    a,b,c = eval(input("Type in 3 numbers: "))
    equation1 = QuadraticEquation(a=a, b=b, c=c)
    equation1.getDescriminant()
    equation1.getRoot()