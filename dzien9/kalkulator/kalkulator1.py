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
    match operacja:
        case '+': print(liczba1 + liczba2)
        case '-': print(liczba1 - liczba2)
        case '*': print(liczba1 * liczba2)
        case '/': print(liczba1 / liczba2)
        case '%': print(liczba1 % liczba2)
        case '^': print(liczba1 ** liczba2)
        case _ : print('Nieznana operacja')

print('Dziękujemy za skorzystanie z naszego programu.')
