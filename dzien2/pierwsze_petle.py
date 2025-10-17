# Pętla = wielokrotne powtarzanie fragmentów programu

for i in range(5):
    print(f'Ala ma kota nr {i}')
    print('Ola ma psa')
print("-"*50)


# W Pythonie istnieją dwa typy pętli: while i for
# while WARUNEK: INSTRUKCJE
# 1. sprawdzamy WARUNEK
# 2. jeśli fałszywy → wtedy pomijamy INSTRUKCJE i idziemy dalej
# 3. jeśli prawdziwy → wtedy wykonujemy INSTRUKCJE i ponownie wracamy do punktu 1.

x = 1
print('jestem przed pętlą while, teraz x =', x)
while x < 5:
    print('jestem w while, x =', x)
    x += 1
print('jestem ZA pętlą while, teraz x =', x)
print("-"*50)

# for zmienna in ŹRÓDŁO: INSTRUKCJE
# Dla każdego elementu znajdującego się w ŹRÓDŁO Python wykonuje:
# 1. Wpisuje do zmienna ten element (kolejny element pobrany ze ŹRÓDŁA)
# 2. Wykonuje INSTRUKCJE

lista = ['Warszawa', 'Kraków', 'Wrocław', 'Poznań']
for miasto in lista:
    print(f'Pozdrawiamy {miasto}')
print()

for i, miasto in enumerate(lista):
    print(f'Pozdrawiamy {miasto} numer {i}')
print()

# Żródłem elementów dla pętli for mogą być m.in:
# - lista, zbiór, krotka, słownik... generalnie "kolekcja"
# - otwarty plik (czytane są kolejne linie)
# - wynik zapytania SQL
# - tablica numpy, tabela Pandas
# - range - generator liczb z zakresu
# - inny generator

for kolor in 'red', 'green', 'blue':
    print(kolor)
print()

# range - generuje ciąg liczb całkowitych
# range przyjmuje maksymalnie 3 argumenty
# range(start, stop, step)
# generowane są liczby od start włącznie do stop wyłączając z krokiem step
# domyślną wartością step jest 1, domyślnym start jest 0
for i in range(10):
    print(i, end=', ')
print()

for i in range(40, 50):
    print(i, end=', ')
print()

for i in range(30, 60, 5):
    print(i, end=', ')
print()

for i in range(10, 0, -1):
    print(i, end=', ')
print()
