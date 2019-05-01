from turtle import right, forward, left, shape, exitonclick
from math import sqrt
def domecek(strana, uhel):
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
    forward(50)
    left(90)
    for i in range(pocet_stran_ctverce):
        forward(strana)
        left(uhel)
        right(180)
    right(180-135)
    forward(sqrt(2)*strana)
    for i in range(strecha):
        left(uhel)
        forward(sqrt(2)*strana/2)
    left(90)
    forward(sqrt(2)*strana)
    left(45)
    forward(50)

strecha = 2
pocet_stran_ctverce = 4
domecek(100, 90)

exitonclick()
