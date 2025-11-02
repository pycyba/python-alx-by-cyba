from datetime import datetime

limit = 500

pocz = datetime.now()
# dla 500 czas działania 10s
# lista = [(a, b, c)
#          for a in range(1, limit+1) for b in range(1, limit+1) for c in range(1, limit+1)
#          if a < b < c and a**2 + b**2 == c**2]

# dla 500 czas ok 4s
# lista = [(a, b, c)
#          for c in range(3, limit+1) for b in range(2, c) for a in range(1, b)
#          if a**2 + b**2 == c**2]

# dla 500 czas ok 4s
# lista = [(a, b, c)
#          for a in range(1, limit-1) for b in range(a, limit) for c in range(b, limit+1)
#          if a**2 + b**2 == c**2]

# dla 500 czas ok 3s
lista = [(a, b, c)
         for a in range(1, limit-1) for b in range(a, limit) for c in range(b, limit+1)
         if a*a + b*b == c*c]
konc = datetime.now()

print('len:', len(lista))
print('Czas działania:', konc - pocz)

print(lista)

# istnieje jeszcze wersja oparta o pierwiastek. mimo, że byłaby jeszcze szybsza, to jakoś mało mi się podoba, dlatego pomijam :)
