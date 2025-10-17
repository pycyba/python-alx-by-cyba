import sys

# wersja bez tworzenia tablic

def mnoz_zakres(n):
    return sum(e1 * e2 for e1 in range(n) for e2 in range(n))

if __name__ == '__main__':
    n = int(sys.argv[1])
    wynik = mnoz_zakres(n)
    print('Wynik:', wynik)
