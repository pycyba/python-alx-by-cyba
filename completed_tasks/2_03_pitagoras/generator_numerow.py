'''
Za pomocą list comprehension wygeneruj listę wszystkich możliwych numerów telefonu postaci '+48123XYYYYY',
gdzie X jest cyfrą z zakresu od 1 do 5, a na każdej pozycji oznaczonej Y mogą być dowolne cyfry (od 0 do 9).

Nie wypisuj tej listy w całości, a wypisz info o jej rozmiarze
oraz 10 pierwszych i 10 ostatnich elementów (użyj notacji z :dwukropkiem)

Używając odpowiedniej funkcji z modułu random, wypisz 10 losowych elementów z wnętrza listy.
'''

# idea rozwiązania na małym zakresie:
#numery = ['+48123' + str(x) for x in range(1, 6)]

# teraz kolejne wersje równoważne pod względem działania, ale z coraz bardziej zwięzłym zapiesem

# numery = ['+48123' + str(x) + str(y1) + str(y2) + str(y3) + str(y4) + str(y5)
#           for x in range(1, 6)
#           for y1 in range(10)
#           for y2 in range(10)
#           for y3 in range(10)
#           for y4 in range(10)
#           for y5 in range(10)]

# numery = [f'+48123{x}{y1}{y2}{y3}{y4}{y5}'
#           for x in range(1, 6)
#           for y1 in range(10)
#           for y2 in range(10)
#           for y3 in range(10)
#           for y4 in range(10)
#           for y5 in range(10)]

# numery = [f'+48123{x}{y:05}'
#           for x in range(1, 6)
#           for y in range(100000)]

numery = [f'+48123{x}' for x in range(100000, 600000)]


print('len:', len(numery))
print('początek:', numery[:10])
print('koniec:', numery[-10:])
print()

# random i losowy wybór elementów
from random import sample

print('sample:', sample(numery, 10))
