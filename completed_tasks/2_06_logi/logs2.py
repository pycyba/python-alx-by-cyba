# W tej wersji wszystko liczymy od razu w jednym słowniku
# z tym że czasy LOGIN zapisujemy ze znakiem ujemnym
# Tymczasowo w słowniku będzie liczba ujemna, ale gdy dodamy czas LOGOUT, to pozostanie na końcu różnica między nimi
# (czas_logout1 - czas_login1) + (czas_logout2 - czas_login2)
# ↓↓↓
# -czas_login1 + czas_logout1 -czas_login2 + czas_logout2

# Dodatkowe uproszczenie: defaultdict zamiast zwykłego słownika
from collections import defaultdict
suma_czasu = defaultdict(int)

with open('logs.txt', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        t = linia.strip().split(';')
        user, event, time = t
        time = int(time)
        if event == 'LOGIN':
            suma_czasu[user] -= time
        elif event == 'LOGOUT':
            suma_czasu[user] += time

print('Sumaryczne czasy sesji:')
for user, suma in suma_czasu.items():
    print(f'{user:10} → {suma:6}s')
