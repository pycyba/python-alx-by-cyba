N = 100_000_000

print('Liczę sumę za pomocą generatora...')
suma1 = sum((x*x for x in range(N)))
print('suma1:', suma1)


print('Liczę sumę za pomocą listy...')
suma2 = sum([x*x for x in range(N)])
print('suma2:', suma2)

