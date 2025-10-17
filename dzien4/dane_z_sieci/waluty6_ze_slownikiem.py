import requests

dane = requests.get('https://api.nbp.pl/api/exchangerates/tables/A/?format=json').json()
tabela = dane[0]
print(f'Pobrano tabelę nr {tabela["no"]} z dnia {tabela["effectiveDate"]}.')

# W tej wersji programu budujemy słownik, w którym kluczami będą kody walut, a wartościami ich kursy (liczby)
# kursy = {kod: kurs}
kursy = {rate["code"]: rate["mid"] for rate in tabela["rates"]}

print(kursy)

while True:
    szukany_kod = input('Podaj kod waluty: ').strip().upper()
    if not szukany_kod: break
    if szukany_kod not in kursy:
        print(f'Nie ma waluty o kodzie {szukany_kod}')
        continue
    kurs = kursy[szukany_kod]
    print('Kurs:', kurs)
    kwota = float(input('Podaj kwotę: '))
    print(f'{kwota:.2f} {szukany_kod} = {kwota * kurs:.2f} PLN')
    print(f'{kwota:.2f} PLN = {kwota / kurs:.2f} {szukany_kod}')
