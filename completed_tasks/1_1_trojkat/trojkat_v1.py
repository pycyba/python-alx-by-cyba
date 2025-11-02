import math

a = float(input('Podaj długość pierwszego boku: '))
b = float(input('Podaj długość drugiego boku  : '))
c = float(input('Podaj długość trzeciego boku : '))

if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'To jest poprawny trójkąt, a jego pole wynosi {pole}')
else:
    print('To nie jest poprawny trójkąt')
