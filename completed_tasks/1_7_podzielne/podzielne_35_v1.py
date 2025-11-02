limit = int(input('Podaj limit: '))

ile = 0
for i in range(1, limit+1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ile += 1

print('Taki liczb było', ile)
