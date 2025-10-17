import random

x = random.randint(1, 1000)   # wylosowana liczba
y = 0                         # liczba podana przez gracza
proba = 0                     # licznik prób
#print(x) # Test, tez mozna przez pydebugera shift f9 i pozniej alt f8
while x != y:
    y = int(input("Podaj liczbę: "))
    proba += 1
    if y == x:
        print(f" Gratulacje, zgadłeś {x} za {proba} próbą!")
    elif y < x:
        print(f"Twoja {y} jest za mała")
    else:
        print(f"Twoja {y} jest za duża")