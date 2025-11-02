import random

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def hint(prev_dist, curr_dist):
    if curr_dist < prev_dist:
        return "Cieplej 🔥 (bliżej skarbu)"
    elif curr_dist > prev_dist:
        return "Zimniej ❄️ (dalej od skarbu)"
    else:
        return "Bez zmian (ani bliżej, ani dalej)"

def move_treasure():
    return random.randint(1, 10), random.randint(1, 10)

treasure_x = random.randint(1, 10)
treasure_y = random.randint(1, 10)

player_x = random.randint(1, 10)
player_y = random.randint(1, 10)

ruchy = 0
min_steps = manhattan(player_x, player_y, treasure_x, treasure_y)
prev_dist = min_steps

print("Szukaj skarbu! Sterowanie: W=góra, S=dół, A=lewo, D=prawo")

while True:
    if ruchy == 0:
        print(f"Twoja pozycja x: {player_x}  y: {player_y}")
    else:
        print(f"Twoja pozycja x: {player_x}  y: {player_y}, liczba ruchów: {ruchy}")

    komenda = input("Podaj komendę: ").lower().strip()
    if komenda == 'w':
        player_y -= 1
    elif komenda == 's':
        player_y += 1
    elif komenda == 'a':
        player_x -= 1
    elif komenda == 'd':
        player_x += 1
    else:
        print("Nieprawidłowy ruch")
        continue

    ruchy += 1

    # poza planszą
    if player_x < 1 or player_x > 10 or player_y < 1 or player_y > 10:
        print("Przegrałeś (wyszedłeś poza planszę).")
        break

    # znaleziono skarb
    if player_x == treasure_x and player_y == treasure_y:
        print(f"Wygrałeś, gratulacje! Znalazłeś skarb w {ruchy} ruchach")
        break

    # podpowiedź z prawdopodobieństwem 4/5
    curr_dist = manhattan(player_x, player_y, treasure_x, treasure_y)
    if random.randrange(5) != 0:
        print(hint(prev_dist, curr_dist))
    else:
        print("Brak podpowiedzi tym razem... 🤫")
    prev_dist = curr_dist

    # przeniesienie skarbu po przekroczeniu dwukrotności minimalnych kroków
    if ruchy > 2 * min_steps:
        old_tx, old_ty = treasure_x, treasure_y
        treasure_x, treasure_y = move_treasure()
        while treasure_x == player_x and treasure_y == player_y:
            treasure_x, treasure_y = move_treasure()
        min_steps = manhattan(player_x, player_y, treasure_x, treasure_y)
        prev_dist = min_steps
        print("Skarb przemieścił się w inne miejsce!")