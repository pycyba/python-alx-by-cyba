from klasa_employee_v2 import Employee

# Ta wersja PremiumEmployee jest krótsza, ale działa tylko dla pewnej konkretnej wersji klasy Employee
# Takiej wersji, w której zarobione pieniądze dodajemy od razu do atrybutu `kasa`.
class PremiumEmployee(Employee):
    def give_bonus(self, bonus):
        self.kasa += bonus


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

