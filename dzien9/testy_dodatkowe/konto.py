# W tym pliku najpierw zdefiniujemy klasę Konto, a poniżej dodamy testy tej klasy

class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def __str__(self):
        return f'Konto nr {self.numer}, wł. {self.wlasciciel}, saldo {self.saldo}'

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        self.saldo -= kwota

#####################
# testy:

def test_tworzenie_konta():
    konto = Konto(1, 'Ala', 1000)
    assert konto.numer == 1
    assert konto.wlasciciel == 'Ala'
    assert konto.saldo == 1000

def test_zero():
    konto = Konto(1, 'Ala')
    assert konto.numer == 1
    assert konto.wlasciciel == 'Ala'
    assert konto.saldo == 0

def test_str():
    konto = Konto(1, 'Ala', 1000)
    s = str(konto)
    assert s == 'Konto nr 1, wł. Ala, saldo 1000'

def test_wplata():
    konto = Konto(1, 'Ala', 1000)
    konto.wplata(300)
    assert konto.saldo == 1300

def test_wyplata():
    konto = Konto(1, 'Ala', 1000)
    konto.wyplata(400)
    assert konto.saldo == 600
