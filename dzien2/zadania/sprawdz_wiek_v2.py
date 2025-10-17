"""
Program na podstawie wieku przypisuje osobę do jednej z kategorii.
0-3 - niemowlak
4-6 - przedszkole
7-17 - szkoła
18-64 - dorosły
65+ - emeryt
"""

wiek = int(input('Podaj wiek: '))

if wiek < 0:
    print('nieporpawny wiek')
elif wiek <= 3:
    print('niemowlak')
elif wiek <= 6:
    print('przedszkole')
elif wiek <= 17:
    print('szkoła')
elif wiek <= 64:
    print('dorosły')
else:
    print('emeryt')

