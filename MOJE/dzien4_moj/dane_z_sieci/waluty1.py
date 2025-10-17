# requests jest dodatkową biblioteką programistyczną poza standardem Pythona
# i wymaga doinstalowania

import requests

dane = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json').json()
print('dane jest typu', type(dane).__name__, ', rozmiar', len(dane))

tabela = dane[0]
print('tabela jest typu', type(tabela).__name__, ', rozmiar', len(tabela))
print('pola obiektu tabela:', tabela.keys())

rates = tabela["rates"]
print('rates jest typu', type(rates).__name__, ', rozmiar', len(rates))

jeden_rate = rates[1]
print('rate jest typu', type(jeden_rate).__name__, ', rozmiar', len(jeden_rate))
print(jeden_rate)
print(jeden_rate["mid"])
# wersja skrótowa, jednolinijkowa:
print(dane[0]["rates"][1]["mid"])
print()

print(f'Tabela nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')
for rate in rates:
    print(rate["code"], rate["currency"], rate["mid"])
