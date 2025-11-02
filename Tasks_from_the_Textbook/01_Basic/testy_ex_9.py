from ex_9 import sprawdz_pelnoletnosc


def test_pelnoletni_granica():
    """Osoba urodzona dokładnie 18 lat temu jest pełnoletnia."""
    assert sprawdz_pelnoletnosc(2007, rok_obecny=2025) == True


def test_pelnoletni_starszy():
    """Osoba starsza niż 18 lat jest pełnoletnia."""
    assert sprawdz_pelnoletnosc(1980, rok_obecny=2025) == True


def test_niepelnoletni():
    """Osoba młodsza niż 18 lat nie jest pełnoletnia."""
    assert sprawdz_pelnoletnosc(2010, rok_obecny=2025) == False


def test_niepelnoletni_granica():
    """Osoba urodzona 17 lat temu nie jest pełnoletnia."""
    assert sprawdz_pelnoletnosc(2008, rok_obecny=2025) == False


def test_rok_przyszly():
    """Osoba 'urodzona w przyszłości' nie jest pełnoletnia."""
    assert sprawdz_pelnoletnosc(2030, rok_obecny=2025) == False


def test_wiek_zero():
    """Osoba urodzona w bieżącym roku nie jest pełnoletnia."""
    assert sprawdz_pelnoletnosc(2025, rok_obecny=2025) == False