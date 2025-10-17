gipsowanie_scian = 100
malowanie_scian_sufitu = 30
polozenie_paneli = 50
polozenie_listew = 40

a, b, h = map(int, input("Podaj wymiary pokoju (długość szerokość wysokość): ").split())

powierzchnia_podlogi = a * b
powierzchnia_sufitu = a * b
powierzchnia_sciany_a = a * h
powierzchnia_sciany_b = b * h
obwod = 2 * (a + b)

czy_gipsowac = input("Czy gipsować ściany (T/N): ").upper()
czy_malowac = input("Czy malować ściany i sufit (T/N): ").upper()
czy_panele = input("Czy położyć panele (T/N): ").upper()
czy_listwy = input("Czy położyć listwy (T/N): ").upper()

suma = 0
if czy_gipsowac == "T":
    suma += (2 * powierzchnia_sciany_a + 2 * powierzchnia_sciany_b) * gipsowanie_scian
if czy_malowac == "T":
    suma += (2 * powierzchnia_sciany_a + 2 * powierzchnia_sciany_b + powierzchnia_sufitu) * malowanie_scian_sufitu
if czy_panele == "T":
    suma += powierzchnia_podlogi * polozenie_paneli
if czy_listwy == "T":
    suma += obwod * polozenie_listew

print(f"Łączna cena: {suma:.2f} zł")