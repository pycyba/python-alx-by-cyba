"""
Program zadaje trzy pytania:
- Podaj nazwę towaru
- Podaj cenę jednostkową (ile kosztuje jedna sztuka)
- Podaj liczbę sztuk (ile towaru kupujesz)

Program oblicza kwotę do zapłaty i wypisuje tekst tego typu:
Za 7 sztuk towaru kawa płacisz 77.70
"""

# nazwa = input('Podaj nazwę towaru: ')
# cena = float(input('Podaj cenę jednostkową: '))
# sztuk = int(input('Podaj liczbę sztuk: '))

nazwa = input('Co chcesz kupić? ')
cena = float(input(f'Ile kosztuje jedna sztuka {nazwa}? '))
sztuk = int(input(f'Ile sztuk towaru {nazwa} kupujesz? '))

do_zaplaty = cena * sztuk
print(f'Za {sztuk} sztuk towaru {nazwa} płacisz {do_zaplaty:.2f} zł')
