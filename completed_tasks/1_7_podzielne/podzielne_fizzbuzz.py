'''
Inna wersja, "FizzBuzz":
Program wypisuje liczby z zakresu od 1 do limit (podany przez użytkownika)
ale gdy liczba jest podzielna przez 3, to zamiast niej wypisuje słowo Fizz
gdy liczba jest podzielna przez 5, to zamiast tej liczby słowo Buzz
a gdy liczba jest podzielna jednocześnie przez 3 i przez 5, to wypisuje FizzBuzz
'''

limit = int(input('Podaj limit: '))
for i in range(1, limit+1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
