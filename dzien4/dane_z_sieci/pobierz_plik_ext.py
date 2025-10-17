'''
W miarę uniwersalny program do pobierania plików z sieci. Wystarczy poddć URL, a program pobierze dane i zapisze plik,
dobierając przy tym rozszerzenie na podstawie typu MIME.
'''

import requests

def rozszerzenie_pliku(content_type:str):
    import re

    if ';' in content_type or '+' in content_type:
        content_type = re.split(r'[;+]', content_type)[0]

    match content_type:
        case 'text/plain': return 'txt'
        case 'text/html': return 'html'
        case 'text/csv': return 'csv'
        case 'application/xml': return 'xml'
        case 'application/json': return 'json'
        case 'application/pdf': return 'pdf'
        case 'application/zip': return 'zip'
        case 'image/jpeg': return 'jpg'
        case 'image/png': return 'png'
        case _: return 'data'


def main():
    print('Aby zakończyć, podaj pusty adres...')
    while True:
        adres = input('Podaj URL: ')
        if not adres: break
        try:
            response = requests.get(adres)
            print('Uzyskana odpowiedź:', response)
            print('Kod odpowiedzi:', response.status_code)
            content_type = response.headers.get('Content-Type')
            print('Format danych:', content_type)
            if response.status_code != 200:
                continue
            nazwa = input('Podaj nazwę pliku (bez rozszerzenia): ')
            nazwa += '.' + rozszerzenie_pliku(content_type)
            with open(nazwa, mode='wb') as plik:
                plik.write(response.content)
        except Exception as e:
            print('Błąd:', e)

    print('Koniec programu')


if __name__ == '__main__':
    main()
