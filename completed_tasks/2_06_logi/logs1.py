# w słowniku ostatni_login będziemy pamiętać czas poprzedniego logowania
# w słowniku suma_czasu będziemy pamiętać sumę czasów sesji

ostatni_login = {}
suma_czasu = {}

with open('logs.txt', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        t = linia.strip().split(';')
        # print(t)
        # user, event, time = t i potem jeszcze time = int(time)
        user = t[0]
        event = t[1]
        time = int(t[2])
        if event == 'LOGIN':
            ostatni_login[user] = time
        elif event == 'LOGOUT':
            czas_sesji = time - ostatni_login[user]
            # print(f'Użytkownik {user} wylogowuje się. Czas sesji: {czas_sesji}')
            if user in suma_czasu:
                suma_czasu[user] += czas_sesji
            else:
                suma_czasu[user] = czas_sesji

print('Sumaryczne czasy sesji:')
for user, suma in suma_czasu.items():
    print(f'{user:10} → {suma:6}s')