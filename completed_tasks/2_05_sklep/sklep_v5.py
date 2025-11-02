# Względem wersji 4:
# * podział kodu na oddzielne funkcje
# * szerokość kolumny z nazwą dopasowana do max długości
# * możliwość podania alternatywnej nazwy pliku

menu = '''
 Q - zakończ program
 P - wypisz dostępne towary
 R - wczytaj dane z pliku
 W - zapisz dane do pliku
 K - wykonaj zakupy
 N - zdefiniuj nowy towar
 U - usuń towar z cennika
 C - zmień cenę towaru
 D - dostawa towaru'''

SEP = ';'
PLIK = 'towary.csv'

def wybor_z_menu():
    print(menu)
    return input('Wybierz polecenie: ').strip().upper()


def wypisz_towary(towary):
    width = max(len(nazwa) for nazwa in towary.keys()) if towary else 6
    print('Dostępne produkty:')
    print(f'| {"nazwa":{width}}|{" cena":6} |{" ilość":6} |')
    print('=' * (width + 18))
    for nazwa, (cena, ilosc) in towary.items():
        print(f'| {nazwa:{width}}|{cena:6} |{ilosc:6} |')


def wczytaj_plik():
    sciezka = zapytaj_o_plik()
    with open(sciezka, 'r') as plik:
        towary = {}
        ile = 0
        for linia in plik:
            nazwa, cena, ilosc = linia.strip().split(SEP)
            towary[nazwa] = [int(cena), int(ilosc)]
            ile += 1
        print(f'Wczytano dane {ile} towarów')
    return towary


def zapisz_plik(towary):
    sciezka = zapytaj_o_plik()
    with open(sciezka, 'w') as plik:
        ile = 0
        for nazwa, (cena, ilosc) in towary.items():
            print(nazwa, cena, ilosc, sep=SEP, file=plik)
            ile += 1
        print(f'Zapisano dane {ile} towarów')


def zapytaj_o_plik():
    sciezka = PLIK
    s = input(f'Podaj nazwę pliku lub naciśnij enter aby zatwierdzić domyślną ({sciezka}):')
    if s:
        sciezka = s
    return sciezka


def nowy_towar(towary):
    nazwa = input('Podaj nazwę nowego towaru: ')
    if nazwa in towary:
        print('Taki towar już istnieje, przerywam')
    else:
        cena = int(input('Podaj cenę towaru: '))
        towary[nazwa] = [cena, 0]


def usun_towar(towary):
    nazwa = input('Podaj nazwę istniejącego towaru: ')
    if nazwa not in towary:
        print('Taki towar nie istnieje, przerywam')
    else:
        del towary[nazwa]
        print('Towar usunięty')


def zmien_cene_towaru(towary):
    nazwa = input('Podaj nazwę istniejącego towaru: ')
    if nazwa not in towary:
        print('Taki towar nie istnieje, przerywam')
    else:
        print(f'Obecna cena: {towary[nazwa][0]}')
        cena = int(input('Podaj nową cenę towaru: '))
        towary[nazwa][0] = cena


def zakupy(towary):
    suma = 0
    while True:
        nazwa = input('Podaj nazwę towaru lub naciśnij Enter, aby zakończyć: ')
        if not nazwa:
            break
        if nazwa not in towary:
            print(f'Nieznany towar {nazwa}')
            continue
        sztuki = int(input('Ile sztuk? '))
        if sztuki > towary[nazwa][1]:
            print(f'Nie ma tylu sztuk towaru. Jest tylko {towary[nazwa][1]}.')
            continue
        do_zaplaty = towary[nazwa][0] * sztuki
        towary[nazwa][1] -= sztuki
        print(f'Za {sztuki} sztuk towaru {nazwa} do zapłaty będzie {do_zaplaty}')
        suma += do_zaplaty
    print(f'Łącznie za cały koszyk do zapłaty: {suma}')


def dostawa(towary):
    nazwa = input('Podaj nazwę istniejącego towaru: ')
    if nazwa not in towary:
        print('Taki towar nie istnieje, przerywam')
    else:
        print(f'Obecny stan magazynowy: {towary[nazwa][1]}')
        zmiana = int(input('Podaj liczbę sztuk w dostawie: '))
        towary[nazwa][1] += zmiana


def main():
    print('Witamy w naszym sklepie')
    towary = {}
    while True:
        akcja = wybor_z_menu()
        if akcja == 'Q':
            break
        elif akcja == 'P':
            wypisz_towary(towary)
        elif akcja == 'R':
            towary = wczytaj_plik()
        elif akcja == 'W':
            zapisz_plik(towary)
        elif akcja == 'K':
            zakupy(towary)
        elif akcja == 'N':
            nowy_towar(towary)
        elif akcja == 'C':
            zmien_cene_towaru(towary)
        elif akcja == 'U':
            usun_towar(towary)
        elif akcja == 'D':
            dostawa(towary)
        else:
            print('Nieznane polecenie')
    print('Do widzenia')


if __name__ == '__main__':
    main()
