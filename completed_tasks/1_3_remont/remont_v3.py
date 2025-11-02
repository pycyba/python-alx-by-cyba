# w tej wersji w słowniku prac zapisuję obliczone koszty, a nie ceny jednostkowe.
# dlatego słownik powstaje po odczytaniu wymiarów

print('Podaj wymiary pomieszczenia w metrach (np. 3.75 )')
a = float(input('długość  : '))
b = float(input('szerokość: '))
h = float(input('wysokość : '))
obwod = 2*a + 2*b
pow_podlogi = a*b
pow_scian = obwod*h

prace = {
    'gipsowanie': 100 * pow_scian,
    'malowanie': 30 * (pow_scian + pow_podlogi),
    'panele podłogowe': 50 * pow_podlogi,
    'listwy podłogowe': 40 * obwod,
}

suma = 0
for praca, koszt in prace.items():
    wybor = input(f'Czy chcesz wykonać pracę "{praca}", której koszt wynosi {koszt:.2f} zł?\nT / N: ').strip().upper()
    if wybor == 'T':
        suma += koszt
        print('Koszt pracy doliczony')
    elif wybor == 'N':
        print('OK, nie liczę tej pracy')
    else:
        print('Niepoprawny wybór - tej pracy nie liczę.')

print(f'Łączny koszt prac wyniesie {suma:.2f} zł')
