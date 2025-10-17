# Napisz funkcję powtorz_napis
# która przyjmuje dwa parametry: napis i liczbę powtórzeń
# i wypisuje na ekran podany napis tyle razy, ile wynosi drugi argument

def powtorz_napis(napis='-', liczba_powtorzen=1):
    for _ in range(liczba_powtorzen):
        print(napis)


# Powinny działać wywołania:
powtorz_napis('Ala ma kota', 5)
powtorz_napis('Ola ma psa', 3)
powtorz_napis('Nie ma mnie', 0)
powtorz_napis('Jeden raz')
powtorz_napis(liczba_powtorzen=4)

p = powtorz_napis('Sierotka ma rysia', 2)
print(p)


