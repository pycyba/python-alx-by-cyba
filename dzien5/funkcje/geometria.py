"""
To jest przykład modułu, a więc pliku, w którym są zdefiniowane funkcje (ew. klasy, ...
Inne pliki w projekcie będą korzystać z tego pliku za pomocą import.
"""
import math

def pole_kwadratu(a):
    return a*a

def obwod_kwadratu(a):
    return 4*a

def pole_prostokata(a, b):
    return a*b

def obwod_prostokata(a, b):
    return 2*a + 2*b

def pole_kola(r):
    return math.pi*r*r

def obwod_kola(r):
    return math.pi*2*r

def poprawny_trojkat(a, b, c):
    return a+b > c and b+c > a and c+a > b

def pole_trojkata(a, b, c):
    p = obwod_trojkata(a, b, c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def obwod_trojkata(a, b, c):
    return a+b+c



