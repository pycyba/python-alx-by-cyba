poczatek = int(input('Podaj nr dnia, kiedy buty są oddawane do naprawy: '))
czas_naprawy = int(input('Ile dni będzie trwać naprawa: '))

koniec = poczatek + czas_naprawy
while koniec > 7:
    koniec -= 7

print('Buty do odbioru w dzień nr', koniec)

if koniec == 1: print('To jest poniedziałek')
if koniec == 2: print('To jest wtorek')
if koniec == 3: print('To jest środa')
if koniec == 4: print('To jest czwartek')
if koniec == 5: print('To jest piątek')
if koniec == 6: print('To jest sobota')
if koniec == 7: print('To jest niedziela')
