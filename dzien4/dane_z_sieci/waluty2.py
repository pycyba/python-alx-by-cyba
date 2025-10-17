# https://api.nbp.pl/api/exchangerates/tables/a/?format=json
# https://api.nbp.pl/api/exchangerates/tables/a/2025-09-01?format=json

import requests

data = input('Podaj datę w formacie YYYY-MM-DD lub naciśnij enter: ')
# pobierz tabelę dla podanej daty lub tabelę bieżącą,
url = f'https://api.nbp.pl/api/exchangerates/tables/a/{data}?format=json'

try:
    dane = requests.get(url).json()
    tabela = dane[0]

    # wypisz ogólne informacje
    print(f'Tabela nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')
    # oraz wylistuj wszystkie waluty i ich kursy
    for rate in tabela["rates"]:
        print(f'{rate["code"]:3} – kurs średni: {rate["mid"]:10.8f}, waluta {rate["currency"]}')
except Exception as e:
    print(f'Błąd typu {type(e).__name__}. Prawdopodobnie nieobsługiwana data.')
    print(e)
