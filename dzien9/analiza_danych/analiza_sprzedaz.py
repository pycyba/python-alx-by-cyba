import pandas as pd

sprzedaz = pd.read_csv('sprzedaz.csv', sep=',', encoding='utf-8', parse_dates=['data'])
print(f'Wczytano {len(sprzedaz)} rekordów.')
print(sprzedaz["miasto"].unique())
sprzedaz["wartość"] = sprzedaz["cena"] * sprzedaz["sztuk"]

# Zadanko 1
# Użytkownik podaje nazwę kolumny i nazwę funkcji, a program oblicza to za pomocą agg
kolumna = input('Podaj nazwę kolumny: ')
funkcja = input('Podaj nazwę funkcji: ')
wynik = sprzedaz[kolumna].agg(funkcja)
print(wynik)
print()

# Zadanie 2
# Użytkownik podaje:
# nazwę kolumny, po której chcemy dane grupować
# nazwę kolumny, dla której obliczamy funkcję
# nazwę funkcji
# * jeśli potrafisz :) - w każdym z tych punktów pozwól na podane LISTY kolumn lub funkcji
#   pewnie trzeba będzie umówić się na sposób rozdzielania (spacja, przecinek czy coś innego) i użyć split

# jedna kolumna, jedna funkcja
kolumna_grp = input('Podaj nazwę kolumny do grupowania: ')
kolumna_agg = input('Podaj nazwę kolumny do obliczenia: ')
funkcja = input('Podaj nazwę funkcji: ')
wynik = sprzedaz.groupby(kolumna_grp)[kolumna_agg].agg(funkcja)
# wynik = sprzedaz.groupby(kolumna_grp).agg({kolumna_agg: funkcja})
# wynik może być wielowierszowy
print(wynik)
print()
