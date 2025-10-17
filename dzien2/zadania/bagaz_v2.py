# w tej wersji: warunek negatywny, wszystkie rzeczy sprawdzane w jednym ifie

a = float(input('Podaj długość: '))
b = float(input('Podaj szerokość: '))
c = float(input('Podaj wysokość: '))
obj = a*b*c

if a > 50 or b > 50 or c > 50 or obj > 50_000:
    print('Bagaż odrzucony')
else:
    print('Bagaż spełnia normy')
