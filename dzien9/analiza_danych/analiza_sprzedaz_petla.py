import pandas as pd

pd.options.display.max_columns = 100
pd.options.display.max_rows = 500

sprzedaz = pd.read_csv('sprzedaz.csv', sep=',', encoding='utf-8', parse_dates=['data'])
print(f'Wczytano {len(sprzedaz)} rekordów.')
sprzedaz["wartość"] = sprzedaz["cena"] * sprzedaz["sztuk"]

while True:
    kolumny_grp = input('Podaj nazwy kolumn do grupowania rozdzielając przecinkami:\n').split(',')
    # opcjonalny krok - usunięcie spacji z początku i końca każej nazwy:
    kolumny_grp = [nazwa.strip() for nazwa in kolumny_grp]
    kolumny_agg = input('Podaj nazwy kolumn do obliczenia:\n').split(',')
    kolumny_agg = [nazwa.strip() for nazwa in kolumny_agg]
    funkcje = input('Podaj nazwy funkcji do obliczenia:\n').split(',')
    funkcje = [nazwa.strip() for nazwa in funkcje]
    try:
        wyniki = sprzedaz.groupby(kolumny_grp)[kolumny_agg].agg(funkcje)
        print(wyniki)
    except Exception as e:
        print('Wystąpił błąd:', e)
    print()
    czy = input('Czy chcesz wykonać kolejne obliczenie [T/N]?')
    if czy.upper() == 'N':
        break

print('Do widzenia')
