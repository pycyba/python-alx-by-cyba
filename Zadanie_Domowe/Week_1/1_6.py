import random

x = random.randint(1, 20)   # pierwsza wylosowana liczba
y = random.randint(1, 20)   # druga wylosowana liczba
wynik_mnozenia = x * y
proba = 0
liczba = None   # na start None, bo jeszcze nie zgadywaliśmy

while liczba != wynik_mnozenia:
    liczba = int(input(f"Ile to jest {x} * {y}? "))
    proba += 1

    if liczba == wynik_mnozenia:
         print(f"Brawo! Udało się za {proba} próba!")
    else:
        print("spróbuj jeszcze raz.")