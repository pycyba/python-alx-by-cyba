"""
Program prosi o podanie dwóch rzeczy:
- napis (linia tekstu)
- liczba powtórzeń (liczba całkowita)
A następnie w kolejnych liniach wypisuje podany napis tyle razy, ile chciał użytkownik.
"""

napis = input('Podaj tekst:\n')
ile = int(input('Ile razy powtórzyć: '))
print()

# for i in range(ile):
#     print(napis)

# Jako nazwa zmiennej w pętli for może być użyte _
# Z punktu widzenia Pythona jest to normalna zmienna,
# ale używamy tego w kodzie gdy chcemy pokazać, że wartość tej zmiennej nie ma dla nas znaczenia i nie będziemy jej używać.
for _ in range(ile):
    print(napis)

# for i in range(1, ile+1):
#     print(f'{i}. {napis}')

# Ile możliwe zapisy...
# a = 0
# while a < ile:
#     print(napis)
#     a += 1

# a = 1
# while a <= ile:
#     print(a, napis)
#     a += 1
