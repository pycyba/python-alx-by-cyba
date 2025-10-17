# Niech program wypisuje wszystkie informacje o błędach,
# ale na końcu podaje też informację zbiorczą, czy można przepuścić bagaż.
# W tej wersji robimy to za pomocą "listy błędów".

a = float(input('Podaj długość: '))
b = float(input('Podaj szerokość: '))
c = float(input('Podaj wysokość: '))
obj = a*b*c
bledy = []

if a > 50:
    bledy.append('zbyt duża długość')
if b > 50:
    bledy.append('zbyt duża szerokość')
if c > 50:
    bledy.append('zbyt duża wysokość')
if obj > 50_000:
    bledy.append('zbyt duża objętość')

if not bledy:
    print('Bagaż spełnia normy')
else:
    print('Bagaż odrzucony. Znalezione problemy:')
    for blad in bledy:
        print(' -', blad)


# Inne opcje wypisania elementów listy:
# print(bledy)
# print(*bledy, sep=', ')
# print('; '.join(bledy))
