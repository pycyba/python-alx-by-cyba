def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik



while True:
    arg = int(input('Podaj argument: '))
    if arg < 0: break
    wynik = silnia(arg)
    print(wynik)