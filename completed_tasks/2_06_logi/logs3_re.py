# Wersja podobna do v3, ale używająca wyrażeń regularnych do analizy linii pliku.

from collections import defaultdict
import re

pattern_login = re.compile(r'(.+);LOGIN;(\d+)')
pattern_logout = re.compile(r'(.+);LOGOUT;(\d+)')

suma_czasow = defaultdict(int)

with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for line in plik:
        match_login = pattern_login.match(line)
        match_logout = pattern_logout.match(line)
        if match_login:
            username = match_login[1]
            time = int(match_login[2])
            print(f'LOGIN  kto: {username} , czas: {time}')
            suma_czasow[username] -= time
        elif match_logout:
            username = match_logout[1]
            time = int(match_logout[2])
            print(f'LOGOUT kto: {username} , czas: {time}')
            suma_czasow[username] += time

print()
for k, v in suma_czasow.items():
    print(f'Suma sesji {k:8}: {v:6} s')
