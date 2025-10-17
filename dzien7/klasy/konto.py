class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, wł. {self._wlasciciel}, saldo {self._saldo}'

    def wplata(self, kwota):
        self._saldo += kwota

    def wyplata(self, kwota):
        self._saldo -= kwota

    def przelew(self, other, kwota):
        self._saldo -= kwota
        other._saldo += kwota
