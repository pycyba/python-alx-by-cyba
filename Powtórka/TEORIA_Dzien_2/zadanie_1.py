while True:
    try:
        x = int(input("Podaj liczbee od 1 do 10: "))
        if x in range(1, 11):
            print(f"Ok, {x}")
            break
        else:
            print("Licba poza zakresu; ")
    except ValueError:
        print("Zła liczba:")

