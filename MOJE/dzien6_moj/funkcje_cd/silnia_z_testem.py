"""
W tym pliku mamy:
- definicję zwykłej funkcji `silnia`
- kilka funkcji testujących - ich nazwy rozpoczynają się od test
- funkcję główną `main` - ta nazwa nie ma dla Pythona szczególnego znaczenia

Ten sam plik w PyCharm można uruchamiać na kilka sposobów, a wszystkie są dostępne, gdy się wejdzie w menu Run / Run
(skrót Alt+Shift+F10):
- po prostu "silnia_z_testem" - uruchamia ten plik jako program (w konsoli python silnia_z_testem.py)
  wtedy wykona się kod umieszczony w if __name__ == '__main__'
  czyli wykona się funkcja main
- "Python tests in silnia_z_testem" - uruchamia nasz plik za pomocą biblioteki do testowania; u nas jest to pytest
  odpowiednik konsolowy:  pytest silnia_z_testem.py
  pytest wykonuje wszystkie funkcje z nazwami na test... i raportuje liczbę testów zakończonych sukcesem lub z błędem asercji
- można też uruchomić pojedyncze funkcje testujące

W Pythonie istnieją też testy opisywana jako "doctest".
To są takie fratgmenty w docstringach (czyli tu, gdzie jesteśmy), gdzie udajemy, że wywołujamy funkcję w terminalu Pythona
i pod spodem wpisujemy wynik, który ma się pojawić.
W PyCharm można to uruchomić poprzez Run / Run "Doctests in silnia_z_testem.py"

>>> silnia(0)
1
>>> silnia(5)
120
"""


def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik


def test_silnia_1():
    assert silnia(1) == 1

def test_silnia_5():
    wynik = silnia(5)
    assert wynik == 120


def main():
    while True:
        arg = int(input('Podaj argument: '))
        if arg < 0: break
        wynik = silnia(arg)
        print(f'{arg}! = {wynik}')


if __name__ == '__main__':
    main()
