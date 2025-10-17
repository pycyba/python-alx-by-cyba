liczba = int(input("Liczba: "))

for i in range(1, liczba+1):
    spacje = " " * (liczba - i)
    gwiazdki = "*" * (2*i - 1)
    print(spacje + gwiazdki)