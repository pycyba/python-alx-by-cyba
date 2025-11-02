poczatek = int(input('Podaj nr dnia, kiedy buty są oddawane do naprawy: '))
czas_naprawy = int(input('Ile dni będzie trwać naprawa: '))

# wynikiem będzie liczba z przedziału od 1 do 7 włącznie
koniec = (poczatek + czas_naprawy - 1) % 7 + 1
print('Buty do odbioru w dzień nr', koniec)

# Wersja z match - od Python 3.10
match koniec:
    case 1: print('To jest poniedziałek')
    case 2: print('To jest wtorek')
    case 3: print('To jest środa')
    case 4: print('To jest czwartek')
    case 5: print('To jest piątek')
    case 6: print('To jest sobota')
    case 7: print('To jest niedziela')
