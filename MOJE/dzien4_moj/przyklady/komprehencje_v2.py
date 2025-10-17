import random

# wygeneruj listę 20 liczb losowych z zakresu od 1 do 100
liczby = [random.randint(1, 100) for _ in range(20)]
print(liczby)

# utwórz zbiór tych liczb z powyższej listy, które są podzielne przez 10
podzielne = {x for x in liczby if x % 10 == 0}
# podzielne = set(x for x in liczby if x % 10 == 0)
print('podzielne przez 10:', podzielne)

# utwórz słownik, w którym kluczami są liczby z losowej listy podzielne przez 10
# a wartościami są wyniki dzielenia przez 10
slownik = {x: x//10 for x in podzielne}
# slownik = {x: x//10 for x in liczby if x % 10 == 0}
print(slownik)
print()

# odczyt podzbioru elementów, który spełnia jakiś warunek, można też zrealizować funkcją `filter`
podzielne2 = set(filter(lambda x: x % 10 == 0, liczby))
print('podzielne przez 10 inaczej:', podzielne2)
print('#'*40 + '\n')

##############

# gdybyśmy chcieli taki słownik uzyskać od razu z randoma
slownik2 = {x: x//10 for x in (random.randint(1, 100) for _ in range(20)) if x % 10 == 0}
print(slownik2)

# ale tak w ogóle "losowe liczby podzielne przez 10" da się uzyskać wprost za pomocą randrange z krokiem równym 10
liczby3 = [random.randrange(10, 101, 10) for _ in range(10)]
print(liczby3)
print()

##############

# programowanie w stylu języka C, takie "imperatywne", czyli podstawiony wartości na okreslone pozycje
tablica = [0, 0, 0, 0, 0]
for i in range(0, 5):
    tablica[i] = random.randint(1, 100)
print(tablica)
print()
##############

