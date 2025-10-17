def silnia(n):
    wynik = 1
    for i in range(2, n+1):
        wynik *= i
    return wynik


# funkcje testujące dałoby się wpisać w tym samym pliku, ale my wpiszemy w osobnym, bo tak jest "porządniej"
