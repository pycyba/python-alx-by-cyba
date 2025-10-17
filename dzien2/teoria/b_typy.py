# Typy danych:
# int - liczba całkowita
x = 15
y = 20
z = -6
print(type(x), x)
print(x + y)
print(x * 2)

# W Pythonie liczby całkowite nie mają ograniczenia na wielkość,
# a obliczenia na int-ach zawsze są w pełni precyzyjne.
print(x ** y)
print()

# float - liczba z ułamkiem, "zmiennoprzecinkowa", odpowiednik double z języków C, Java (rozmiar 64-bit)
# Wewnętrznie zapisana jest w oparciu o notację wykładniczą, ale o podstawie 2, a nie 10.
f = 3.14
print(type(f), f)
# zalety: można obsługiwać zarówno bardzo duże, jak i bardzo małe wartości

# Zapis w treści programu z literą e oznacza notację wykłądniczą o podstawie 10.
f = 1.2e40  # oznacza 1.2 * (10 do potęgi 40)
print(f)

f = 1.23e-20 # 1.23 * (10 do potęgi minus 20)
print(f)

f = 3.14e2
print(f)

# Liczba znaczących cyfr jest ograniczona - float musi zmieścić się w 64 bitach pamięci
# w dodatku komputer przechowuje te dane w systemie dwójkowym
# (pamięta liczbę całkowitą pomnożoną przez 2 do jakiejś potęgi - ujemnej albo dodatniej)
# Powoduje to błędy w obliczeniach nawet dla liczb, które nam (w systemie dziesiętnym)
# wydają się proste do obsłużenia.
f = 1.2
print(3 * f)
print(3 * 1.2)

# Szczególnie groźne jest porónywanie wyników na zasadzie "musi być dokładnie równe"
if 3*f == 3.6:
    print('TAK')
else:
    print('NIE')

# problem dotyczy też innych języków programowania,
# po prostu procesory tak działają

print(f'format {3*f:.2f}')
r = round(3*f, 2)
print('round', r)
print(f"round {r:.2f}")
print(f'z większą precyzją: {r:.20f}')
print(f'z większą precyzją: {3.6:.20f}')
print(f'z większą precyzją: {1.2:.20f}')
print()


# w razie potrzeby precyzyjnych obliczeń z ułamkami (np. księgowość)
# można użyć typu Decimal - wymaga importu i odpowiedniego użycia

# Porównajmy
cena = 1.20 # float
print(3 * cena)

from decimal import Decimal
cena = Decimal('1.20')
print('Decimal:', 3 * cena)
print()

# complex - licby zespolone
# Można je tworzyć albo w notacji x+yj, albo na podstawie dwóch liczb rzeczywistych, mogą się też same pojawiać w wyniku obliczeń.
pierwiastek_z_ujemnej = (-2) ** 0.5
print(pierwiastek_z_ujemnej, 'typu', type(pierwiastek_z_ujemnej))
ju = complex(0, 1)
z = 3+2j
print(ju, z, ju+z, ju*f*z, type(z))
print()

# str - napis
# w większości innych języków nazywa się string
s = 'Ala ma kota'
t = " a Ola ma psa"
print(type(s), s)
if isinstance(s, str):
    print('Tak, to jest napis')
else:
    print('Nie, to nie jest napis')

print(s + t)
print(s * 2)
# print(s - t)
# różne działanie operatorów dla różnych typów = "przeciążanie operatorów" / "operator overloading"
# w numpy gdy mamy tablicę a
# to można napisać a * 2 i dostaniemy tablicę liczb pomnożonych przez 2

# Można wybierać pojedyncze znaki lub fragmenty:
print(s[0])
print(s[4:6]) # od włącznie do wyłączając, numeracja od zera
print()

# Po co są typy?
# Typ decyduje o tym, co można z daną wartością robić i jak działają określone operacje.
liczba = 1234
# print(liczba[0])

# można konwertować wartości między typami
napis = str(liczba)
print(napis)
print(napis[0]) # teraz OK

napis_z_liczba = '4321'
print(napis_z_liczba * 2)

# z takiego napisu można utworzyć liczbę za pomocą takiej konwersji (mówi się też "rzutowania")
x = int(napis_z_liczba)
print(x)
print(x * 2)
print()

# bool - typ dla wartości logicznych
# b = True
# b = False
b = x > 500
print(type(b), b)
if b:
    print('PRAWDA')
else:
    print('FAŁSZ')
print()

lista = [123, 456, 'Ala', 'kot']
print(type(lista), lista)
print(lista[1])
