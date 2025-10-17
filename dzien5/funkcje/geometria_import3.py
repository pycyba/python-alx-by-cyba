from geometria import pole_kwadratu, obwod_kwadratu, pole_prostokata, obwod_prostokata
from math import pi
from random import randint, choice

print(pole_kwadratu(5))
print(obwod_kwadratu(5))

print(pole_prostokata(3, 4))
print(obwod_prostokata(3, 4))

# błędne wywołania:
# print(geometria.pole_kwadratu(5))
# print(geometria.pole_kola(5))
# print(pole_kola(4))

print(pi)
print(randint(10, 20))
print(choice(['red', 'green', 'blue']))
