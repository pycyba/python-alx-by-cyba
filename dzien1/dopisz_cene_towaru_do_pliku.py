import re
# "wyrażenia regularne"

nazwa = input('Podaj nazwę towaru: ')
cena = input(f'Podaj cenę towaru {nazwa}: ')
# weryfikacja formatu - czy podana cena ma dwie cyfry po kropce?
# obowiązkowa część całkowita, opcjonalna część ułamkowa: kropka i od jednej do dwóch cyfr
if re.fullmatch(r'[0-9]+(\.[0-9]{1,2})?', cena):
    print(f'Cena {cena} zaakceptowana')
    # dopisujemy to jako dodatkową linię do pliku ceny.txt
    with open('ceny.txt', mode='a', encoding='UTF-8') as wyjscie:
        print(nazwa, cena, sep=';', file=wyjscie)
else:
    print(f'Cena {cena} nie spełnia wymagań')

# inna wersja r'[0-9]+\.[0-9]{2}'
# obowiązkowa część całkowita i zawsze kropka i dwie cyfry
