def oblicz(liczba1: float, liczba2: float, operacja: str) -> float:
    '''Funkcja oblicza podane działanie i zwraca wynik jako liczbę.
        W przypadku nieznanej operacji wyrzuca wyjątek ValueError.
        Może też zgłaszać inne wyjątki, jak dzielenie przez zero itp.'''
    match operacja:
        case '+': return liczba1 + liczba2
        case '-': return liczba1 - liczba2
        case '*': return liczba1 * liczba2
        case '/': return liczba1 / liczba2
        case '%': return liczba1 % liczba2
        case '^': return liczba1 ** liczba2
        case _: raise ValueError(f'Nieznana operacja {operacja}')


def main():
    print('Podawaj działania na zasadzie liczba1 + liczba2')
    print('Uwaga! Spacje są obowiązkowe!')
    print('Aby zakończyć, podaj pusty napis (naciśnij enter)')

    while True:
        linia = input(': ')
        if not linia: break
        try:
            liczba1, operacja, liczba2 = linia.split()
            # teraz liczba1 i liczba2 są typu str; musimy zamienić na liczby
            liczba1 = float(liczba1)
            liczba2 = float(liczba2)
            wynik = oblicz(liczba1, liczba2, operacja)
            print('wynik:', wynik)
        except Exception as e:
            print('Błąd:', e)

    print('Dziękujemy za skorzystanie z naszego programu.')


if __name__ == '__main__':
    main()
