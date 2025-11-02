# Wersja wykorzystująca wyśrodkowanie w f-string
wysokosc = int(input('Podaj wysokość: '))
szer = 2 * wysokosc + 1
for i in range(wysokosc):
    napis = '*' * (2*i + 1)
    print(f'{napis:^{szer}}')
