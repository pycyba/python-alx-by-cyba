# Utworzenie zmiennej (instrukcja przypisania / assign)
zmienna = 'wartość'
x = 100
# teraz można odczytać wartość zmiennej
print(zmienna, x)

# program może zmienić wartość zmiennej
zmienna = 'inna wartość'
x += 5 # działa tak samo jak x = x + 5
print(zmienna, x)

# nie wolno odczytywać zmiennej, która nie istnieje / nie została wcześniej utworzona
#ERR print(y)
#print('dalszy etap')
print()

a = 123
print(a, 'typu', type(a))
f = 123.45
print(f, 'typu', type(f))
s = 'Ala'
print(s, 'typu', type(s))

miasta = ['Warszawa', 'Kraków', 'Wrocław']
print(miasta, 'typu', type(miasta))
