# w tym przykładzie używamy biblioteki `requests`, która NIE JEST elementem biblioteki standardowej
# trzeba ją doinstalować. (jest bardzo popularna)
import requests
import re

url = 'https://www.alx.pl/pl/bootcamp-python/'
response = requests.get(url)
print(response)
print('code', response.status_code)
print('ctype:', response.headers.get('Content-Type'))

cala_tresc = response.text
# print(cala_tresc)
print(f'Tekst ma {len(cala_tresc)} znaków.')
print('Początek:', cala_tresc[:100])
print('===============')
print('Koniec:', cala_tresc[-100:])
print('===============')

for h in re.findall(r'<h2>.+</h2>', cala_tresc):
    print(h)
