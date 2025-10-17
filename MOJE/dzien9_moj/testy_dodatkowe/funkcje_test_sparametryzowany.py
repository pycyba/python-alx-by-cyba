# Testy funkcji silnia w formie testu sparametryzowanego

from funkcje import *
import pytest

@pytest.mark.parametrize('argument,wynik', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
])
def test_silnia(argument, wynik):
    assert silnia(argument) == wynik

