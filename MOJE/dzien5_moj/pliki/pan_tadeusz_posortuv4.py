print('odczyt')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()

print('filtrowanie i sortowanie')
oczyszczone = []
for linia in linie:
    linia = linia.lstrip()       # usuń spacje z lewej
    if not linia.strip():        # pomiń puste
        continue
    if linia[0] in "*-·#":       # usuń 1 znak specjalny, jeśli występuje
        linia = linia[1:]
    oczyszczone.append(linia + "\n")

linie = sorted(oczyszczone)

print('zapis')
with open('posortowany.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie)

print('gotowe')