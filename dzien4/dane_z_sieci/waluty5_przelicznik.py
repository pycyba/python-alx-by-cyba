import requests
import typing

def pobierz_tabele(data:str='') -> typing.Dict:
    adres = f'https://api.nbp.pl/api/exchangerates/tables/A/{data}?format=json'
    response = requests.get(adres)
    if response.status_code != 200:
        raise KeyError
    return response.json()[0]


def znajdz_walute(tabela:typing.Dict, szukany_kod:str) -> typing.Dict:
    for rate in tabela["rates"]:
        if rate["code"] == szukany_kod:
            return rate
    # jeśli nie znajdziemy takiej waluty, to zgłaszamy KeyError
    raise KeyError


def pracuj_z_waluta(rate: typing.Dict):
    print(f'Waluta {rate["currency"]} ({rate["code"]}) ma kurs {rate["mid"]} PLN')
    while True:
        kwota = float(input('Podaj kwotę (0, aby zakończyć): '))
        if kwota == 0: break
        print(f'{kwota:.2f} {rate["code"]} = {kwota * rate["mid"]:.2f} PLN')
        print(f'{kwota:.2f} PLN = {kwota / rate["mid"]:.2f} {rate["code"]}')


def pracuj_z_tabela(tabela:typing.Dict):
    print(f'Pobrano tabelę nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')
    while True:
        szukany_kod = input('Podaj kod waluty (pusty, aby zakończyć): ').strip().upper()
        if not szukany_kod: break
        try:
            rate = znajdz_walute(tabela, szukany_kod)
            pracuj_z_waluta(rate)
        except KeyError:
            print(f'Nie ma waluty o kodzie {szukany_kod}')


def main():
    while True:
        data = input('Podaj datę, lub pusty napis, aby pobrać bieżące, lub słowo "koniec", aby zakończyć\n: ').lower()
        if data == 'koniec':
            break
        try:
            tabela = pobierz_tabele(data)
            pracuj_z_tabela(tabela)
        except KeyError:
            print('Brak danych dla tej daty')
        except Exception as e:
            print('Inny błąd:', e)


if __name__ == '__main__':
    main()
