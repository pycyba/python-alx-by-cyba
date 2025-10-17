"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to godziny powyżej 8 policz
jako nadgodziny (z podwójną stawką godzinową).
"""
class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0

    def register_time(self, czas):
        if czas > 8:
            self.suma_godzin += 8
            self.suma_nadgodzin += (czas - 8)
        else:
            self.suma_godzin += czas

    def pay_salary(self):
        try:
            return self.suma_godzin * self.stawka + self.suma_nadgodzin * 2 * self.stawka
        finally:
            self.suma_godzin = 0
            self.suma_nadgodzin = 0


# Przykładowy scenariusz:
def main():
    # Utworzenie obiektu - pracownik ze stawką godzinową 100
    employee = Employee('Jan', 'Nowak', 100.0)

    # Rejestrujemy czas pracy - pracownik przepracował 6 godzin
    employee.register_time(6)
    # Pracownik przepracował kolejne 4 godziny (ale innego dnia)
    employee.register_time(4)

    # Pobieramy wynagrodzenie za zarejestrowane godziny.
    # Metoda ma wzrócić (return) liczbę - kwotę wypłaty.
    # Tutaj za 10 godzin po 100 zł należy się 1000 zł wypłaty
    kasa = employee.pay_salary()
    print(kasa) # powinno być 1000

    # Gdyby teraz ponownie pobrać wypłatę, to powinno wyjść 0, bo "licznik się resetuje"
    kasa = employee.pay_salary()
    print(kasa) # powinno być 0

    # Jeśli jednak W JEDNEJ SESJI pracownik przepracuje > 8 godzin,
    # to za te nadmiarowe godziny należy się podwójna stawka
    employee.register_time(11)
    # 8 normalnch godzin + 3 nadgodziny
    # 8*100 + 3*2*100 = 1400
    kasa = employee.pay_salary()
    print(kasa) # powinno być 1400


if __name__ == '__main__':
    main()


# Testy jednostkowe PyTest
def test_zwykle_godziny():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(6)
    employee.register_time(4)
    kasa1 = employee.pay_salary()
    assert kasa1 == 1000
    kasa2 = employee.pay_salary()
    assert kasa2 == 0
    # w ortodoksyjnym podejściu do testów jednostkowych, fakt zerowania licznika powinien być sprawdzany w osobny teście
    # ale my to upraszczamy i robimy dwie asercje w jednym teście

def test_nadgodziny():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(11)
    employee.register_time(1)
    kasa1 = employee.pay_salary()
    assert kasa1 == 1500
    kasa2 = employee.pay_salary()
    assert kasa2 == 0

