'''
Napisz program, który pozwala przeliczać kwoty z innych walut na złote oraz ze złotych na inne waluty
w oparciu o kursy pobrane z serwisu NBP.
- Jeśli użytkownik poda datę, to pobierane są kursy archiwalne,
- Jeśli nie poda daty, to pobierane są kursy bieżące.
- (dla chętnych - możliwość zmiany daty w trakcie działania programu)

- Użytkownik podaje kod waluty (np. USD), a program znajduje i wyświetla kurs tej waluty
- Użytkownik podaje kwotę w tej walucie, a program wylicza ile to jest PLN
- Powinna być też opcja przeliczania kwoty w PLN na inną walutę
'''

# wersja rozbudowana - wiele razy można pobierać tabelę, wybierać wiele walut, podawać wiele kwot
import requests

ADRES_BAZOWY = 'https://api.nbp.pl/api/exchangerates/tables/a/'

def pobierz_tabele(data = ''):
    adres = ADRES_BAZOWY + data + '?format=json'
    response = requests.get(adres)
    if response.status_code == 404:
        return None
    if response.status_code != 200:
        raise ValueError(f'Problem z pobieraniem danych, kod {response.status_code}')
    return response.json()[0]


def znajdz_walute(rates, code):
    for rate in rates:
        if rate["code"] == code:
            return rate
    return None


def dzialaj_z_jedna_waluta(waluta):
    code = waluta["code"]
    mid = waluta["mid"]
    print(f'Kod: {code}, nazwa: {waluta["currency"]}, kurs średni: {mid}')
    while True:
        kwota = float(input('Podaj kwotę do przeliczenia albo 0, aby zakończyć pracę z wybraną walutą\n> '))
        if kwota == 0:
            break
        print(f'{kwota:.2f} {code} = {kwota * mid :.2f} PLN')
        print(f'{kwota:.2f} PLN = {kwota / mid :.2f} {code}')
    print()


def dzialaj_z_jedna_tabela(tabela):
    rates = tabela["rates"]
    while True:
        print(f'Tabela {tabela["table"]} nr {tabela["no"]} z dnia {tabela["effectiveDate"]}')
        kod = input('Podaj kod waluty, lub naciśnij enter, aby zakończyć pracę z bieżącą tabelą walut\n> ').strip().upper()
        if kod == '':
            break
        waluta = znajdz_walute(rates, kod)
        if not waluta:
            print(f'Nie znaleziono waluty o kodzie {kod}')
            continue
        dzialaj_z_jedna_waluta(waluta)
    print()


pytanie = '''Podaj datę w formacie YYYY-MM-DD, aby pobrać kursy archiwalne,
albo naciśnij enter, aby pobrać kursy bieżące
albo wpisz koniec, aby zakończyć program.
> '''

def main():
    while True:
        wybor = input(pytanie)
        if wybor.lower() == 'koniec':
            break
        try:
            if wybor == '':
                tabela = pobierz_tabele()
            else:
                tabela = pobierz_tabele(wybor)
            dzialaj_z_jedna_tabela(tabela)
        except Exception as e:
            print('Nastąpił błąd', e)


if __name__ == '__main__':
    main()
