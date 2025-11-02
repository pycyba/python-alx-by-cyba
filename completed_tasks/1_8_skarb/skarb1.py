from random import randrange

# losuje liczbę od 0 do 9
# Przyjmuję, że (0,0) to lewy górny róg planszy
skarb_x = randrange(0, 10)
skarb_y = randrange(0, 10)
gracz_x = randrange(0, 10)
gracz_y = randrange(0, 10)


print(f'Pozycja skarbu: {skarb_x}, {skarb_y}')

while True:
    print(f'Pozycja gracza:  {gracz_x}, {gracz_y}')
    odleglosc_przed_ruchem = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    ruch = input('Podaj ruch [wsad] lub [q] aby zakończyć: ').upper()
    if ruch == 'Q':
        print('Poddajesz się?')
        break
    elif ruch == 'W':
        gracz_y -= 1
    elif ruch == 'S':
        gracz_y += 1
    elif ruch == 'A':
        gracz_x -= 1
    elif ruch == 'D':
        gracz_x += 1
    else:
        print('Nieprawidłowe polecenie')
        continue

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('Wygrałeś, brawo!')
        break
    if gracz_x < 0 or gracz_x >= 10 or gracz_y < 0 or gracz_y >= 10:
        print('Wypadłeś z planszy, porażka')
        break

    odleglosc_po_ruchu = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    if odleglosc_po_ruchu < odleglosc_przed_ruchem:
        print('Zbliżyłeś się do skarbu')
    else:
        print('Oddaliłeś się do skarbu')
    print()


print('papa')
