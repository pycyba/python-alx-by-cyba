def oblicz(liczba1, liczba2, operacja):
    '''Funkcja oblicza podane działanie i zwraca wynik jako liczbę.
        W przypadku nieznanej operacji wyrzuca wyjątek ValueError.'''
    match operacja:
        case '+': return liczba1 + liczba2
        case '-': return liczba1 - liczba2
        case '*': return liczba1 * liczba2
        case '/': return liczba1 / liczba2
        case '%': return liczba1 % liczba2
        case '^': return liczba1 ** liczba2
        case _: raise ValueError(f'Nieznana operacja {operacja}')


print('Podawaj działania na zasadzie liczba1 + liczba2')
print('Uwaga! Spacje są obowiązkowe!')
print('Aby zakończyć, podaj pusty napis (naciśnij enter)')

while True:
    linia = input(': ')
    if not linia: break
    liczba1, operacja, liczba2 = linia.split()
    # teraz liczba1 i liczba2 są typu str; musimy zamienić na liczby
    liczba1 = float(liczba1)
    liczba2 = float(liczba2)
    wynik = oblicz(liczba1, liczba2, operacja)
    print('wynik:', wynik)

print('Dziękujemy za skorzystanie z naszego programu.')
