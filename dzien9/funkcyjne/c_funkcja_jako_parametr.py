from datetime import datetime

# Do poniższej funkcji inną funkcję przekazuje się jako argument.
# Przekazana funkcja zostanie wykonana, przy czy zostanie zmierzony czas działania
def zmierz_czas_1(funkcja):
    start = datetime.now()
    funkcja()
    stop = datetime.now()
    print(f'Funkcja {funkcja.__name__} wykonała się w czasie {stop - start}')

def petla_10milionowa():
    for i in range(10_000_000):
        pass

zmierz_czas_1(petla_10milionowa)
zmierz_czas_1(lambda: [x*x for x in range(1000000)])
print(20*"=")

# Jeśli tak przekazaną funkcję chcemy uruchomić, ale z parametrami:
def zmierz_czas_2(funkcja, *args):
    start = datetime.now()
    funkcja(*args)
    stop = datetime.now()
    print(f'Funkcja {funkcja.__name__} z argumentami {args} wykonała się w czasie {stop - start}')


def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

zmierz_czas_2(fib, 35)
zmierz_czas_2(fib, 36)
print(20*"=")


# Funkcja wykonuje przekazaną funkcję f tyle razy, ile wynosi ileRazy
# Tutaj przekazywane są wszystkie argumenty: pozycyjne *args oraz z nazwami **kwargs
def powtorz(f, ileRazy, *args, **kwargs):
    for i in range(ileRazy):
        f(*args, **kwargs)

def powitaj():
    print('Witamy serdecznie')


powtorz(powitaj, 3)
print()

# następny krok: dodaj do funkcji powtórz takie elementy, aby można byo uruchamiać również funkcje z argumentami
powtorz(print, 5, 'Ala ma kota')
print()
powtorz(print, 4, 'Ala', 'Ela', 'Ola', sep=';')
# 4 razy zostanie wywołane print('Ala', 'Ela', 'Ola', sep=';')
