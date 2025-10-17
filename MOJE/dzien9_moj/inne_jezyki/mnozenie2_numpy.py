import sys
import numpy

# wersja z użyciem biblioteki numpy
# Gdy użyjemy tej biblioteki, będą używane "natywne" liczby, podobnie jak w C i Javie

def mnoz_zakres(n):
    t1 = numpy.arange(n, dtype=numpy.int64).reshape(1, n)
    t2 = numpy.arange(n, dtype=numpy.int64).reshape(n, 1)
    return (t2 @ t1).sum()

if __name__ == '__main__':
    n = int(sys.argv[1])
    # n = 10000
    wynik = mnoz_zakres(n)
    print('Wynik:', wynik)

