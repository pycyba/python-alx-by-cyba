from funkcje_na_listach import *

def test_suma():
    wynik = suma([5, 10, 15])
    assert wynik ==30

def test_suma_parzystyk():
    wynik = suma_parzystych([5, 10, 20, 15])
    assert wynik ==30

def test_drugi_najwieksz():
    wynik = drugi_najwieksz([5, 10, 20, 15,16, ])
    assert wynik == 16

def test_drugi_najwiekszy():
    wynik = drugi_najwiekszy([5, 10, 20,20, 15,16,16,16 ])
    assert wynik == 16
