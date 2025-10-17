"""
Użytkownik podaje liczbę wierzchołków (= boków)
a program rysuje wielokąt foremny o tej liczbie boków.
"""

import turtle

turtle.Screen().setup(width=900, height=900)

n = int(turtle.numinput('Pytanie', 'Podaj liczbę wierzchołków', 4, 2, 999))
zolw = turtle.Turtle()
zolw.color('red', 'yellow')
zolw.width(3)
obwod = 1200
bok = obwod / n
kat = 360 / n

zolw.penup()
zolw.goto(-bok/2, -obwod/6)
zolw.pendown()

zolw.begin_fill()
for _ in range(n):
    zolw.forward(bok)
    zolw.left(kat)
zolw.end_fill()

turtle.done()
