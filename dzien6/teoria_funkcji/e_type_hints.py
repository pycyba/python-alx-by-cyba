# Od Pythona 3.5 częścią składni stały się "type hints", czyli informacje o typach zmiennych i funkcji,
# do tej pory stosowane w docstringach i komentarzach.

# Informacje o typie mają charakter niezobowiązujących podpowiedzi.
# Stanowią dokumentację oraz wpływają na podpowiedzi dawane przez edytory oraz narzędzia kontroli jakości kodu.
# Ale nie są weryfikowane przez interpreter Pythona!

# typ zmiennej:
x:int = 15
imie:str = "Ala"
print(x)

# nadal można na zmienną wpisać wartość innego typu i to nie będzie błąd Pythona (tylko edytor na nas nakrzyczy)
x = 'Ala ma kota'
print(x)

x:int = 'to nie jest liczba'
print(x)

# Typ parametrów i wyniku funkcji:
def pole_kola(r:float) -> float:
    import math
    return math.pi * r**2


# Do opisania typów kolekcji oraz pewnych szczególnych sytuacji, używa się definicji z moduły typing
import typing

def wypisz_n_razy(napis:str, ile_razy:int=1) -> typing.NoReturn:
    for i in range(ile_razy):
        print(napis)


# W przypadku parametrów *args / **kwargs typ podany za :dwukropkiem jest typem pojedynczego elementu
def suma(*liczby:int) -> int:
    suma = 0
    for x in liczby:
        suma += x
    return suma


def pierwsza_polowa(dane:typing.Sequence) -> typing.List:
    return list(dane[0:len(dane)//2])


def wypisz_cennik(cennik:typing.Dict[str, int]) -> typing.NoReturn:
    for k, v in cennik.items():
        print(f'{k} kosztuje {v}')


def posortuj_teksty(teksty:typing.List[str]) -> typing.List[str]:
    import locale
    locale.setlocale(locale.LC_COLLATE, '')
    return sorted(teksty, key=locale.strxfrm)


def fikumiku(arg:int) -> typing.Union[str,int]:
    if arg % 2 == 0:
        return f"napis {arg}"
    else:
        return 10*arg # liczba


# Pewien problem stanowi odwołanie się do klasy wewnątrz jej definicji (bo ona jeszcze nie istnieje w tym momencie).
# Przyjęto, że w tej sytuacji wpisuje się nazwę tej klasy jako string.
class Punkt:
    def __init__(self, x:float=0, y:float=0):
        self.x = x
        self.y = y

    def przesuniety(self, dx:float, dy:float) -> 'Punkt':
        '''Zwraca punkt przesunięty o podane współrzędne jako nowy obiekt'''
        return Punkt(self.x + dx, self.y + dy)
