# Przykład tesu sparametryzowanego w PyTest
# Podajemy listę (zestawów parametrów), które zostaną przekazane do tej samej funkcji.
# Tutaj są to: stawka, lista rejestrowanych godzin i oczekiwany wynik (wypłata).

from klasa_pracownik import Pracownik
import pytest

@pytest.mark.parametrize('stawka,lista_godzin,wynik', [
    (100, [], 0),
    (100, [5], 500),
    (200, [5], 1000),
    (0, [5], 0),
    (100, [6, 4, 2], 1200),
    (100, [10], 1200),
    (100, [10, 5], 1700),
])
def test_employee(stawka, lista_godzin, wynik):
    emp = Pracownik('X', 'Y', stawka)

    # naliczam godziny zgodnie z listą
    for godziny in lista_godzin:
        emp.register_time(godziny)

    # pierwsza wyplata - ma wyjść oczekiwany wynik
    assert wynik == emp.pay_salary()

    # druga wyplata - ma wyjść zero
    assert 0 == emp.pay_salary()
