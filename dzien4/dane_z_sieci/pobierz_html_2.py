import requests

url = 'https://www.alx.pl/pl/bootcamp-python/'
response = requests.get(url)
if response.status_code == 200:
    with open('pobrane.html', mode='w', encoding='UTF-8') as wyjscie:
        wyjscie.write(response.text)
    print('Plik zapisany')
else:
    print('Kod odpowiedzi', response.status_code, ', nie zapisuję pliku')
