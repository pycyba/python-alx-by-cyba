import random

x = random.randint(1, 100)
y = random.randint(1, 100)

print(f'Wylosowane liczby: x = {x} , y = {y}')
print('Wynik porównania:', x < y)
print()

# Najbardziej typowy zapis if - if z else
# Jeśli warunek jest prawdziwy, wykona się jeden zestaw instrukcji,
# a jeśli nieprawdziwy, to drugi zestaw.
# Za if i za else wpisuje się "bloki kodu", czyli linie z wcięciem - standardowo 4 spacje
if x < 50:
    print('x jest mały')
    print('bo x jest równy tylko', x)
else:
    print('x jest duży')

# Gdy wrócimy na poprzedni poziom wcięcia, to znaczy, że kończymy bloki if / else
# i to co dalej wykona się zawsze
print('a kuku!')
print()

# Jeśli rozważamy więcej niż 2 sytuacje, możemy użyć konstrukcji
# if / elif / ... / else
# sekcji elif może być dużo
# działanie: Python wykona pierwszy blok (tylko jeden), dla którego warunek jest prawdziwy
# jeśli wszystkie warunki są fałszywe - wtedy else (o ile istnieje)
if x < y:
    print('x jest mniejsze od y')
elif x > y:
    print('x jest większe od y')
else:
    print('x i y są sobie równe')
print()

# Sekcję else można pominąć - wtedy w przypadku nieprawdziwości warunku nie wykona się nic
# (ale program idzie dalej)

if x % 2 == 0:
    print('x jest parzysty')

print('a kuku')
print()

# operatory porównania: == != > >= < <=

# W Pythonie istnieje unikalny sposób porównywania łączonego
# Jako pojedynczy warunek można zapisać ciąg porównań, który logicznie jest traktowany jak koniunkcja:
if 10 < x < 20:
    print('x jest rzędu "naście"')

if 10 <= x <= y <= 50:
    print('prawda: 10 <= x <= y <= 50')
else:
    print('nieprawda')
print()

# Spójniki logiczne pisane slownie: and, or, not
if x < 50 and y < 50:
    print('and jest prawdą')
    print('Obie liczby są mniejsze od 50')
else:
    print('and jest nieprawdą')
    print('Co najmniej jedna z liczb jest >= 50')
print()

if x < 50 or y < 50:
    print('or jest prawdą')
    print('Co najmniej jedna z liczb jest mniejsza od 50')
else:
    print('or jest nieprawdą')
    print('Żadna z liczb nie jest mniejsza od 50')

# Uwaga: operatory pisane za pomocą znaczków & | ^ w Pythonie też istnieją,
# ale działają w inny sposób i do zastosowań logicznych zdecydowanie lepiej używać `and` i `or`

# Dla wielu typów jest określone automatyczne rzutowanie na wartość logiczną
# dla liczb 0 oznacza fałsz, a inna wartość prawdę
# dla napisów, list i innych kolekcji puste jest traktowane jak fałsz, a niepuste jak prawda
napis1 = ''
napis2 = ' '
if napis1: print("napis1 prawda")
else: print("napis1 fałsz")
if napis2: print("napis2 prawda")
else: print("napis2 fałsz")

if 'False': print("napis3 prawda")
else: print("napis3 fałsz")
