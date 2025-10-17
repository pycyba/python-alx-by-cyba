x = int(input("Podaj ile wierszy: "))
y = int(input("Podaj ile kolumn: "))

# szerokość kolumn = liczba cyfr największego elementu
d = len(str(x * y))

# nagłówki kolumn
print(" " * (d+1), end="")  # puste miejsce na róg
for kolumna in range(1, y+1):
    print(f"{kolumna:{d}}", end=" ")
print()

# oddzielająca linia
print("-" * ((d+1) * (y+1)))

# właściwa tabliczka
for wiersz in range(1, x+1):
    print(f"{wiersz:{d}}|", end=" ")  # nagłówek wiersza
    for kolumna in range(1, y+1):
        print(f"{wiersz * kolumna:{d}}", end=" ")
    print()