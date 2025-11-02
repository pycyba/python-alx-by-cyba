from random import randint, random

# zamiast używać zmiennych globalnych, jak w poprzednich wersjach, ładniej będzie przechowywać stan gry wewnątrz obiektu (jako "atrybuty")
# wtedy metody (czyli "funkcje zdefiniowane wewnątrz klasy") będą miały dostęp do "atrybutów" poprzez specjalny parametr self.
class Gra:
    MIN = 1
    MAX = 10
    DEBUG = True

    def __init__(self):
        self.wylosuj_pozycje_skarbu()
        self.wylosuj_pozycje_gracza()

    def odleglosc_do_skarbu(self):
        return abs(self.gracz_x - self.skarb_x) + abs(self.gracz_y - self.skarb_y)

    def wylosuj_pozycje_gracza(self):
        self.gracz_x = randint(Gra.MIN, Gra.MAX)
        self.gracz_y = randint(Gra.MIN, Gra.MAX)

    def wylosuj_pozycje_skarbu(self):
        self.skarb_x = randint(Gra.MIN, Gra.MAX)
        self.skarb_y = randint(Gra.MIN, Gra.MAX)
        if Gra.DEBUG:
            print(f'Pozycja skarbu: {self.skarb_x}×{self.skarb_y}')
        self.odleglosc_na_poczatku = self.odleglosc_do_skarbu()
        self.wykonana_liczba_ruchow = 0

    def skarb_znaleziony(self):
        return (self.gracz_x, self.gracz_y) == (self.skarb_x, self.skarb_y)

    def poza_plansza(self):
        return self.gracz_x < Gra.MIN or self.gracz_x > Gra.MAX or self.gracz_y < Gra.MIN or self.gracz_y > Gra.MAX

    def wczytaj_ruch(self):
        ruch = input('Podaj ruch [wsad] lub [q] aby zakończyć: ').upper()
        return ruch

    def wykonaj_ruch(self, ruch):
        if Gra.DEBUG:
            print(f'Pozycja gracza: {self.gracz_x}×{self.gracz_y}')
        if ruch == 'W':
            self.gracz_y -= 1
        elif ruch == 'S':
            self.gracz_y += 1
        elif ruch == 'A':
            self.gracz_x -= 1
        elif ruch == 'D':
            self.gracz_x += 1
        self.wykonana_liczba_ruchow += 1

    def podpowiedz_albo_utrudnij(self, przed, po):
        if self.wykonana_liczba_ruchow > 2 * self.odleglosc_na_poczatku:
            print('Za długo szukasz, skarb został przeniesiony w inne miejsce')
            self.wylosuj_pozycje_skarbu()
        else:
            if random() > 0.2:  # z prawdopodobieństwem 4/5 wypisujemy wskazówkę
                if po < przed:
                    print('Zbliżyłeś się do skarbu')
                else:
                    print('Oddaliłeś się do skarbu')

    def graj(self):
        while not self.skarb_znaleziony():
            odleglosc_przed_ruchem = self.odleglosc_do_skarbu()
            ruch = self.wczytaj_ruch()
            if ruch == 'Q':
                print('Poddajesz się?')
                break
            elif ruch in 'WSAD':
                self.wykonaj_ruch(ruch)
            else:
                print('Nieprawidłowe polecenie')
                continue

            if self.poza_plansza():
                print('Wypadłeś z planszy, porażka')
                break

            odleglosc_po_ruchu = self.odleglosc_do_skarbu()
            self.podpowiedz_albo_utrudnij(odleglosc_przed_ruchem, odleglosc_po_ruchu)
            print()
        else:
            # else do pętli wykona się tylko wtedy, gdy pętla zakońćzy się w sposób normalny
            print(f'Wygrałeś, brawo! Wykorzystałeś {self.wykonana_liczba_ruchow} ruchów na minimalne {self.odleglosc_na_poczatku}.')
        print('papa')


if __name__ == '__main__':
    Gra().graj()
