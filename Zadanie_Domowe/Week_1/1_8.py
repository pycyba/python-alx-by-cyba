import random

# pozycja skarbu
skarb_x = random.randint(0, 9)
skarb_y = random.randint(0, 9)

# pozycja gracza losowa
gracz_x = random.randint(0, 9)
gracz_y = random.randint(0, 9)

ruchy = 0
print("Szukaj skarbu! Sterowanie: W= góra, S= dół, A= lewo, D= prawo")

while True:
    print(f"Twoja pozycja: ({gracz_x}, {gracz_y})")
    komenda = input("Twój ruch: ").upper()

    if komenda == "W":
        gracz_y -= 1
    elif komenda == "S":
        gracz_y += 1
    elif komenda == "A":
        gracz_x -= 1
    elif komenda == "D":
        gracz_x += 1
    else:
        print("Nieprawidłowy ruch – użyj W, A, S, D")
        continue

    ruchy += 1

    if gracz_x < 0 or gracz_x > 9 or gracz_y < 0 or gracz_y > 9:
        print("Wyszedłeś poza planszę – przegrana!")
        break

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f"Znalazłeś skarb w {ruchy} ruchach!")
        break