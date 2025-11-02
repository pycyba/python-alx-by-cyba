# Jeszcze jedna wersja, aby pokazać względnie nową możliwość Pythona: przypisanie := , działające jako wyrażenie, do użycia w if lub while.
# ("assignment expression" / "named expression" / "walrus operator")
# Tak działa każde przypisanie w językach C, C++, C#, Java i od dawna toczyła się dyskusja, czy w Pythonie przypisanie też tak powinno działać.
# Ostatecznie w Pythonie 3.8 to wprowadzono, ale jako nowy operator, a działanie zwykłego = pozostało bez zmian.

from collections import defaultdict
import re

pattern_login = re.compile(r'(.+);LOGIN;(\d+)')
pattern_logout = re.compile(r'(.+);LOGOUT;(\d+)')

suma_czasow = defaultdict(int)

with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for line in plik:
        if match_login := pattern_login.match(line):
            username = match_login[1]
            time = int(match_login[2])
            print(f'LOGIN  kto: {username} , czas: {time}')
            suma_czasow[username] -= time
        elif match_logout := pattern_logout.match(line):
            username = match_logout[1]
            time = int(match_logout[2])
            print(f'LOGOUT kto: {username} , czas: {time}')
            suma_czasow[username] += time

print()
for k, v in suma_czasow.items():
    print(f'Suma sesji {k:8}: {v:6} s')
