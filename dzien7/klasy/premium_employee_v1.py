from klasa_employee_v1 import Employee

# Ta wersja PremiumEmployee działa poprawnie niezależnie od tego, której wersji Employee użyjemy jako podstawy.
# Wystarczy tylko, żeby w Employee poprawnie działała metoda pay_salary - ale nieważne jak jest zaimplementowana.

class PremiumEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        try:
            return super().pay_salary() + self.bonus
        finally:
            self.bonus = 0



def test_premium():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(6)  #  600
    employee.register_time(10) # 1200
    employee.give_bonus(700)   #  700
    employee.register_time(4)  #  400
    employee.give_bonus(100)   #  100
    kasa1 = employee.pay_salary()
    assert kasa1 == 3000
    kasa2 = employee.pay_salary()
    assert kasa2 == 0

