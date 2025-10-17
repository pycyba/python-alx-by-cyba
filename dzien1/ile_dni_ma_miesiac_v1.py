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

miesiac = input('Podaj nazwę miesiąca: ')
match miesiac:
    case 'styczeń': print(31)
    case 'luty': print('ten miesiąc ma 28 lub 29 dni :-)')
    case 'marzec': print(31)
    case 'kwiecień': print(30)
    case 'maj': print(31)
    case 'czerwiec': print(30)
    case 'lipiec': print(31)
    case 'sierpień': print(31)
    case 'wrzesień': print(30)
    case 'październik': print(31)
    case 'listopad': print(30)
    case 'grudzień': print(31)
