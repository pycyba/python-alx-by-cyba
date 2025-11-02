# To jest rozwiązanie, którego można by użyć także w językach,
# gdzie nie ma mnożenia napisu przez liczbę.
wysokosc = int(input('Podaj wysokość: '))
for i in range(wysokosc):
    for j in range(wysokosc - i):
        print(' ', end='')
    for j in range(2*i + 1):
        print('*', end='')
    print()
