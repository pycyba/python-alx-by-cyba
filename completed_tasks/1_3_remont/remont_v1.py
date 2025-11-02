# Tak bym to zrobił nie używając żadnych struktur danych (typu lista / słownik), tylko "tak po prostu"

print('Podaj wymiary pomieszczenia w metrach (np. 3.75 )')
a = float(input('długość  : '))
b = float(input('szerokość: '))
h = float(input('wysokość : '))
obwod = 2*a + 2*b
pow_podlogi = a*b
pow_scian = obwod*h

suma = 0
wybor = input('Czy chcesz gipsować ściany? [T/N] ').strip().upper()
if wybor == 'T':
    suma += pow_scian * 100

wybor = input('Czy chcesz malować ściany i sufit? [T/N] ').strip().upper()
if wybor == 'T':
    suma += (pow_scian + pow_podlogi) * 30

wybor = input('Czy chcesz kłaść panele podłogowe? [T/N] ').strip().upper()
if wybor == 'T':
    suma += pow_podlogi * 50

wybor = input('Czy chcesz kłaść listwy podłogowe? [T/N] ').strip().upper()
if wybor == 'T':
    suma += obwod * 40

print(f'Łączny koszt prac wyniesie {suma:.2f} zł')
