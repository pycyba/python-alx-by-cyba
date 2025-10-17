"""
Program pobiera trzy liczby - wymiary bagażu w cm.
Program ma wypisać, czy bagaż mieści się w limicie:
- żaden wymiar nie może przekraczać 50 cm
- objętość nie może przekraczać 50 tys cm³
"""

# W tej wersji: warunek pozytywny, wszystkie rzeczy sprawdzane w jednym ifie

a = float(input('Podaj długość: '))
b = float(input('Podaj szerokość: '))
c = float(input('Podaj wysokość: '))
obj = a*b*c

if a <= 50 and b <= 50 and c <= 50 and obj <= 50_000:
    print('Bagaż spełnia normy')
else:
    print('Bagaż odrzucony')
