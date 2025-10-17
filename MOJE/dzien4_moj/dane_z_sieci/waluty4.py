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

    a, b = input("Podaj kod waluty oraz kwotę (oddziel spację): ").split()
    b = float(b)
    a = a.upper()

    # szukamy tej waluty
    wybrany = None
    for rate in tabela["rates"]:
        if rate["code"] == a:
            wybrany = rate
            break

    if wybrany:
        kurs = wybrany["mid"]
        print(f" {b} {a} = {b * kurs:.2f} PLN")

        # dla chętnych PLN → waluta:
        pln = float(input("Podaj ile PLN chcesz przeliczyć na tę walutę: "))
        print(f"{pln:.2f} PLN = {pln / kurs:.2f} {a}")
    else:
        print("Nie ma takiej waluty w tabeli")