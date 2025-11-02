# W jednym miejscu zapisuję nazwy i ceny prac, ale w dalszej części programu i tak będę w różny sposób obliczał faktyczny koszt - wzory się różnią.
# Wyciągnięcie tych danych do oddzielnej definicji ma tylko ułatwić ewentualną zmianę cen.
# Struktura słownika:  krótki_klucz: (opis, cena)
cennik = {
    'gip': ('gipsowanie ścian', 100),
    'mal': ('malowanie ścian i sufitów', 30),
    'pan': ('panele podłogowe', 50),
    'lis': ('listwy podłogowe', 40),
}

def pytanie_o_prace(opis: str, koszt: float) -> float:
    wybor = input(f'Czy chcesz wykonać pracę "{opis}", której koszt wynosi {koszt:.2f} zł?\nT / N: ').strip().upper()
    return koszt if wybor == 'T' else 0

def main():
    print('Podaj wymiary pomieszczenia w metrach (np. 3.75 )')
    a = float(input('długość  : '))
    b = float(input('szerokość: '))
    h = float(input('wysokość : '))
    obwod = 2*a + 2*b
    pow_podlogi = a*b
    pow_scian = obwod*h

    suma = 0
    suma += pytanie_o_prace(cennik["gip"][0], cennik["gip"][1] * pow_scian)
    suma += pytanie_o_prace(cennik["mal"][0], cennik["mal"][1] * (pow_scian + pow_podlogi))
    suma += pytanie_o_prace(cennik["pan"][0], cennik["pan"][1] * pow_podlogi)
    suma += pytanie_o_prace(cennik["lis"][0], cennik["lis"][1] * obwod)
    print(f'Łączny koszt prac wyniesie {suma:.2f} zł')

if __name__ == '__main__':
    main()
