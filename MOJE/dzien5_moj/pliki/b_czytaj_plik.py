# Dwa główne sposoby odczytywania danych z plików tekstowych
# 1) metody
# metoda read() czyta cały plik jako jeden string
# a read(liczba_znaków) czyta podaną liczbę znaków
# istnieją też readline - czyta jedną jedną linię
# readlines - czyta wszystkie linie jako listę

with open('plik.txt', 'r', encoding='UTF-8') as wejscie:
    cala_tresc = wejscie.read()
    print('liczba znaków:', len(cala_tresc))

    # cofamy kursor na początek pliku - robię to po to,
    # aby pokazać inną funkcję wczytująca
    wejscie.seek(0)

    poczatek = wejscie.read(10)
    reszta = wejscie.readline()
    druga_linia = wejscie.readline()
    dalsze_linie = wejscie.readlines()
    print('poczatek:', poczatek)
    print('reszta:', reszta)
    print('druga_linia:', druga_linia)
    print('dalsze_linie:', dalsze_linie)
print()

# najczęściej jednak stosuje się podejście, gdzie za pomocą pętli for czyta się po jednej linii
# Odczytywane linie zawierają znaki \n
# Aby się go pozbyć, można wywołać .rstrip()

with open('plik.txt', 'r', encoding='UTF-8') as wejscie:
    for linia in wejscie:
        print('Kolejna linia:', linia.rstrip())


