# Python oferuje kilka modułów związanych z obsługą czasu
# time - niskopoziomowy, „systemowy” dostęp do czasu i operacje bazujące na podejściu UNIX/POSIX
# datetime - wysokopoziomowe, „obiektowe” spojrzenie na datę i czas; łatwy dostęp do pól
# calendar - operacje kalendarzowe
# zoneinfo - obsługa stref czasowych

# Tu zobaczymy dwa najważniejsze moduły.
import time

# czas wyrażony jako liczba sekund od 1 stycznia 1970 (w strefie UTC, jeśli ma to znaczenie)
t1 = time.time()
print(t1, 'typu', type(t1))
# istnieje też wersja z całkowitą liczba nanosekund
# (uwaga, system zwyle nie daje aż takiej precyzji, ale po prostu jest to skala, w jakiej wynik jest podawany)
nt1 = time.time_ns()
print(nt1, 'typu', type(nt1))

doba = 24 * 60 * 60
# sprawdzamy ile to dób i ile sekund / godzin od początku doby...
print(t1 // doba, t1 % doba, (t1 % doba) / 3600)
print('='*40)

# funkcje locatime i gmtime tworzą specjalny obiekt struct_time odpowiadający strukturze time_t z języka C (z drobnymi różnicami)
# (parametr jest opcjonalny i jeśli go nie ma, pobierany jest bieżący czas)
t1_local = time.localtime(t1)
t1_gmt = time.gmtime(t1)
print(t1_local)
print(t1_gmt)
# te obiekty mogą być przekazane do funkcji formatującej strftime
print(time.strftime('%Y-%m-%d %H:%M:%S', t1_local))
# urposzczona prezentacja dostępna jest także pod nazwą ctime
print(time.ctime(t1))
print(time.ctime())
print('='*40)

# Z datetime importujemy tylko dwie klasy.
# date - sama data
# datetime - data z czasem
from datetime import date, datetime

# Klasy `date` i `datetime` oferują wygodniejszy, bardziej obiektowy, dostęp do danych daty i czasu
# Obiekty można tworzyć na podstawie wartości pól lub pobierać bieżącą datę / czas za pomcą `.now()`
dzisiaj = date.today()
wigilia = date(2023, 12, 24)
wigilia2 = date(year=2024, month=12, day=24)
dt1 = datetime.now()

# wypisanie w domyślnym formacie
print(dzisiaj)
print(wigilia)
print(dt1)

# podejrzeć postać obiektową:
print(repr(dt1))

# odczytać poszczególne pola / atrybuty:
print('sekunda:', dt1.second)
print('dzień miesiąca:', dt1.day)
# poniedziałek na numer zero :)
print('dzień tygodnia:', dt1.weekday() + 1)
print()

# za pomocą strftime można uzyskać napis zawierający takie szczególy daty i czasu, jakie chcemy
print(dt1.strftime('%Y-%m-%d %H:%M:%S'))
print(dt1.strftime('%A, %d dzień miesiąca %B w roku %Y, godzina %H minut %M.\nDzisiaj mamy %j dzień roku.'))

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# Poprzez moduł locale możemy zmienić ustawienia regionalne tego programu
# później znaczniki %A %a %B %b będą korzystać z polskich nazw
import locale
locale.setlocale(locale.LC_TIME, 'pl_PL')
print(dt1.strftime('%A, %d dzień miesiąca %B w roku %Y, godzina %H minut %M.\nDzisiaj mamy %j dzień roku.'))
print()
print('='*40)

# sleep(sekundy) - prosty sposób na wstrzymanie programu (lub bieżącego wątku w aplikacji wielowątkowej) na jakiś czas
print('zaczynam czekać')
time.sleep(2.5)
print('skończyłem czekać')

# odejmowanie czasu wyrażonego w sekundach, ale także obiektów `datetime`, to prosty sposób na zmierzenie upływu czasu,
# np. w celu badania wydajności
t2 = time.time()
dt2 = datetime.now()
print(t2, dt2)
print('upłynęło', t2 - t1, 'czyli', dt2 - dt1)

# print('='*40)
# print('Dokumentacja klasy datetime:')
# print(datetime.__doc__)
# print('Dokumentacja metody now:')
# print(datetime.now.__doc__)
