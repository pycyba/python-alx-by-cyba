import random

dzien_number = int(input("Podaj dzień tygodnia (1-7): "))

# Zamiana na nazwę (dla informacji, kiedy oddano)
match dzien_number:
    case 1: dzien_name = 'poniedziałek'
    case 2: dzien_name = 'wtorek'
    case 3: dzien_name = 'środa'
    case 4: dzien_name = 'czwartek'
    case 5: dzien_name = 'piątek'
    case 6: dzien_name = 'sobota'
    case 7: dzien_name = 'niedziela'
    case _:
        print("Nieznany dzień tygodnia, podaj liczbę od 1 do 7")
        exit()

print(f"Buty oddane w: {dzien_name}")

# losowy czas naprawy
czas_naprawy = random.randint(0, 14)
print(f"Czas naprawy: {czas_naprawy} dni")

# obliczamy dzień odbioru
dzien_odbioru_num = (dzien_number + czas_naprawy) % 7
if dzien_odbioru_num == 0:
    dzien_odbioru_num = 7  # bo np. (7+7) % 7 = 0 → niedziela

# zamiana numeru odbioru na słowo
match dzien_odbioru_num:
    case 1: dzien_odbioru_name = 'poniedziałek'
    case 2: dzien_odbioru_name = 'wtorek'
    case 3: dzien_odbioru_name = 'środa'
    case 4: dzien_odbioru_name = 'czwartek'
    case 5: dzien_odbioru_name = 'piątek'
    case 6: dzien_odbioru_name = 'sobota'
    case 7: dzien_odbioru_name = 'niedziela'

# liczba pełnych tygodni między oddaniem a odbiorem
tydzien = (czas_naprawy + dzien_number)// 7

if tydzien == 0:
    kiedy = "w tym tygodniu"
elif tydzien == 1:
    kiedy = "za tydzień"
else:
    kiedy = "za dwa tygodnie"

print(f" Odbiór: {dzien_odbioru_name} {kiedy}")