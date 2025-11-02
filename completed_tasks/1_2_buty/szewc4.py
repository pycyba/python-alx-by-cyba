poczatek = int(input('Podaj nr dnia, kiedy buty są oddawane do naprawy: '))
czas_naprawy = int(input('Ile dni będzie trwać naprawa: '))

koniec = (poczatek + czas_naprawy - 1) % 7 + 1
# wynik mieści się w zakresie 1-7, gdzie 1 oznacza poniedziałek, a 7 niedzielę

tydzien = {
    1: 'poniedziałek',
    2: 'wtorek',
    3: 'środa',
    4: 'czwartek',
    5: 'piątek',
    6: 'sobota',
    7: 'niedziela',
}

print('Buty do odbioru w dzień nr', koniec, 'czyli', tydzien[koniec])
