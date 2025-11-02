# W Pythonie mamy pisane słownie spójniki logiczne `and` `or` i `not`
# Mamy także operatory zapisywane symbolicznie `&` `|` `^` (daszek to nie jest not, jbc)

# Na pierwszy rzut oka wydaje się, ze działają tak samo
print('and', '&')
print(True and True, True & True)
print(True and False, True & False)
print(1 and 0, 1 & 0)

# Ale są różnice

# 1) Operatory & i | zastosowane do liczb stają się operacjami na bitach
print(5 and 2, 5 & 2)
# 5 and 2 daje wynik 2, bo 5 jest traktowane jak prawda i wtedy and zwraca to, co widzi po prawej stronie
# liczby w systemie dwójkowym: 5 → 0101 , 2 → 0010
# gdy na każdej pozycji zastosujemy & do tych zer i jedynek, to na końcu będą same zera
x = 2
y = 5
if x and y:
    print('pierwsza prawda')
else:
    print('pierwsza nieprawda')

if x & y:
    print('druga prawda')
else:
    print('druga nieprawda')

# 2) and pisany słownie ma niską siłą wiązania, a & pisany znaczniem ma wysoką siłę wiązania (nawiasowania)
#    W połączeniu z faktem nr 1 powoduje to, że bardzo łatwo popełnić taki błąd jak w "czwarta nieprawda":
# struktura jest taka: (x >= 2) and (y == 5)
if x >= 2 and y == 5:
    print('trzecia prawda')
else:
    print('trzecia nieprawda')

# Python najpierw obliczy (2 & y), a y jest równy 5, więc wynikiem jest 0, co widzieliśmy wcześniej
# a później sprawdzi warunek x >= 0 == 5, co jest oczywiście nieprawda
# struktura jest taka x >= (2 & y) == 5
if x >= 2 & y == 5:
    print('czwarta prawda')
else:
    print('czwarta nieprawda')

if (x >= 2) & (y == 5):
    print('piąta prawda')
else:
    print('piąta nieprawda')

print()
# 3) and i or pisane słownie są "leniwe", a & i | pisane znaczkowo są "gorliwe"
# Jeśli po sprawdzeniu lewej strony warunku od razu widać, że wynik całego anda będzie fałszywy (analogicznie: wybik ora będzie prawdziwe)
# to Python nie będzie już sprawdzał prawej strony

# Przykład: ryzyko dzielenia przez zero
x = 100
y = 5
# y = 0
# porawnie napisany kod:  gdyby y był równy 0, to Python nie sprawdzi prawej części warunku, a więc nie wykona dzielenia
if y != 0 and x / y >= 10:
    print('and OK')
else:
    print('and nieOK')

# niepoprawnie napisany kod: gdy y będzie równy 0 (możesz sprawdzić zmieniając na chwilę wartość zmiennej)
# to Python i tak wykona dzielenie zapisane po prawej i będzie błąd
if (y != 0) & (x / y >= 10):
    print('& OK')
else:
    print('& nieOK')

# W Pythonie nie tylko wartości True i False typu bool niosą w sobie wartość logiczną,
# ale także wartości innych typów. Mogą one być umieszczone w if (albo while),
# mogą być umieszczanie w spójnikach logicznych and i or.

liczba0 = 0
liczba1 = 1
liczba2 = -3.14

napis0 = ''
napis1 = 'Ala ma kota'
napis2 = '    '

lista0 = []
lista1 = ['Adam', 'Ludwik', 'Xawery']

if liczba0: print('liczba0 true')
else: print('liczba0 false')

if napis0: print('napis0 true')
else: print('napis0 false')

if napis2: print('napis2 true')
else: print('napis2 false')

print()

# Gdy używamy spójników logicznych and or , to wynikiem jest jeden z przekazanych argumentów (a niekoniczenie wartość True / False)
# and: jeśli jedna z wartości jest fałszywa, to and zwraca pierwszą z takich wartości
#      jeśli wszystkie są prawdą, to and zwraca ostatnią rzecz po prawej stronie
print('and:', liczba1 and liczba0)
print('and:', napis1 and lista1)
print('and:', True   and True)
print('and:', lista1 and liczba0 and liczba1 and liczba2)
print('and:', True   and False   and True    and True)
print('and:', lista1 and napis1 and liczba1 and liczba2)

# or: jeśli jedna z wartości jest prawdą, to or zwraca pierwszą z takich wartości
#     jeśli wszystkie są fałszem, to or zwraca ostatnią rzecz po prawej stronie
print('or:', liczba0 or liczba1 or liczba2)
print('or:', liczba0 or napis0 or liczba2)
print('or:', liczba0 or napis0 or lista0)

