from datetime import datetime

# Zapis w starym stylu, aby zrozumieć, jakie są kolejne kroki w korzystaniu z pliku w Pythonie
wyjscie = open('plik.txt', 'w', encoding='UTF-8')
print('Otwarty plik:', wyjscie)

# Dwa sposoby dopisywania treści do pliku:
# 1) metoda write - parametrem musi być napis (w przypadku pliku tekstowego; dla binarnego byłaby to tablica bajtów - `bytes`)
#    Operacje write i writelines samodzielnie nie dopisują znaków nowej linii.
#    Jeśli chcemy, musimy sami dodać znak \n do wypisywanych stringów.
wyjscie.write('Pierwszy tekst')
wyjscie.write('Drugi tekst')
wyjscie.writelines(['Trzeci tekst', 'Czwarty tekst\n', 'Następna linia\n'])

# 2) funkcja print z dodatkowym parametrem file
print('Zwykły print', file=wyjscie)
print('Kolejny print', file=wyjscie)
print('Czas modyfikacji:', datetime.now(), file=wyjscie)

# Zalecaną praktyką jest zamknięcie pliku, gdy przestajemy go używać.
# To zwalnia zasoby systemowe związane z otwartym plikiem
# i gwarantuje, że cała treść zapisywana do pliku już się w nim znalazła.
wyjscie.close()

# Zapis "nowoczesny" z użyciem `with`
# Przy okazji otwieramy plik w trybie 'a', co oznacza dopisywanie treści na końcu pliku
with open('plik.txt', 'a', encoding='UTF-8') as output:
    print('Dopisane przez append', file=output)
    print('Ponowny odczyt czasu:', datetime.now(), file=output)


# gdy wyjdziemy z with, to plik jest automatycznie zamykany; nie pisze się już close()
print('Gotowe')

# Kwestia kodowania znaków
# W systemie Windows "oficjalnym domyślnym kodowaniem"
# jest windows-1250 (dla Windows po polsku,
# a windows-1252 dla Windows po angielsku lub niemiecku)
# i Python przyjmuje to domyślne kodowanie, jeśli nie podamy parametru.
