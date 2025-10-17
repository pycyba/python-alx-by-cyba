import random

dni_tygodnia = ["", "poniedziałek", "wtorek", "środą", "czwartek", "piątek", "sobota", "niedziela"]

dzien_number = int(input("Podaj dzień tygodnia (1-7): "))

if not 1 <= dzien_number <= 7:
    print("Podaj liczbe od 1 do 7")
    exit()
print(f'Buty oddane w {dni_tygodnia[dzien_number]}')
czas_naprawy = 4 #random.randint(0, 14)
print(f'Czas naprawy butow {czas_naprawy}')

dzien_odbioru_buta = (dzien_number + czas_naprawy) %7
if dzien_odbioru_buta == 0:
    dzien_odbioru_buta = 7

print(f'Dzien odbioru butow: {dni_tygodnia[dzien_odbioru_buta]}')


tydzien = (czas_naprawy + dzien_number) // 7

if tydzien == 0:
    kiedy = "w tym tygodniu"
elif tydzien == 1:
    kiedy = "za tydzień"
else:
    kiedy = "za dwa tygodnie"

print(f" Odbiór: {dni_tygodnia[dzien_odbioru_buta]} {kiedy}")
