from funkcje_na_listach import *

def test_suma():
    wynik = suma([5, 10, 15])
    assert wynik == 30

def test_suma_pusta():
    wynik = suma([])
    assert wynik == 0


def test_suma_parzystych_1():
    wynik = suma_parzystych([1, 3, 7, 4, 6, 99, 10])
    assert wynik == 20

def test_suma_parzystych_2():
    wynik = suma_parzystych([1, 3, 7, 5, 99, 11])
    assert wynik == 0

def test_suma_parzystych_3():
    wynik = suma_parzystych([])
    assert wynik == 0


def test_drugi_najwiekszy():
    wynik = drugi_najwiekszy([22, 33, 11, 44])
    assert wynik == 33


def test_drugi_najwiekszy_duplikaty():
    wynik = drugi_najwiekszy([22, 33, 44, 33, 11, 44])
    assert wynik == 33

def test_drugi_najwiekszy_pusty():
    wynik = drugi_najwiekszy([])
    assert wynik == None

def test_drugi_najwiekszy_jednakowe():
    wynik = drugi_najwiekszy([22, 22, 22])
    assert wynik == None

def test_drugi_najwiekszy_inne():
    wynik = drugi_najwiekszy(range(20, 30, 2))
    assert wynik == 26

def test_drugi_najwiekszy_inne2():
    wynik = drugi_najwiekszy({'Ala', 'Ola', 'Ula', 'Ela'})
    assert wynik == 'Ola'
