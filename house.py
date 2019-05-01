from turtle import right, forward, left, shape, exitonclick, penup, pendown
from math import sqrt

def domecek(strana):
    uhel = 90
    strecha = 2
    pocet_stran_ctverce = 4
    for i in range(pocet_stran_ctverce):
        left(uhel)
        forward(strana)
        right(180)
    left(180-135)
    forward(sqrt(2)*strana)
    for i in range(strecha):
        left(uhel)
        forward(sqrt(2)*strana/2)
    left(90)
    forward(sqrt(2)*strana)
    left(45)

domecek(50)

exitonclick()
