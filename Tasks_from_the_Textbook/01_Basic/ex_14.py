"""

Write a program that displays the minimum and maximum numbers from
all the numbers entered by the user. Give
the user the option to end the number entry process
with an appropriate command. Make sure to handle the case where
the user does not enter any numbers.

"""

min_val = None
max_val = None

while True:
    s = input("Podaj liczbę (Enter lub q aby zakończyć): ").strip()
    if s == "" or s.lower() == "q":
        break

    try:
        num = float(s)  # użyj float, jeśli chcesz akceptować też wartości z przecinkiem/kropką
    except ValueError:
        print("Błąd: wpisz poprawną liczbę.")
        continue

    if min_val is None or num < min_val:
        min_val = num
    if max_val is None or num > max_val:
        max_val = num

if min_val is None:
    print("Nie podano żadnej liczby.")
else:
    print(f"Min: {min_val}, Max: {max_val}")