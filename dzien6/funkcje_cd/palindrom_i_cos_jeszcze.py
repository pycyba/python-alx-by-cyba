# ewentualne rozszerzenie możliwości palindromu:
# dodatkowy parametr normalizuj=Fasle
# gdy ustawi się wartość True, to dodatkowo:
# - nie bierze pod uwagę wielkości liter
# - nie bierze pod uwagę spacji
# palindrom('Kobyła ma mały bok', True)   → True
# palindrom('Kobyła ma mały bok')   → False
# palindrom('kajak')   → True

def palindrom_petla(napis, normalizuj=False):
    if normalizuj:
        napis = napis.casefold().replace(' ', '')
    lewy = 0
    prawy = len(napis)
    while lewy < prawy:
        prawy -= 1
        if napis[lewy] != napis[prawy]:
            return False
        lewy += 1
    return True

def palindrom(napis, normalizuj=False):
    if normalizuj:
        napis = napis.casefold().replace(' ', '')
    return napis == napis[::-1]

    # gdyby myśleć o wydajności, to ew. coś w tym kierunku:
    # polowa = len(napis)//2
    # return napis[:polowa] == napis[:polowa:-1]


def ile_samoglosek(napis):
    """Zwraca liczbę liter będących samogłoskami w tym napisie"""
    samogloski = set('aeiouyąęó')
    wynik = 0
    for z in napis.lower():
        if z in samogloski:
            wynik += 1
    return wynik


def ile_samoglosek_comprehension(napis):
    return sum(1 for z in napis.lower() if z in 'aeiouyąęó')


def main():
    while True:
        napis = input('Podaj napis: ')
        if not napis:
            break

        print('Uwzględniając spacje i wielkość liter ', end='')
        if palindrom(napis):
            print('to JEST palindrom')
        else:
            print('to NIE jest palindrom')
        print('Ignorując spacje i wielkość liter ', end='')
        if palindrom(napis, True):
            print('to JEST palindrom')
        else:
            print('to NIE jest palindrom')
        print('palindorm_petla:', palindrom_petla(napis))
        print('palindorm_petla norm:', palindrom_petla(napis, True))

        print('Liczba samogłosek w tekście:', ile_samoglosek(napis))
        print('Liczba samogłosek w tekście wersja c:', ile_samoglosek_comprehension(napis))


if __name__ == '__main__':
    main()
