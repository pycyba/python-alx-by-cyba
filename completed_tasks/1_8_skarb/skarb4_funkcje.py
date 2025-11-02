from random import randint, random

def odleglosc_do_skarbu():
    # Gdy funkcja ma tylko odczytać zmienne globalne, to nie musi ich deklarować jako global, i tak ma do nich dostęp.
    # Mimo, że nie jest to konieczne, zadeklarujemy te zmienne jako globalne dla zwiększenia czytelności.
    global skarb_x, skarb_y, gracz_x, gracz_y
    return abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)


def wylosuj_pozycje_gracza():
    global gracz_x, gracz_y
    gracz_x = randint(1, 10)
    gracz_y = randint(1, 10)


def wylosuj_pozycje_skarbu():
    # To nie jest najładnieszy styl programowania, ale w tym konkretnym przypadku tak będzie najwygodniej:
    # Funkcja modyfikuje zmienne globalne.
    # Jeśli funkcja ustawia lub modyfikuje zmienne globalne, muszą być wymienione w deklaracji global
    global skarb_x, skarb_y, odleglosc_na_poczatku, odleglosc_przed_ruchem, wykonana_liczba_ruchow

    skarb_x = randint(1, 10)
    skarb_y = randint(1, 10)
    #print(f'Pozycja skarbu: {skarb_x}, {skarb_y}')
    odleglosc_na_poczatku = odleglosc_do_skarbu()
    odleglosc_przed_ruchem = odleglosc_na_poczatku
    wykonana_liczba_ruchow = 0


# Początek programu
# W tej wersji również treść programu mieścimy w funkcji - zgodnie z konwencją nazwiemy ją main()
# Informacyjnie: W C, C++, Java, C# trzeba tak robić. W Pythonie nie trzeba, ale niektórzy tak robią.

def main():
    global skarb_x, skarb_y, gracz_x, gracz_y, odleglosc_na_poczatku, odleglosc_przed_ruchem, wykonana_liczba_ruchow

    wylosuj_pozycje_gracza()
    wylosuj_pozycje_skarbu()

    while (gracz_x, gracz_y) != (skarb_x, skarb_y):
        #print(f'Pozycja gracza:  {gracz_x}, {gracz_y}')

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

        wykonana_liczba_ruchow += 1
        if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
            print('Wypadłeś z planszy, porażka')
            break

        if wykonana_liczba_ruchow > 2*odleglosc_na_poczatku:
            print('Za długo szukasz, skarb został przeniesiony w inne miejsce')
            wylosuj_pozycje_skarbu()
        else:
            odleglosc_po_ruchu = odleglosc_do_skarbu()
            if random() > 0.2:  # z prawdopodobieństwem 4/5 wypisujemy wskazówkę
                if odleglosc_po_ruchu < odleglosc_przed_ruchem:
                    print('Zbliżyłeś się do skarbu')
                else:
                    print('Oddaliłeś się do skarbu')
            odleglosc_przed_ruchem = odleglosc_po_ruchu # odległość przed następnym ruchem jest róna odległości po tym ruchu
        print()
    else:
        # else do pętli wykona się tylko wtedy, gdy pętla zakońćzy się w sposó normalny
        # (w przypadku while: gdy warunek logiczny stanie się fałszywy)
        # a nie wykona się, gdy pętla zostanie przerwana za pomocą break
        print(f'Wygrałeś, brawo! Wykorzystałeś {wykonana_liczba_ruchow} ruchów.')
    print('papa')


# Aby funkcja main się wykonała, trzeba ją wywołać
main()
