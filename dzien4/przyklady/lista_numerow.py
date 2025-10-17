"""
Utwórz listę wszystkich możliwych numerów telefonu z pewnego zakresu.
Każdy numer to napis składający się z 9 cyfr.
Ustalmy, że pierwsze cyfry to 123, a kolejne 6 cyfr może być zupełnie dowolne.

Wygenerowana lista powinna mieć rozmiar miliona elementów.
Nie wypisuj jej w całości.
Wypisz 10 pierwszych i 10 ostatnich elementów.
"""

# kilka wersji rozwiązania
# podejście 1 - każdą cyfrę generujemy niezależnie
# numery = ['123' + str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
#                 for a in range(0, 10)
#                 for b in range(0, 10)
#                 for c in range(0, 10)
#                 for d in range(0, 10)
#                 for e in range(0, 10)
#                 for f in range(0, 10)
#          ]

# numery = [f'123{a}{b}{c}{d}{e}{f}'
#                 for a in range(0, 10)
#                 for b in range(0, 10)
#                 for c in range(0, 10)
#                 for d in range(0, 10)
#                 for e in range(0, 10)
#                 for f in range(0, 10)
#          ]


# IMO najlepsze rozwiązanie:
numery = [f'123{x:06}' for x in range(0, 1000000)]
# numery = [f'+48123{x:06}' for x in range(0, 1000000)]

# numery = [str(x) for x in range(123_000_000, 124_000_000)]
# numery = [f'+48{x}' for x in range(123_000_000, 124_000_000)]

# ew. generowanie listy liczb, a nie listy napisów
# numery = [123_000_000 + x for x in range(0, 1000000)]
# numery = [x for x in range(123_000_000, 124_000_000)]
# numery = list(range(123_000_000, 124_000_000))

print('długość listy:', len(numery))
print('początek:', numery[:10])
print('koniec:', numery[-10:])

# wybór losowej próbki danych
import random
print('przykładowe wartości:', random.sample(numery, 10))
