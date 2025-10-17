import geometria
from geometria import *

menu = """Wybierz figure:
K - Kwadrat
P - Prostokąt
O - Koło
Q - Koniec programu 
"""

while True:
    wybor = input(menu)

    match wybor:
        case 'Q':break
        case 'K':
            a = float(input("Podaj długość boku: "))
            pole = pole_kwadratu(a)
            obwod = obwod_kwadratu(a)
            print(f"Pole {pole}, obwod: {obwod}")
        case 'P':
            a, b = map(float, input("Podaj 3 liczby: ").split())
            pole = pole_prostokata(a, b)
            obwod = obwod_prostokata(a, b)
            print(f"Pole {pole}, obwod: {obwod}")
        case 'O':
            r = float(input("Podaj r"))
            pole = pole_kola(r)
            obwod = obwod_kola(r)
            print(f"Pole {pole}, obwod: {obwod}")



