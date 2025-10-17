"""
Program w kolejnych liniach wypisuje liczby od 1 do limit włącznie
a obok nich ich kwadraty i szcześciany (liczby podniesione do drugiej i trzeciej potęgi).
Jeśli dasz radę, wyrównaj kolumny za pomocą f-stringów.
"""

limit = int(input('Podaj limit: '))
for i in range(1, limit+1):
    print(i, i**2, i**3)
    # print(f'{i} {i**2} {i**3}')
    # print(f'{i:4} {i**2:8} {i**3:12}')
    # print(f'{i:<4} {i**2:<8} {i**3:<12}')
    # print(f'{i:^4} {i**2:^8} {i**3:^12}')
    # print('{:4} {:8} {:12}'.format(i, i**2, i**3))
    # print('%4d %8d %12d' % (i, i**2, i**3))
    # zapis z języka C:
    # printf("%4d %8d %12d\n", i, i*i, i*i*i)
print()

# dynamiczne obliczenie szerokości kolumn
szer1 = len(str(limit))
szer2 = len(str(limit**2))
szer3 = len(str(limit**3))
for i in range(1, limit+1):
    print(f'| {i:{szer1}} | {i**2:{szer2}} | {i**3:{szer3}} |')
