import pickle

class Osoba:
    WIEK_PELNOLETNIOSCI = 18

    def __init__(self, imie, nazwisko, wiek=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat')

    def pelnoletnia(self):
        return self.wiek >= Osoba.WIEK_PELNOLETNIOSCI

    def __str__(self):
        return f'Osoba {self.imie} {self.nazwisko}, {self.wiek} lat'



def zapisz_pikle(o:Osoba, path:str="dane.pickle"):
    with open(path, "wb") as f:
        pickle.dump(o, f)

def czytaj_pikle(path:str="dane.pickle"):
    with open(path, "rb") as f:
        o = pickle.load(f)
        return o


def main():
    ala = Osoba('Ala', 'Kowalska', 30)
    print(ala)
    if ala.pelnoletnia(): print('pełnoletnia')
    print('zapisuję')
    zapisz_pikle(ala)
    print()
    print('czytam')
    osoba = czytaj_pikle()
    print(osoba, 'typu', type(osoba))
    osoba.przedstaw_sie()
    if osoba.pelnoletnia(): print('nadal pełnoletnia')


if __name__ == '__main__':
    main()