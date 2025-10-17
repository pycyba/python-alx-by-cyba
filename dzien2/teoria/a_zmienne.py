# W Pythonie próba odczytania niezdefiniowanej zmiennej jest błędem:
# print(zmienna) # błąd

# Zmienne są tworzone w ten sposób, że pod jakąś nazwę wpisuje się wartość
# Operatorem przypisania (assignment) jest pojedynczy znak równości =
imie = 'Ala'
liczba = 15
x = 2*liczba
pi = 3.14

# Teraz te zmienne już istnieją
print(imie, liczba, pi)
print('x = ', x)

# Do zmiennej można wpisać inną wartość
imie = 'Alicja'
liczba = 100
print(imie, liczba)
print('x = ', x) # nadal 30

# Można ustalić nową wartość zmiennej na podstawie starej wartości
liczba = liczba * 2
print(liczba) # 200

# "Rozszerzone operatory przypisania" pozwalają zwięźle zapisać zmianę wartości względem poprzedniej
# Aby ich użyć, zmienna musi już wcześniej istnieć
liczba += 5 # jak liczba = liczba + 5
print(liczba) # 205
# istnieją też += -= *= /= //= %= **= ^= &= |=

# W Pythonie nie ma operatorów inkrementacji ++x i x++
# liczba++

# Niektóre nazwy są zabronione - słowa kluczowe języka (keyword)
# if = 'yes'
# yield = True
# interpreter pozwoli za to nadpisać nazwę funkcji globalnej, np.
# print = 'hahaha'
max = 123
# ale wtedy może nie działać dalsza część programu

# Do sprawdzenia typu można użyć operacji type:
print('Zmienna liczba ma teraz wartosc', liczba, 'typu', type(liczba))

# O ile w Javie lub C takie rzeczy by nie przeszły,
# to w Pythonie do istniejącej zmiennej można wpisać wartość innego typu niż była wcześniej.
liczba = 'Ala ma kota'
print(liczba)

# Więc mówiąc precyzyjnym językiem:
# To nie zmienne mają typ, tylko wartości mają typ, a do zmiennych wpisywane są różne wartości.
print('Zmienna liczba ma teraz wartosc', liczba, 'typu', type(liczba))

# Nie trzeba tego robić i zazwyczaj się nie robi,
# ale istnieje instrukcja del, która usuwa zmienne.
del liczba
# print(liczba) # błąd

# Wbudowane funkcje globals() i locals() pozwalają "zobaczyć" wszystkie zmienne
# (w formie słownika, z podziałem na globalne i lokalne - o tym wszystkim będzie później)
print(globals())
