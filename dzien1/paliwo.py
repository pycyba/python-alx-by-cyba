miastoA = input('Miasto A: ')
miastoB = input('Miasto B: ')
dystans = float(input(f'Dystans {miastoA}-{miastoB}: '))
cena = float(input('Cena paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))

koszt = dystans * cena * spalanie / 100
print(f'Koszt przejazdu {miastoA}-{miastoB} to {koszt} PLN')
print(f'Koszt przejazdu {miastoA}-{miastoB} to {round(koszt)} PLN')
print(f'Koszt przejazdu {miastoA}-{miastoB} to {koszt:.0f} PLN')
print(f'Koszt przejazdu {miastoA}-{miastoB} to {koszt:.2f} PLN')
