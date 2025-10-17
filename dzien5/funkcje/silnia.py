import sys

# aby wypisywały się mega duże silnie, zwiększamy limit cyfr
sys.set_int_max_str_digits(100_000)

# silnia to jest iloczyn kolejnych liczb naturalnych od 1 do n włącznie
# przykładowo 5!, czyli silnia(5) = 1*2*3*4*5 = 120
# dla 0 i 1 przyjmuje się, że wynik wynosi 1
def silnia(n):
    iloczyn = 1
    for i in range(2, n+1):
        iloczyn *= i # albo iloczyn = iloczyn * i
    return iloczyn


def silniaw(n):
    iloczyn = 1
    while n > 1:
        iloczyn *= n
        n -= 1
    return iloczyn


def silnia_rek(n):
    if n <= 1: return 1
    return n * silnia_rek(n-1)


while True:
    arg = int(input('Podaj argument: '))
    if arg < 0: break
    wynik = silnia(arg)
    print(f'{arg}! = {wynik}')
