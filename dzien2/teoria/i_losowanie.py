import random

# pobranie (pseudo)losowej liczby rzeczywistej z zakresu od 0 do 1:
x = random.random()
print(x)

# jeśli chodzi o liczby całkowite, to do wyboru mamy dwie funkcje:
# 1) randint(a, b) - zwraca liczbę z zakresu między a i b włącznie
# (zarówno a, jak i b, też mogą pojawić się jako wynik)
# każda liczba z tego zakresu z równym prawdopodobieństwem
y = random.randint(10, 20)
print(y)

# 2) randrange(a, b) - zwraca liczbę z zakresu od a włącznie do b wyłączając
z = random.randrange(110, 120)
print(z)

# randrange posiada inne formy uruchomienia: od 1 do 3 parametrów,
# których znaczenie jest takie samo jak w generatorze `range`
# np. randrange(10) zwraca liczby od 0 do 9

# Jedna z pełnych "setek" między 1000 włącznie a 2000 wyłączając
z = random.randrange(1000, 2000, 100)
print(z)

# wybór wartości z listy
kolory = ['czerwony', 'zielony', 'niebieski', 'żółty', 'purpurowy']

# wybór jednej z wartości z równym prawdop.
print(random.choice(kolory))

# wybór wielu wartości:
# z możliwością powtórzenia (wielokrotne losowanie z pełnego zbioru)
print(random.choices(kolory, k=3))
# z wagami dla podanych pozycji; żółty nie ma prawa się pojawić
print(random.choices(kolory, weights=[5, 2, 2, 0, 1], k=3))

# wybór bez możliwości powtórzenia (wybór podzbioru)
print(random.sample(kolory, k=3))
