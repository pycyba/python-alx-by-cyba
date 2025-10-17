with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline()
    for numer, linia in enumerate(wejscie, 1):
        #print(linia, end='')
        pola = linia.split(';')
        #print(pola)
        print(f'{numer}.Pracownik {pola[1]} {pola[2]} zarabia {pola[4]}$')

# oblicz średnia pensje pracownikow z całego pliku

with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline()
    a = 0
    b = 0
    for _ in wejscie:
        pola = _.split(';')
        a += 1
        b += int(pola[4])
        print(f'.Pracownik {pola[1]} {pola[2]} zarabia {pola[4]}$')

    print(f"Srednie: {b / a}")

with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline()   # pomiń nagłówek
    pensje = []

    for linia in wejscie:
        pola = linia.strip().split(';')
        pensje.append(int(pola[4]))
        print(f'Pracownik {pola[1]} {pola[2]} zarabia {pola[4]}$')

    sr = sum(pensje) / len(pensje)
    print(f"Średnia pensja: {sr:.2f}$")

with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline()
    pensje = [int(linia.split(';')[4]) for linia in wejscie]

for i, p in enumerate(pensje, 1):
    print(f"Pracownik {i} zarabia {p}$")

print(f"Średnia pensja: {sum(pensje)/len(pensje):.2f}$")