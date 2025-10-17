"""
Program na podstawie wieku przypisuje osobę do jednej z kategorii.
0-3 - niemowlak
4-6 - przedszkole
7-17 - szkoła
18-64 - dorosły
65+ - emeryt
"""

wiek = int(input('Podaj wiek: '))
if 0 <= wiek <= 3:
    print('niemowlak')
elif 4 <= wiek <= 6:
    print('przedszkole')
elif 7 <= wiek <= 17:
    print('szkoła')
elif 18 <= wiek <= 64:
    print('dorosły')
elif wiek >= 65:
    print('emeryt')
else:
    print('niepoprawny wiek')
