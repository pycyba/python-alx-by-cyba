N = 100_000_000

print('Licze sume za pomocą generatora...')

suma1 = sum(x*x for x in range(N))
print(f'Suma1: {suma1}')

print('Licze sume za pomocą listy...')
suma2 = sum([x*x for x in range(N)])
print(f'Suma1: {suma2}')

