"""
Napisz program typu 'przelicznik walut', który pozwala:
- pobrać bieżące kursy
- "dla chętnych" - pozwala także pobrać kursy z określonej daty
- podać kod waluty i kwotę do przeliczenia
- przelicza podaną kwotę z podanej waluty na PLN zgodnie z kursem z tabeli
- "dla chętnych" - przeliczaj także kwoty w PLN na podaną walutę
  (sam wymyśl sposób podawania tych kwot i walut)
"""

import requests

data = input('Podaj datę w formacie YYYY-MM-DD lub naciśnij enter dla daty bieżącej:\n')
url = f'https://api.nbp.pl/api/exchangerates/tables/A/{data}?format=json'
try:
    dane = requests.get(url).json()
    tabela = dane[0]
    print(f'Pobrano tabelę nr {tabela["no"]} z dnia {tabela["effectiveDate"]}.')

    szukany_kod = input('Podaj kod waluty obcej:\n').upper()
    for rate in tabela["rates"]:
        if rate["code"] == szukany_kod:
            print(f'Znaleziono walutę {rate["currency"]}, kurs {rate["mid"]} PLN')
            wybor = input(f'Czy chcesz przeliczać {szukany_kod} na PLN (wybierz 1), czy PLN na {szukany_kod} (wybierz 2)?\n')
            kwota = float(input('Podaj kwotę:\n'))
            if wybor == '1':
                wynik = kwota * rate["mid"]
                print(f'{kwota:.2f} {szukany_kod} = {wynik:.2f} PLN')
            elif wybor == '2':
                wynik = kwota / rate["mid"]
                print(f'{kwota:.2f} PLN = {wynik:.2f} {szukany_kod}')
            break
    else:
        print(f'Nie znaleziono waluty o kodzie {szukany_kod}')

    print('Dziękujemy za skorzystanie z usług naszego kantoru')
except Exception:
    print('Błąd. Prawdopodobnie niepoprawna data.')
