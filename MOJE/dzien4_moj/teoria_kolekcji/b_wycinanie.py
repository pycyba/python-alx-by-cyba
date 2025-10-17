# Python posiada składnię "slices" ("wycinanki"),
# która pozwala w bardzo wygodny sposób wybierać fragmenty list (i innych sekwencji)

l = ['zero', 'jeden', 'dwa', 'trzy', 'cztery',
     'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
print(l)
print('len =', len(l))
print()

# Można wybierać pojedyncze elementy
print('l[0]', l[0])
print('l[3]', l[3])
print('l[9]', l[9])
# print(l[10]) # IndexError: list index out of range

# liczenie od końca
print('l[-3]', l[-3])
# ostatni
print('l[-1]', l[-1])
print('l[-1]', l[len(l)-1])
# Ujemny też może wyjść poza zakres
#ERR print('l[-15]', l[-15])
print()

# Notacją z dwukropkami wybiera się przedziały / fragmenty list

print('l[3:7]', l[3:7]) # pozycje od 3 do 6
# gdy mówimy o zakresach, to zawsze jest to zakres od lewej granicy włącznie, do prawej wyłączając
# (lewostronnie domknięty)
# przy czym numerujemy od zera
# inne spojrzenie: pomijamy 3 elementy, a następnie pobieramy 4 kolejne

# odwołanie do pojedynczego elementu poza zakresem kończy się błędem IndexError
# print(l[20])

# wyjście poza listę w przypadku zakresu nie powoduje błędu - po prostu dostajemy krótszy fragment, czasami wręcz pusty
print('l[5:25]',  l[5:25])
print('l[20:25]', l[20:25])

# W zakresach można podawać indeksy ujemne, które zostaną odpowiednio przeliczone
print('l[-8:-6]', l[-8:-6])
print('l[2:6]', l[2:6])
print('l[-8:6]',  l[-8:6])
print('l[8:3]',  l[8:3])
print()

# trzeci parametr składni "przedziałowej" / "slices" oznacza wielkość kroku
# (domyślnie krok = 1)
# czyli ogólnie mamy [start:stop:step]

print('l[2:10:2]', l[2:10:2])
print('l[0:10:3]', l[0:10:3])
# Przy tym podejściu drugi parametr jest traktowany tak, że zostaną odczytane elementy o indeksach mniejszych niż ten parametr
print('l[1:5:3]', l[1:5:3]) # 4 < 5, więc 4 się wyświetli
print('l[1:6:3]', l[1:6:3])
print('l[1:7:3]', l[1:7:3]) # nieprawda, że 7 < 7, więc 7 się nie wyświetli
print('l[1:8:3]', l[1:8:3]) # 7 < 8, więc 7 się wyświetli
print()
# to jest analogia do takiej pętli:
i = 1
while i < 8:
     print(l[i], end=',')
     i += 3
print('!\n')

# Niektóre parametry można pominąć.
# Domyślnie start=0, stop=len, step=1
# (gdy step jest ujemny, to start i stop zamieniają się znaczeniem)

print('l[::2]', l[::2]) # wypisz wszystkie pozycje parzyste

# 3 pierwsze elementy
print('l[:3]', l[:3])
print('l[:3:]', l[:3:]) # równoważne powyższemu

# od 3 do końca
print('l[3:]', l[3:])

# 3 ostatnie elementy
print('l[-3:]', l[-3:])
print()

# obejmuje całe listy
print('l[:]', l[:])
print('l[::]', l[::])
print()

# Gdy krok jest ujemny, to przeglądamy elementy w odwrotnej kolejności
print('l[8:2:-2]', l[8:2:-2]) # 8 6 4

# Najprostszy sposób na odwrócenie listy:
print('l[::-1]', l[::-1])
print()

# Napisy (str) też są "sekwencjami" i można do nich stosować indeksowanie i wycinanie
tekst = 'Ala ma kota a Ola ma psa'
print(tekst[2])
print(tekst[-2])
print()

# spróbujcie wyciąć słowo "kota"
print(tekst[7:11])

print(tekst[::2])

print(tekst)
# od tyłu:
print(tekst[::-1])

print('\n' + 60*'=' + '\n')

lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Katowice', 'Białystok', 'Toruń', 'Bydgoszcz']
print(lista)

# do wstawiania elementów można też użyć zakresów:
print(lista[5])

print(lista[5:5])

# działa tak jak insert(5, 'Trójmiasto')
lista[5:5] = ['Trójmiasto']
print(lista)

# Uwaga, inaczej zadziałałoby:
# lista[5] = ['Trójmiasto']
# print(lista)

print(lista[5:6]) # ['Trójmiasto']
# zastąp wycinek o długości jeden tymi trzema elementami
# zastępuje Trójmiasto tymi trzema miastami
lista[5:6] = ['Gdańsk', 'Sopot', 'Gdynia']
# trzy_miasta = ['Gdańsk', 'Sopot', 'Gdynia']
# lista[5:6] = trzy_miasta
print(lista)
print(lista[5:8])
lista[5:8] = ['GDAŃSK', 'WRZESZCZ', 'OLIWA', 'SOPOT', 'GDYNIA']
print(lista)

# Usunie elementy WRZESZCZ i OLIWA
lista[6:8] = []
print(lista)

# Można też deletować zakresy:
del lista[1:4]
print(lista)

# str jest "niemutowalny" (immutable), więc zakresy są tylko do odczytu
#txt = 'ABCDEF'
#ERR txt[1:2] = 'XY'

lista = ['A', 'B', 'C', 'D', 'E']
lista[0:4:2] = [1, 2]
print(lista)
