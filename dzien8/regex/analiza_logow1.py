import re
import time

pattern = re.compile(r'^([^|]+)\|install\|([^|]+)\|([^|]+)\|')

with open('zypper.log', mode='r', encoding='UTF-8') as plik:
    licznik = 0
    pocz = time.time()
    for linia in plik:
        m = pattern.match(linia)
        # m = re.match(r'^([^|]+)\|install\|([^|]+)\|([^|]+)\|', linia)
        if m:
            data = m[1]
            pakiet = m[2]
            wersja = m[3]
            if 'python' in pakiet:
                print('Pakiet', pakiet, 'w wersji', wersja, 'zainstalowano w dniu', data)
                licznik += 1
    konc = time.time()
    print(licznik)
    print('czas:', konc-pocz)
