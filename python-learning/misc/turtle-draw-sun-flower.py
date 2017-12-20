# coding=utf-8
import turtle
import time

turtle.color('red','yellow')

turtle.begin_fill()
for _ in range(50):
    turtle.forward(300)
    turtle.left(170)
    turtle.end_fill()

turtle.mainloop()