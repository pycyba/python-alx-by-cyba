import re

teksty = [
    'Ala Kowalska urodzona 04.11.1994',
    'Ola Malinowska urodzona 31.12.1994 w Łodzi',
    'Pan Jan Kowalski urodzony 13.04.1974 w Poznaniu',
    'Jan Maria Malinowski ur. w roku 1990',
    'Data 1.5.2005 to jest rok przed 01.05.2006',
]

# match - sprawdza, czy POCZĄTEK tekstu pasuje do wzorca
print('if match:')
for tekst in teksty:
    if re.match(r'\w+ \w+ ur(odzony|odzona|\.) [0-9]{2}\.[0-9]{2}\.[0-9]{4}', tekst):
        print('  pasuje')
    else:
        print('  nie pasuje')
print()

# Aby podnieść wydajność (w niewielkim stopniu, ale zawsze :) )
# warto wyrażenia regularne SKOMPILOWAĆ, jeśli chcemy używać go wielokrotnie, np. w pętli
pattern = re.compile(r'\w+ \w+ ur(odzony|odzona|\.) [0-9]{2}\.[0-9]{2}\.[0-9]{4}')

# Teraz zamiast pisać re.match(wzorzec, tekst), będziemy pisać pattern.match(teskt)
# To dotyczy także operacji innych niż match.
print('if pattern.match:')
for tekst in teksty:
    if pattern.match(tekst):
        print('  pasuje')
    else:
        print('  nie pasuje')
print()

# Operacje podobne w działaniu do match
# fullmatch - sprawdza, czy cały tekst idealnie pasuje do wzorca
print('if pattern.fullmatch:')
for tekst in teksty:
    if pattern.fullmatch(tekst):
        print('  pasuje')
    else:
        print('  nie pasuje')
print()

# search - sprawdza, czy wewnątrz tekstu znajduje się fragment pasujący do wzorca
print('if pattern.search:')
for tekst in teksty:
    if pattern.search(tekst):
        print('  pasuje')
    else:
        print('  nie pasuje')
print()

# Powyższe funkcje mogą zostać użyte nie tylko do sprawdzania, czy tekst pasuje do wzorca
# (True / False), ale gdy tekst pasuje, można pobrać dodatkowe informacje o dopasowaniu.
print('match wyniki:')
for nr, tekst in enumerate(teksty, 1):
    match = pattern.match(tekst)
    if match:
        print(f'Tekst nr {nr} pasuje')
        print('  match:', match)
        print(f'  Tekst znaleziony na pozycjach od {match.start()} do {match.end()}')
        print(' ', tekst[match.start():match.end()])
    else:
        print(f'Tekst nr {nr} nie pasuje, {match=}')
print()

# Przejdźmy na inny wzorzec - szukamy samego wystąpienia daty
data = re.compile(r'[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}')

for nr, tekst in enumerate(teksty, 1):
    if m := data.search(tekst):
        print(f'W tekście nr {nr} data występuje na pozycjach {m.start()}:{m.end()}')
        print(f'  Znaleziona data: {m.group()}')
        print(f'  Znaleziona data: {m[0]}')
    else:
        print(f'W tekście nr {nr} nie ma daty')
print()

# Szukanie wielu wystąpień wzorca w jednym tekście.
s = 'Lalala 11.12.2013 ble ble 30.3.2033 i jeszcze 9.10.19523 ale to już koniec'

# findall zwraca listę wszystkich znalezionych fragmentów - bardzo łatwe w użyciu
lista_dat = data.findall(s)
print(lista_dat)
# przy okazji:
# - przypominam, że wszystkie te operacje można uruchamiać z poziomu re. bez wcześniejszej kompilacji
# - \b oznacza "boundary", czyli granicę słowa
lista_dat = re.findall(r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', s)
print(lista_dat)
print()

# finditer - zwraca sekwencję obiektów Match opisujących znalezione dopasowania
# wynikiem jest 'iterator', czyli trzeba użyć pętli for do odczytu (albo funkcji next, albo zrzutować na listę...)
for m in data.finditer(s):
    print(m)
print()
for m in data.finditer(s):
    print(f'mam datę {m[0]} na pozycjach od {m.start()} do {m.end()}')
print()

# można też ewentualnie wielokrotnie uruchamiać serach podając coraz dalsze pozycje startowe
print('while:')
pos = 0
while m := data.search(s, pos):
    print(f'mam datę {m[0]} na pozycjach od {m.start()} do {m.end()}')
    pos = m.end()
print('nie ma więcej dat')
print()

# GRUPY
# W matchowanych tekstach można zaznaczyć (fragmenty) i mieć do nich łatwy dostęp.
m = re.match(r'([0-9]{2})\.([0-9]{2})\.([0-9]{4})', '12.05.1995 dalej')
print(m)
print('Cała data:', m[0])
print('Dzień:', m[1])
print('Miesiąc:', m[2])
print('Rok:', m[3])
print('Rok:', m.group())
print(m.groups())
print()

data_gr = re.compile(r'([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4})')
for m in data_gr.finditer(s):
    print(f'mam datę {m[0]}. d:{m[1]}, m:{m[2]}, r:{m[3]}')
print()

# Jeśli we wzorcu musimy użyć nawiasów w innym celu, niż tworzenie numerowanej grupy,
# to powinniśmy napisać (?:TUTAJ COŚ)
pattern2 = re.compile(r'(\w+) (\w+) ur(?:odzony|odzona|\.) (([0-9]{2})\.([0-9]{2})\.([0-9]{4}))')

for nr, tekst in enumerate(teksty, 1):
    if m := pattern2.search(tekst):
        print(f'Tekst nr {nr} pasuje. imię: {m[1]} nazwisko: {m[2]}')
        print(f'Data: {m[3]}, d:{m[4]}, m:{m[5]}, r:{m[6]}')
    else:
        print(f'Tekst nr {nr} nie pasuje')
print()


print()
# 'Walrus operator' czyli przypisanie, które jednocześnie zwraca wynik
x = 11
if x := 0:
    print('tak')
else:
    print('nie')

print(x)

