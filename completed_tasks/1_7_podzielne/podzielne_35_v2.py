limit = int(input('Podaj limit: '))

liczby = [i for i in range(1, limit+1) if i % 3 == 0 or i % 5 == 0]

print('Taki liczb jest', len(liczby))
print('Wsystkie liczby:')
print(liczby)
