poczatek = int(input('Podaj nr dnia, kiedy buty są oddawane do naprawy: '))
czas_naprawy = int(input('Ile dni będzie trwać naprawa: '))

koniec = (poczatek + czas_naprawy) % 7
# wynik mieści się w zakresie 0-6, gdzie 0 oznacza niedzielę

tydzien = ['niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota']

print('Buty do odbioru w dzień nr', koniec, 'czyli', tydzien[koniec])
