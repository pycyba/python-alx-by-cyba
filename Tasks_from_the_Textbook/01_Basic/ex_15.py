"""
Write a game involving a treasure hunt on a two-dimensional
board measuring 10 by 10. The user can enter
commands to change the character's position. After each move,
the user should receive information about whether they are heading
in the right direction. Going outside the board means the end of the game. After
finding the treasure, print the number of moves used by
the user to reach the goal.
Additionally:
And after taking more than twice the
minimum number of steps, place the treasure in a new location,
And with a probability of 1/5, do not give the player a hint
after taking a step.

"""

import random

treasure_x = random.randint(1, 10)
treasure_y = random.randint(1, 10)

player_x = random.randint(1, 10)
player_y = random.randint(1, 10)

ruchy = 0
print("Szukaj skarbu! Sterowanie: W= góra, S= dół, A= lewo, D= prawo")
while True:
    if ruchy ==0:
        print(f"Twoja pozycja x: {player_x}  y: {player_y} ")
    else:
        print(f"Twoja pozycja x: {player_x}  y: {player_y}, ilosc ruchow: {ruchy}")
    komenda =input("Podaj komende: ").lower()
    if komenda == 'w':
        player_y -= 1
    elif komenda == 's':
        player_y += 1
    elif komenda == 'a':
        player_x -= 1
    elif komenda == 'd':
        player_x += 1
    else:
        print("Nieprawidłowych ruch")
        continue
    ruchy += 1

    if player_x < 1 or player_x > 10 or player_y < 1 or player_y > 10:
        print("Przegrałeś")
        break
    if player_x == treasure_x and player_y == treasure_y:
        print(f"Wygrałeś, gratukuje, znalezleś skarb w {ruchy} ruchach")
        break