"""

Write a program that calculates the average temperature for a given
week based on temperatures entered by
the user.

"""
suma = 0.0
n = 0

while n < 7:  # maksymalnie 7 dni
    s = input(f"Podaj temperaturę dnia {n+1} (Enter aby zakończyć wcześniej): ").strip()
    if s == '':
        break
    try:
        temp = float(s.replace(',', '.'))
    except ValueError:
        print("Błąd: podaj liczbę.")
        continue
    suma += temp
    n += 1

if n == 0:
    print("Brak danych – nie można obliczyć średniej.")
else:
    srednia = suma / n
    print(f"Średnia temperatura z {n} dni: {srednia:.2f}")