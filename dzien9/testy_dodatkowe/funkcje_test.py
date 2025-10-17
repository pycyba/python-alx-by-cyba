from funkcje import *

# Testy funkcji silnia:
def test_silnia_5():
    wynik = silnia(5)
    assert wynik == 120

def test_silnia_0():
    assert silnia(0) == 1


# Gdybyśmy nie mieli frameworku do testowania, moglibyśmy wywołać sobie te funkcje
# test_silnia_0()
# test_silnia_5()

# W praktyce takie funkcje/metody testujące są uruchamiane automatycznie za pomocą jednego z frameworków do uruchamiania testów jednostkowych.
# My użyjemy biblioteki pytest

# pytest uruchamia wszystkie funkcje, których nazwy rozpoczynają się od "test"
# i sprawdza, czy kończą się normalnie (sukces), czy wyjątkiem (porażka)

# Asercje służą do sprawdzania warunków logicznych i działają tak,
# jeśli warunek jest spełniony, to nic się nie dzieje,
# jeśli warunek niespełniony, to wyrzucany jest wyjątek AssertionError
