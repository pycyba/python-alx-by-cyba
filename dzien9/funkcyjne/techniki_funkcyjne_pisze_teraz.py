from datetime import datetime
import math

def do_kwadratu(x):
    return x ** 2

def do_trzeciej(x):
    return x ** 3


# Funkcję można nie tylko wywołać:
wynik = do_kwadratu(5)
print(wynik)

# Funkcję można też "wskazać", można traktować jak wartość - zapisać do zmiennej, zapisać do listy albo słownika,
# przekazać jako parametr do innej funkcji...
# W tym przypadku używamy nazwy funkcji bez dopisywania (nawiasów)
print(do_kwadratu, do_trzeciej)
funkcja = do_kwadratu
print('Funkcja to jest:', funkcja)

# Gdy w zmiennej znajduje się funkcja, to można użyć tej zmiennej w celu uruchomienia
wynik = funkcja(6)
print(wynik)

funkcja = math.sqrt
print('Teraz funkcja to jest:', funkcja)
wynik = funkcja(16)
print(wynik)
print()

liczby = [0, 1, 2, 9, 16, 50]
funkcje = [do_kwadratu, do_trzeciej, math.sqrt, math.exp, lambda x: 10*x]

for f in funkcje:
    for x in liczby:
        y = f(x)
        print(f'{f.__name__}({x}) = {y}')

print()
# Funkcja może być parametrem innej funkcji,
# może być też wynikiem funkcji.
# Na funkcje, które przyjmują inne funkcje jako parametry, mówi się "funkcje wyższego rzędu".

def powtorz(procedura, ile_razy=1):
    for _ in range(ile_razy):
        procedura()

def witaj():
    print('Witaj człowieku')

def wierszyk():
    print('aaa, kotki dwa')
    print('szare-bure obydwa')

powtorz(witaj, 5)
powtorz(wierszyk, 3)
print()

# Wyrażenie lambda to skrócony sposób definiowania funkcji.
# Funkcja nie ma oficjalnej nazwy (jako nazwa zawsze wpisane jest '<lambda>')
plus1 = lambda x: x+1
wynik = plus1(10)
print(wynik)

# Wyrażeń lambda używa się najczęściej, gdy funkcję musimy przekazać jako parametr do innej funkcji.
powtorz(lambda: print(f'jestem lambdą z godziny {datetime.now()}'), 5)
print()

# Przykładem zastosowania lambdy jest przekazywanie funkcji key do sortowania
lista = ['A.Kowalska', 'K.Kwiatkowski', 'Z.Anioł', 'B.Nowakowska', 'C.Rak', 'O.Kawa']
print(lista)
print(sorted(lista))
# sorted układa napisy według kolejności wynikającej z wyników funkcji len
print(sorted(lista, key=len))
print(sorted(len(s) for s in lista))

# Gdy chcemy użyć niestandardowego sposobu sortowania, którego nie opisuje żadna istniejąca funkcja,
# do parametru key przekazujemy napisaną przez siebie lambdę
# spróbuj posortować te napisy alfabetycznie wg nazwisk (nie musi być pl_PL)
print(sorted(lista, key=lambda s: s[2:]))
s = 'A.Kowalska'
print(s[2:])

# inny sposób
print(sorted(lista, key=lambda s: s.split('.')[1]))
