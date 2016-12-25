# -*- coding: utf-8 -*-
# -*- version: python3 -*-
import turtle
import math
import os

turtle.penup()
turtle.goto(-175,0)
turtle.pendown()
turtle.goto(175,0)
turtle.penup()
turtle.goto(0, - 50)
turtle.pendown()
turtle.goto(0, 50)
turtle.penup()
turtle.goto(-175, 50 * math.sin((-175 / 100) * 2 * math.pi))
turtle.pendown()
turtle.circle(1)
turtle.penup()
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("-2\u03c0")
turtle.penup()
turtle.hideturtle()
os.system('pause')
