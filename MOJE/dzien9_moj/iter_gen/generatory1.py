def nieparzyste(limit):
    current = 1
    while current <= limit:
        yield current
        current += 2


for i in nieparzyste(7):
    print(f'{i=}')

# Zaletą generatorów jest to, że wartości dostarczane są na bieżąco i nie muszą być gromadzone na raz w pamięci
print('zaczynam liczyć sumę')
suma = sum(nieparzyste(200_000_000))
print('suma liczb nieparzystych:', suma)


# to samo w oparciu o listę - jeśli macie podgląd zużycia pamięci w komputerze, to warto porównać:
print('generuję listę')
lista = list(nieparzyste(200_000_000))
# lista = list(range(1, 100_000_001, 2))
print('zaczynam liczyć sumę listy')
suma = sum(lista)
print('suma liczb nieparzystych:', suma)


