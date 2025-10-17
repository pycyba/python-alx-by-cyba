import requests

# ewentualnie pytanie o datę...
url = 'https://api.nbp.pl/api/exchangerates/tables/A/?format=json'
dane = requests.get(url).json()

szukana_waluta = input('Podaj kod waluty: ').upper()
kwota = float(input('Podaj kwotę do przeliczenia: '))
rates = dane[0]["rates"]
for rate in rates:
    if rate["code"] == szukana_waluta:
        print('Znaleziona waluta: ', rate)
        kurs = rate["mid"]
        print(f'{kwota:.2f} {szukana_waluta} = {kwota * kurs :.2f} PLN')
        print(f'{kwota:.2f} PLN = {kwota / kurs :.2f} {szukana_waluta}')
        break

