from geometria import pole_kwadratu as pk, obwod_kwadratu as ok, pole_prostokata as pp, obwod_prostokata as op
from math import pi as liczba_pi
from random import randint as min, choice as max

#ERR print(geometria.pole_kwadratu(5))
#ERR print(pole_kwadratu(5))
print(pk(5))
print(ok(5))

print(pp(3, 4))
print(op(3, 4))

print(liczba_pi)
# pod nazwami min max mamy tak naprawdę funkcje z randoma
print(min(10, 20))
print(max(['red', 'green', 'blue']))
