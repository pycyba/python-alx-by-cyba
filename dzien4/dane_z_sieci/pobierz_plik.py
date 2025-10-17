import requests

while True:
    url = input('Podaj adres (lub puste, aby zakończyć):\n')
    if not url:
        break
    try:
        response = requests.get(url)
        print('Kod odpowiedzi:', response.status_code)
        if response.status_code == 200:
            plik = input('Podaj nazwę pliku: ')
            # plik otwieram jako 'binarny', czyli ciąg bajtów, a nie fragment tekstu
            with open(plik, mode='wb') as wyjscie:
                wyjscie.write(response.content)
    except Exception as e:
        print('Problem', e)
