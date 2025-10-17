
##################
# ten sam styl:
# from decimal import Decimal
# from turtle import Turtle
# from datetime import datetime

from konto import Konto

konto1 = Konto(1, 'Ala', 1000)
print(konto1.__dict__)
print(konto1)

# zadanie:
# uzupełnij definicję klasy tak, aby zadziałały poniższe wywłania metod
# efektem ma być zmiana salda
konto1.wplata(300)
print(konto1)
konto1.wyplata(400)
print(konto1)
# metodę można wywołać z poziomu klasy:
Konto.wplata(konto1, 1000)
print(konto1)
print()

konto2 = Konto(2, 'Ola')
print(konto1, konto2)
konto1.przelew(konto2, 800)
print(konto1, konto2)
