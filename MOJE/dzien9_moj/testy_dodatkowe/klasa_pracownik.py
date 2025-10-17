class Pracownik:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0

    def register_time(self, godziny):
        if godziny <= 8:
            self.suma_godzin += godziny
        else:
            self.suma_nadgodzin += godziny - 8
            self.suma_godzin += 8

    def pay_salary(self):
        do_zaplaty = self.suma_godzin * self.stawka + self.suma_nadgodzin * self.stawka * 2
        self.suma_godzin = 0
        self.suma_nadgodzin = 0
        return do_zaplaty

class PremiumPracownik(Pracownik):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        do_zaplaty = super().pay_salary() + self.bonus
        self.bonus = 0
        return do_zaplaty