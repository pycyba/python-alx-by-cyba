from datetime import datetime

# Zapis w starym stylu, aby zrozumieć, jakie są kolejne kroki w korzystaniu z pliku w Pythonie
wyjscie = open('plik.txt', 'w', encoding='utf-8')
wyjscie.write('Pierwszy tekst')
wyjscie.writelines(['Drugi tekst'])

print('Zwykły print', file=wyjscie)
print('Kolejny print', file=wyjscie)
print('Czas modyfikacji:', datetime.now(), file=wyjscie)

# Zalecaną praktyką jest zamknięcie pliku, gdy przestajemy go używać.
# To zwalnia zasoby systemowe związane z otwartym plikiem
# i gwarantuje, że cała treść zapisywana do pliku już się w nim znalazła.
wyjscie.close()

# Zapis "nowoczesny" z użyciem `with`
#Przy okazji otwieramy plik w trybie 'a', co oznacza dopisywanie tresci na koncu pliku:
with open('plik.txt', 'a', encoding='utf-8') as output:
    print('Dopisane przez append', file=output)
    print('Dopisane przez append',datetime.now(), file=output)

#gdy wyjdzie
print('Gotowe')
