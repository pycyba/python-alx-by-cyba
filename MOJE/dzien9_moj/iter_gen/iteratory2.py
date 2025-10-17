# Każdą rzecz, którą do tej pory przekazywaliśmy do pętli for, można traktować w ten sposób bezposrednio używając operacji iter i next

lista = ['Ala', 'Ela', 'Ola']
print(lista)
print('Normalny for:')
for x in lista:
    print('*', x)
print()

# Gdy w Pythonie uruchamiamy pętlę for, to Python wewnętrze realizuje to w ten sposób...

print('Pętla iter / next:')
it = iter(lista)
print('Uzyskałem iterator:', it)
try:
    while True:
        el = next(it)
        print('-', el)
except StopIteration:
    print('Koniec elementów')

# Czasami obiekt iterowalny jest jednocześnie iteratorem - przykładem są otwarte pliki.
