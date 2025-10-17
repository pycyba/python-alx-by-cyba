print('Początek programu')
while True:
    x = int(input('Podaj liczbę: '))
    print('Podana liczba:', x)
    if x % 3 == 0:
        print('Liczba jest podzielna przez 3, robię continue')
        continue
    print('Nie było podzielności przez 3')
    if x % 5 == 0:
        print('Liczba jest podzielna przez 5, robię break')
        break
    print('Nie było podzielności przez 5')
    print('Ładna pogodna')

print('Jestem już za pętlą')
print('Koniec programu')
