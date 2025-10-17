print('Początek programu')

def funkcja():
    print('Jestem w funkcji')
    print('lalala')
    print('Koniec funkcji')

print('Funkcja została zdefiniowana:', funkcja)
print('Zaraz uruchomię funkcję...')
funkcja()
print("=========")
funkcja()
print()

# Funkcja może otrzymywać parametry
def wykonaj_wiele_razy(n):
    print('parametr n =', n)
    for _ in range(n):
        funkcja()
    print('Koniec powtarzania')

wykonaj_wiele_razy(3)
print()

# Funkcja może zwrócić wynik
# W treści funkcji występuje instrukcja return, która mówi, co ma być wynikiem, i kończy działanie funkcji
# Wywołując funkcję możemy potraktować ją jak wartość, którą np. zapiszemy do zmiennej
def powitanie(imie):
    #tu nie ma print!!!!!!!!!!
    return f'Hello {imie}'

wynik = powitanie('Ala')
print('Funkcja powitanie została wykonana')
print('Wynikiem tej funkcji jest:', wynik)

print('Inne powitanie:', powitanie('Ola'))

# Samo wywołanie funkcji nie powoduje wypisania wyniku
powitanie('Patryk')

# Najlepszym przykładem funkcji, która zwraca wynik, jest funkcja matematyczna
def do_kwadratu(x):
    return x*x

wynik = do_kwadratu(5)
print('5 ^ 2 =', wynik)

print()
print('Koniec programu')
