# Tutaj pobieramy dane proste z sieci.
# Używamy rzeczy, które są w bibliotece standardowej Pythona.

import json
from urllib import request

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'

print('Pobieram dane...')

# Bez żadnych dodatkowych bibliotek można pobrać dane z sieci i potraktować jak JSON-a w taki sposób:
with request.urlopen(ADRES) as response:
    txt = response.read().decode('utf-8')

dane = json.loads(txt)

print(dane)
print('typ zmiennej dane:', type(dane))

# lista zawiera jeden element, którym jest słownik
tabela = dane[0]
print('typ zmiennej tabela:', type(tabela))

print('Numer tabeli:', tabela["no"])
print('Data tabeli:', tabela["effectiveDate"])
print()

rates = tabela["rates"]
print('typ zmiennej rates:', type(rates))
print('liczba elementów:', len(rates))
print()

# Tutaj rate jest słownikiem, który pełni rolę obiektu.
# W tym słowniku są trzy pola: currency (nazwa waluty), code (kod 3-literowy), mid (kurs średni)
for rate in rates:
    print(rate)
    # print(rate["code"], rate["currency"], rate["mid"])
