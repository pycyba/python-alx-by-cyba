class CzasPracy:
    def __init__(self, imie, nazwisko, stawka):
        self.Imie = imie
        self.Nazwisko = nazwisko
        self.stawka = float(stawka)
        self.regular_time = 0.0
        self.ovr_time = 0.0

    def register_time(self, czas):
        czas = float(czas)
        if czas <= 0:
            raise ValueError("Czas musi być dodatni")
        if czas > 8:
            self.regular_time += 8
            self.ovr_time += (czas - 8)
        else:
            self.regular_time += czas

    def pay_salary(self):
        kwota = self.stawka * self.regular_time + 2 * self.stawka * self.ovr_time
        self.regular_time = 0.0
        self.ovr_time = 0.0
        return float(kwota)

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko} {self.stawka}"