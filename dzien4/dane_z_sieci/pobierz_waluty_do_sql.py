import requests

class PobieraczWalut:
    adres_bazowy = 'https://api.nbp.pl/api/exchangerates'
    kwartaly = [
        ('01-01', '03-31'),
        ('04-01', '06-30'),
        ('07-01', '09-30'),
        ('10-01', '12-31'),
    ]

    def __init__(self):
        # dla kodu waluty pamięta jej nazwę, np 'USD': 'dolar amerykański'
        self.nazwy_walut = {}
        # słownik: (data, kod): kurs_średni
        self.kursy = {}

    def daj_kursy_z_jednego_okresu(self, pocz, konc, tab):
        adres = PobieraczWalut.adres_bazowy + f'/tables/{tab}/{pocz}/{konc}?format=json'
        #print(adres)
        response = requests.get(adres)
        if response.status_code != 200:
            raise ValueError(f'Błąd HTTP, kod {response.status_code}')
        return response.json()

    def zaladuj_kursy_z_jednego_okresu(self, pocz, konc, tab):
        json = self.daj_kursy_z_jednego_okresu(pocz, konc, tab)
        for tabela in json:
            # print(tabela["no"])
            data = tabela["effectiveDate"]
            for rate in tabela["rates"]:
                if True or rate["code"] not in self.nazwy_walut:
                    self.nazwy_walut[rate["code"]] = rate["currency"]
                    self.kursy[(data, rate["code"])] = rate["mid"]


    def zaladuj_kursy_z_lat(self, zakres_lat, zakres_tabel=('A',)):
        okresy = [(f'{rok}-{pocz}', f'{rok}-{konc}', tabela)
                  for tabela in zakres_tabel
                  for rok in zakres_lat
                  for (pocz, konc) in PobieraczWalut.kwartaly
                  ]
        for pocz, konc, tab in okresy:
            self.zaladuj_kursy_z_jednego_okresu(pocz, konc, tab)

    def wypisz_sql_walut(self):
        for kod, nazwa in sorted(self.nazwy_walut.items()):
            nazwa = nazwa.replace("'", "''")
            print(f"INSERT INTO waluty(kod, nazwa) VALUES('{kod}', '{nazwa}');")

    def wypisz_sql_kursow(self):
        for (data, kod), kurs in sorted(self.kursy.items()):
            print(f"INSERT INTO kursy(kod, data, kurs) VALUES('{kod}', DATE '{data}', {kurs});")


def main():
    pobieracz = PobieraczWalut()
    pobieracz.zaladuj_kursy_z_lat(range(2023, 2025), ['A', 'B'])
    pobieracz.zaladuj_kursy_z_jednego_okresu('2025-01-01', '2025-03-31', 'A')
    pobieracz.zaladuj_kursy_z_jednego_okresu('2025-04-01', '2025-06-30', 'A')
    pobieracz.zaladuj_kursy_z_jednego_okresu('2025-01-01', '2025-03-31', 'B')
    pobieracz.zaladuj_kursy_z_jednego_okresu('2025-04-01', '2025-06-30', 'B')
    pobieracz.wypisz_sql_walut()
    pobieracz.wypisz_sql_kursow()


if __name__ == '__main__':
    main()