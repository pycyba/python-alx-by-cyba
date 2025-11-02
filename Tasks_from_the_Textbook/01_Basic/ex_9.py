def sprawdz_pelnoletnosc(rok_urodzenia: int, rok_obecny: int = 2025) -> bool:
    """
    Sprawdza, czy osoba jest pełnoletnia (>= 18 lat).

    Args:
        rok_urodzenia: rok urodzenia osoby
        rok_obecny: rok, względem którego sprawdzamy (domyślnie 2025)

    Returns:
        True jeśli osoba ma >= 18 lat, False w przeciwnym razie
    """
    wiek = rok_obecny - rok_urodzenia
    return wiek >= 18


def main():
    """Interaktywna wersja programu."""
    try:
        rok = int(input("Podaj rok urodzenia: "))
        if sprawdz_pelnoletnosc(rok):
            print("Jesteś pełnoletni!")
        else:
            print("Nie jesteś pełnoletni.")
    except ValueError:
        print("Błąd: podaj poprawny rok (liczba całkowita).")


if __name__ == '__main__':
    main()