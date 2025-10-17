def rownanie_kwadratowe(a, b, c):
    """
    Funkcja rozwiązuje równanie kwadratowe ax²+bx+c=0
    Zwraca listę rozwiązań: 0, 1, lub 2 wartości x, dla których równanie jest spełnione.
    """
    if a == 0:
        raise ValueError('Współczynnik a równy zero - to nie jest równanie kwadratowe!')
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return [x1, x2]
    elif delta == 0:
        x = (-b) / (2*a)
        return [x]
    else:
        return []


def main():
    print('Podawaj po trzy współczynniki równania kwadratowego rozdzielone spacjami, a ja rozwiążę to równanie.')
    print('Aby zakończyć, naciśnij enter bez wprowadzania liczb.')
    while True:
        try:
            linia = input('> ').strip()
            if not linia: break
            a, b, c = map(float, linia.split())
            wyniki = rownanie_kwadratowe(a, b, c)
            match len(wyniki):
                case 0: print(f'Równanie nie ma żadnego rozwiązania.')
                case 1: print(f'Równanie ma jedno rozwiązanie: {wyniki[0]}.')
                case 2: print(f'Równanie ma dwa rozwiązania: {wyniki[0]}, {wyniki[1]}.')
        except Exception as e:
            print('Błąd:', e)



if __name__ == '__main__':
    main()
