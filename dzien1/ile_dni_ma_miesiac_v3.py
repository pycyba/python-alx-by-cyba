"""
Użytkownik podaje nazwę miesiąca
a program wypisuje info, ile dni ma ten miesiąc.
Jeśli poprawnie chcecie obsłużyć luty, to należy zapytać dodatkowo o rok,
a zasada ustalania roku przestępnego jest taka:
- rok jest podzielny przez 4, ale nie jest podzielny przez 100, chyba że jest podzielny przez 400
2001 - 28
2004 - 29
2100 - 28
2400 - 29
"""

miesiac = input('Podaj nazwę miesiąca: ').lower()
match miesiac:
    case 'styczeń'|'marzec'|'maj'|'lipiec'|'sierpień'|'październik'|'grudzień':
        wynik = 31
    case 'kwiecień'|'czerwiec'|'wrzesień'|'listopad':
        wynik = 30
    case 'luty':
        rok = int(input('Podaj rok: '))
        if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
            wynik = 29
        else:
            wynik = 28
    case _:
        wynik = None

if wynik is not None:   # lub po prostu if wynik:
    print(f'Miesiąc {miesiac} ma {wynik} dni.')
else:
    print('Nieznany miesiąc')
