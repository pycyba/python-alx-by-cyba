koniec = True
proba = 0
while koniec:
    import random

    slownik = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Losowanie 1000 rzutów
    for _ in range(1000):
        kostka = random.randint(1, 6)
        slownik[kostka] += 1  # To wystarczy — bez if/elif!

    # Wypisanie wyników
    for oczko in range(1, 7):
        procent = (slownik[oczko] / 1000) * 100
        print(f"{oczko}: {procent:.1f}%")
        if procent> 20:
            print("WOw powyzej 20%")
            koniec = False
        else:
            print("Lipa")

    proba += 1
print(f"{proba}")
print(slownik)

