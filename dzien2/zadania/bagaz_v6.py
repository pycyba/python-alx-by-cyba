# Niech program wypisuje wszystkie informacje o błędach,
# ale na końcu podaje też informację zbiorczą, czy można przepuścić bagaż.
# W tej wersji robimy to w oparciu o zmienną logiczną.

a = float(input('Podaj długość: '))
b = float(input('Podaj szerokość: '))
c = float(input('Podaj wysokość: '))
obj = a*b*c
wszystko_ok = True

if a > 50:
    print('zbyt duża długość')
    wszystko_ok = False
if b > 50:
    print('zbyt duża szerokość')
    wszystko_ok = False
if c > 50:
    print('zbyt duża wysokość')
    wszystko_ok = False
if obj > 50_000:
    print('zbyt duża objętość')
    wszystko_ok = False

if wszystko_ok:
    print('Bagaż spełnia normy')
else:
    print('Bagaż odrzucony')
