from random import randint, random

skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

# Losujemy pozycję gracza tak, żeby nie pokrywała się z pozycją skarbu (losowanie do skutku)
gracz_x = skarb_x
gracz_y = skarb_y # takie ustawienie początkowych wartości, aby program wszedł do tej pętli choć jeden raz
while gracz_x == skarb_x and gracz_y == skarb_y:
    gracz_x = randint(1, 10)
    gracz_y = randint(1, 10)

# Przyjmuję, że (1,1) to lewy górny róg planszy

print(f'Pozycja skarbu: {skarb_x}, {skarb_y}')
odleglosc_na_poczatku = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
odleglosc_przed_ruchem = odleglosc_na_poczatku
wykonana_liczba_ruchow = 0

while True:
    print(f'Pozycja gracza:  {gracz_x}, {gracz_y}')

    ruch = input('Podaj ruch [wsad] lub [q] aby zakończyć: ').upper()
    match ruch:
        case 'Q':
            print('Poddajesz się?')
            break
        case 'W':
            gracz_y -= 1
        case 'S':
            gracz_y += 1
        case 'A':
            gracz_x -= 1
        case 'D':
            gracz_x += 1
        case _:
            print('Nieprawidłowe polecenie')
            continue

    wykonana_liczba_ruchow += 1
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f'Wygrałeś, brawo! Wykorzystałeś {wykonana_liczba_ruchow} ruchów.')
        break
    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print('Wypadłeś z planszy, porażka')
        break

    if wykonana_liczba_ruchow > 2*odleglosc_na_poczatku:
        # od nowa losujemy pozycję skarbu
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        print('Za długo szukasz, skarb został przeniesiony w inne miejsce')
        print(f'Pozycja skarbu: {skarb_x}, {skarb_y}')
        odleglosc_na_poczatku = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        odleglosc_przed_ruchem = odleglosc_na_poczatku
        wykonana_liczba_ruchow = 0
    else:
        odleglosc_po_ruchu = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        if random() >= 0.2:  # z prawdopodobieństwem 4/5 wypisujemy wskazówkę
            if odleglosc_po_ruchu < odleglosc_przed_ruchem:
                print('Zbliżyłeś się do skarbu')
            else:
                print('Oddaliłeś się do skarbu')
        odleglosc_przed_ruchem = odleglosc_po_ruchu # odległość przed następnym ruchem jest równa odległości po tym ruchu
    print()

print('papa')
