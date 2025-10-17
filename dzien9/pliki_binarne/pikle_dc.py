import pickle
from dataclasses import dataclass

@dataclass
class Osoba:
    imie: str
    nazwisko: str
    wiek: int

    def pelnoletnia(self):
        return self.wiek >= 18


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
    if osoba.pelnoletnia(): print('nadal pełnoletnia')
    

if __name__ == '__main__':
    main()