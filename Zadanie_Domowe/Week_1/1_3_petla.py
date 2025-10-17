a, b, h = map(int, input("Podaj wymiary pokoju (długość szerokość wysokość): ").split())

powierzchnia_podlogi = a * b
powierzchnia_sufitu = a * b
powierzchnia_sciany_a = a * h
powierzchnia_sciany_b = b * h
obwod = 2 * (a + b)

uslugi = [
    ("gipsowanie scian", 100, 2*powierzchnia_sciany_a + 2*powierzchnia_sciany_b ),
    ("malowanie scian", 30, 2*powierzchnia_sciany_a + 2*powierzchnia_sciany_b + powierzchnia_sufitu),
    ("polozenie paneli", 50, powierzchnia_sufitu),
    ("polozenie listew", 40, obwod),
]
suma = 0
for nazwa, cena, jednostka in uslugi:
    odp = input(f"Czy chcesz {nazwa}: T/N \n").upper()
    if odp == "T":
        suma += cena * jednostka

print(f"Łączna cena: {suma:.2f} zł")