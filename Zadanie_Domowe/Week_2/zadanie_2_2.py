def statystyka(lista):
    ilosc_elementow = 0
    suma = 0

    # inicjalizacja min/max pierwszym elementem
    minimalna_wartosc = lista[0]
    maksymalna_wartosc = lista[0]

    for x in lista:
        ilosc_elementow += 1
        suma += x

        if x < minimalna_wartosc:
            minimalna_wartosc = x
        if x > maksymalna_wartosc:
            maksymalna_wartosc = x

    srednia_arytmetyczna = suma / ilosc_elementow
    return (ilosc_elementow, suma, srednia_arytmetyczna, minimalna_wartosc, maksymalna_wartosc)

def test_statystyka():

    n = [2, 5, 2, 3, 5]
    assert statystyka(n) == (5, 17, 3.4, 2, 5)

    m = [-5, -2, -3]
    assert statystyka(m) == (3, -10, -10/3, -5, -2)
