"""

Write a program that, based on the player's position (x, y) on the
board in the range from 0 to 100, displays their approximate
location (center, upper right corner, upper edge, . . . ) or
information about their position outside the board. Assume a value of 10 as the
edge margin.
Example program message:
Enter player position X: 95
Enter player position Y: 95
The player is in the upper right corner.

Translated with DeepL.com (free version)

"""

try:
    poz_x = int(input("Podaj pozycję x: "))
    poz_y = int(input("Podaj pozycję y: "))
except ValueError:
    print("Błąd: podaj poprawne liczby całkowite.")
    exit()

if poz_x < 0 or poz_x > 100 or poz_y < 0 or poz_y > 100:
    print("Gracz jest poza planszą.")
elif poz_x >= 90 and poz_y >= 90:
    print("Gracz znajduje się w prawym górnym rogu.")
elif poz_x <= 10 and poz_y >= 90:
    print("Gracz znajduje się w lewym górnym rogu.")
elif poz_x <= 10 and poz_y <= 10:
    print("Gracz znajduje się w lewym dolnym rogu.")
elif poz_x >= 90 and poz_y <= 10:
    print("Gracz znajduje się w prawym dolnym rogu.")
elif poz_y >= 90:
    print("Gracz znajduje się na górnej krawędzi.")
elif poz_y <= 10:
    print("Gracz znajduje się na dolnej krawędzi.")
elif poz_x <= 10:
    print("Gracz znajduje się na lewej krawędzi.")
elif poz_x >= 90:
    print("Gracz znajduje się na prawej krawędzi.")
else:
    print("Gracz znajduje się w centrum.")
