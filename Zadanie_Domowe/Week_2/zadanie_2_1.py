def suma_cyf(n):
    suma = 0
    for ch in str(n):
        suma += int(ch)
    return suma
    # alternatywnie: return sum(int(ch) for ch in str(n))

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    elif liczba == 2:
        return True
    elif liczba % 2 == 0:
        return False
    else:
        for i in range(3, int(liczba**0.5) + 1, 2): # Pierwiastek skraca nam range, i zrobi to szybciej komptuer.
            if liczba % i == 0:
                return False
        return True


def fib(n):
    if n == 0:return 0
    elif n == 1:return 1
    else:
        return fib(n-2) + fib(n-1)

def test_suma_cyf():
    assert suma_cyf(1023) == 6
    assert suma_cyf(0) == 0
    assert suma_cyf(9999) == 36

def test_czy_pierwsza():
    assert czy_pierwsza(2) is True
    assert czy_pierwsza(13) is True
    assert czy_pierwsza(15) is False
    assert czy_pierwsza(1) is False
    assert czy_pierwsza(2147483647) is True  # duża pierwsza (Mersenne 2^31-1)

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(10) == 55

