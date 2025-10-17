# W tej wersji używamy funkcji `eval`, która ewaluuje dowolne wyrażenie podane przez użytkownika.
# Jest w tym pewne ryzyko, bo nie wiemy, co wpisze użytkownik.

def zapisz(x):
    with open('haha.txt', mode='a', encoding='utf-8') as plik:
        print(x, file=plik)
    return x


def main():
    print('Podawaj dowolne działania, które rozumie Python')
    print('Aby zakończyć, podaj pusty napis (naciśnij enter)')

    while True:
        linia = input(': ')
        if not linia: break
        try:
            wynik = eval(linia)
            print('wynik:', wynik)
        except Exception as e:
            print('Błąd:', e)

    print('Dziękujemy za skorzystanie z naszego programu.')


if __name__ == '__main__':
    main()
