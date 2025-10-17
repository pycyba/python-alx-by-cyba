# To jest komentarz, można sobie pisać bzdury
imie = input('Jak masz na imię? ')
print('Witaj', imie)

# Dopisz pytanie o nazwę miasta (np 'Skąd jesteś?')
# i wypisz 'Pozdrowienia dla ...'
miasto = input('Skąd jesteś?\n')
print('Pozdrowienia dla miasta', miasto)

# Python potraktuje ciąg znaków wpisany przez użytkownika jako liczbę.
wiek = int(input('Ile masz lat? '))
print('Masz', wiek, 'lat, czyli urodziłe|aś się w roku', 2025-wiek)

if wiek >= 18:
    print('Jesteś osobą pełnoletnią')
    print('Możesz kupić piwo czy co tak chcesz...')
else:
    print('Jesteś osobą niepełnoletnią')
    print('a kuku')

print('Koniec programu')
