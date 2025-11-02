# Różne sposoby wypisywania danych w Pythonie:

x = 111
y = 222
wynik = x * y

print(wynik)
print(10 * x + y)

# print pozwala wypisać kilka rzeczy na raz, podczas wypisywania rozdziela je spacją
print('Wynik wynosi', wynik)

print(x, 'razy', y, 'jest równe', x * y)
print()

# Aby odstępem nie była spacja, tylko coś innego, może podać parametr sep
print('Ala','Ola',   'Ela') # rozdziela spacjami

print('Adam', 'Tomasz', 'Andrzej', sep=' oraz ') # rozdziela słowem oraz
print('Ala', 'Ola', 'Ela', 'Ula', sep=';')
print(12, 13, 14, 15, sep='')
lista = ['Toruń', 'Bydgoszcz', 'Włocławek', 'Inowrocław']
print(*lista, sep=';')
# Wypakowanie parametrów z listy (lub innej sekwecji). To jest równoważne:
print('Toruń', 'Bydgoszcz', 'Włocławek', 'Inowrocław', sep=';')
print()

# Aby print nie przechodził do nowej linii, można ustawić pusty parametr end

print('Ala ma kota', end='')
print('Ola', 'ma', 'psa', end='!')
print('Koniec')
print('Następna linia')
print()

# print(10 * '\n')

# Domyślne wartości dodatkowych parametrów print to
# sep=' ', end='\n', file=None

# Sposoby na łączenie fragmentów tekstu z wartościami ("string interpolation")

# 1) Podejście klasyczne: operator % ("modulo"). Analogia do funkcji printf z języka C:
# Bardzo popularne w Pythonie 2 i ogólnie w starych programach Pythona
print('%d razy %d jest równe %d' % (x, y, wynik))
# d jest od decimal, a inne formaty to np. x - hexcadecimal, s - string, f - float

imie = 'Alicja'
pi = 3.14159
print('%s ma %f kotów, a %d szestastkowo zapisuje się jako %x' % (imie, pi, x, x))
print()

# 2) Funkcja format - coś pośredniego między 1) a 3), mi osobiście niezbyt się podoba
print('{} razy {} jest równe {}'.format(x, y, x*y))

# można podać numery parametrów i w ten sposób zmienić kolejność, albo do tego samego odwołać się po raz kolejny
# (numeracja od 0)
print('{1} razy {0} jest równe {2} ; dla przypomnienia x = {0}'.format(x, y, x*y))

# 3) f-string, dostępne od Pythona 3.6:
print(f'{x} razy {y} jest równe {wynik}')
print(f'{x} razy {y} jest równe {x*y}')
print(f'Wartości zmiennych: {x=} {y=} {wynik=}')
print()


# dodatkowa możliwości:
# wyrównywanie do określonej liczby pozycji
imie1 = 'Ala'
imie2 = 'Ewelina'
imie3 = 'Aleksandrowska'

print(imie1, 'ma kota')
print(imie2, 'ma kota')
print()
print('%10s ma kota' % imie1)
print('%10s ma kota' % imie2)
print('%-10s ma kota' % imie2)
print('%10s ma kota' % imie3)
print()
print('{:10} ma kota'.format(imie1))
print('{0:10} ma {1:4}'.format(imie2, 'psa'))
print('{:>10} ma kota'.format(imie2))
print('{:^10} ma kota'.format(imie2))
print('{:10} ma kota'.format(imie3))
print()
print(f'{imie1:10} ma kota')
print(f'{imie2:10} ma kota')
print(f'{imie2:>10} ma kota')
print(f'{imie1:^10} ma kota')
print(f'{imie3:10} ma kota')
print()

# zaokrąglanie do określonej liczby cyfr po przecinku
import math
p = math.sqrt(2)
print('pierwiastek:', p)

print('pierwiastek: %.3f' % p)
print('pierwiastek: {:.3f}'.format(p))
print(f'pierwiastek: {p:.3f}')
print(f'pierwiastek: {p:10.6f}')

# Gdybym szerokość lub precyzję chciał wczytać ze zmiennej, to można tak:
szerokosc = 12
precyzja = 6
print(f'pierwiastek: {p:{szerokosc}.{precyzja}f}')
print()

# zera wiodące
liczba = 432
print('liczba: %05d' % liczba)
print('liczba: {:05}'.format(liczba))
print(f'liczba: {liczba:5}')
print(f'liczba: {liczba:05}')
print(f'liczba: {liczba:05d}')
print()

duza_liczba = 7**20
print(duza_liczba)
print(f'{duza_liczba:,}')
print(f'{duza_liczba:,}'.replace(',', ' '))

vat = 0.23
print(f'VAT wynosi {vat:.0%}')
oprocentowanie = 0.0752
print(f'oprocentowanie {oprocentowanie:.3%}')
