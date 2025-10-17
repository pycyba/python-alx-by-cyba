import requests

dane = requests.get('https://api.nbp.pl/api/exchangerates/tables/A/?format=json',
                    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'}).json()
tabela = dane[0]
print(f'Pobrano tabelę nr {tabela["no"]} z dnia {tabela["effectiveDate"]}.')

kursy = {rate["code"]: rate["mid"] for rate in tabela["rates"]}
# dodaję sztuczny wpis PLN z kursem 1.0
kursy["PLN"] = 1
print(kursy)

print('Podawaj specyfikacje w formie 1000 USD to EUR')
print('Aby zakończyć, wprowadź pustą linię.')
while True:
    wejscie = input('> ').strip().upper()
    if not wejscie: break
    kwota, kod1, to, kod2 = wejscie.split()
    kwota = float(kwota)
    try:
        kurs1 = kursy[kod1]
        kurs2 = kursy[kod2]
        wynik = kwota * kurs1 / kurs2
        print(f'{kwota:.2f} {kod1} = {wynik:.2f} {kod2}')
    except KeyError as e:
        print(f'Nie ma waluty o kodzie {e}')
