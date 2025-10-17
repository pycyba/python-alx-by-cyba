# https://api.nbp.pl/api/exchangerates/tables/a/?format=json
# https://api.nbp.pl/api/exchangerates/tables/a/2025-09-01?format=json

import requests

data = input('Podaj datę w formacie YYYY-MM-DD lub naciśnij enter: ')
# pobierz tabelę dla podanej daty lub tabelę bieżącą,
url = f'https://api.nbp.pl/api/exchangerates/tables/a/{data}?format=json'
response = requests.get(url)
print('response:', response)

if response.status_code == 404:
    print('Ta data nie jest obsługiwana')
elif response.status_code != 200:
    print(f'Inny błąd HTTP, ale nie wiem o co chodzi, status {response.status_code}')
else:
    tabela = response.json()[0]
    print(f'Tabela nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')
    for rate in tabela["rates"]:
        print(f'{rate["code"]:3} – kurs średni: {rate["mid"]:10.8f}, waluta {rate["currency"]}')

