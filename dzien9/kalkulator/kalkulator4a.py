dzialania = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y,
    '^': lambda x, y: x ** y,
}

def main():
    print('Podawaj działania na zasadzie liczba1 + liczba2')
    print('Uwaga! Spacje są obowiązkowe!')
    print('Aby zakończyć, podaj pusty napis (naciśnij enter)')

    while True:
        linia = input(': ')
        if not linia: break
        try:
            liczba1, operacja, liczba2 = linia.split()
            x = float(liczba1)
            y = float(liczba2)
            f = dzialania[operacja]
            wynik = f(x, y)
            print('wynik:', wynik)
        except KeyError:
            print('Nieznana operacja')
        except Exception as e:
            print('Błąd:', e)

    print('Dziękujemy za skorzystanie z naszego programu.')


if __name__ == '__main__':
    main()
