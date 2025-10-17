from klasa_czas_pracy import CzasPracy


class PremiumEmployee(CzasPracy):
    def __init__(self, imie, nazwisko, stawka):
        # Wywołaj konstruktor klasy bazowej, żeby zainicjalizować
        # imię, nazwisko, stawkę i liczniki godzin
        super().__init__(imie, nazwisko, stawka)
        # Dodaj nowe pole dla bonusów
        self._bonus = 0.0

    def give_bonus(self, kwota):
        """Przyznaj bonus pracownikowi"""
        kwota = float(kwota)
        if kwota <= 0:
            raise ValueError("Bonus musi być dodatni")
        self._bonus += kwota

    def pay_salary(self):
        """Wypłać pensję: godziny + bonusy, potem wyzeruj wszystko"""
        # Wywołaj oryginalną metodę z klasy bazowej
        # (liczy pensję za godziny i zeruje liczniki godzin)
        pensja_za_godziny = super().pay_salary()

        # Dodaj zgromadzone bonusy
        calkowita_wyplata = pensja_za_godziny + self._bonus

        # Wyzeruj bonusy po wypłacie
        self._bonus = 0.0

        return calkowita_wyplata

    def __str__(self):
        """Opcjonalnie: ładniejszy wydruk"""
        return f"Premium: {self.Imie} {self.Nazwisko} @ {self.stawka:.2f} (bonus: {self._bonus:.2f})"