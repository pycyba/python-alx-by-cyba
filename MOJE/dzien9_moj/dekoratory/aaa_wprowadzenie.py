# Funkcja poczatek_i_koniec jest "funkcją wyższego rzędu", tzn.
# jako parameter przyjmuje i jako wynik zwraca inną funkcję.
# Operuje na funkcjach, a nie na zwykłych wartościach.

# Funkcja poczatek_i_koniec jako parametr przyjmuje pewną funkcję bezargumentową.
# W wyniku zwraca zmienioną funkcję, która działa tak jak funkcja, ale dodatkowo na początku
# i na końcu swojego działania wypisuje POCZATEK i KONIEC.
def dopisz_poczatek_i_koniec(funkcja):
    def zmieniona_funkcja():
        print('POCZATEK')
        funkcja()
        print('KONIEC')

    return zmieniona_funkcja

def powitaj():
    print('Witamy serdecznie')

def pozdrow():
    print('Na zdrowie!')


print('Normalne powitaj:')
powitaj()
print()

zmienione_powitaj = dopisz_poczatek_i_koniec(powitaj)
print('Zmienione powitaj:')
zmienione_powitaj()
print()

zmienione_pozdrow = dopisz_poczatek_i_koniec(pozdrow)
print('Zmienione pozdrów:')
zmienione_pozdrow()
zmienione_pozdrow()
print()

# Można też wywołać zmienioną funkcję bez wpisywania na zmienną:
dopisz_poczatek_i_koniec(powitaj)()
