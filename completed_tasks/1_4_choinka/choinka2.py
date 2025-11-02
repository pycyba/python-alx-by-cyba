# Rozwiązanie wykorzystujące możliwości Pythona - mnożenie napisu przez liczbę i dodawanie napisów
wysokosc = int(input('Podaj wysokość: '))
for i in range(wysokosc):
    print(' ' * (wysokosc-i) + '*' * (2*i + 1))
