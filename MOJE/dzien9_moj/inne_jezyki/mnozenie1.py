import sys

# najbardziej oczywisty zapis w Pythonie - wersja z tworzeniem tablic int

def mnoz_zakres(n):    
    t1 = list(range(n))
    t2 = list(range(n))
    suma = 0
    for e1 in t1:
        for e2 in t2:
            suma += e1 * e2
    return suma

if __name__ == '__main__':
    n = int(sys.argv[1])
    wynik = mnoz_zakres(n)
    print('Wynik:', wynik)

