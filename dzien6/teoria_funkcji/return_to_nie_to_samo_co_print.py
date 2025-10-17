def aaa(x):
    print(x*x)


def bbb(x):
    return x*x


print('Wersja błędna:')
x = int(input('Podaj liczbę: '))
print(x, 'do kwadratu to jest', aaa(x))

print('\n\nWersja poprawna:')

x = int(input('Podaj liczbę: '))
print(x, 'do kwadratu to jest', bbb(x))

