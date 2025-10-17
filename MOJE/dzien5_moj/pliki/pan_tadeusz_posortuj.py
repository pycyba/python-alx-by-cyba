"""
Do pliku posrotowany.txt zapisz wszystkie linie ptposortowane alfabateycznie.
Dla chetnych
Pomijaj puste linie oraz usuwawaj wciecia lewej strony.

"""

zbior = set()

with open('pan_tadeusz.txt', 'r', encoding='UTF-8') as wejscie:
    with open('posortowane.txt', 'w', encoding='UTF-8') as wyjscie:
        for i in wejscie:
            linia = i.strip()       # usuń spacje i \n
            if linia:               # pomiń puste
                zbior.add(linia)

        for linia in sorted(zbior):
            print(linia, file=wyjscie)
