while True:
    liczba = int(input("Liczba: "))
    if liczba % 2 != 0  and liczba % 3 == 0 and liczba > 10 or liczba ==7:
        print("Liczba spelnia warunek")
    elif liczba == '':
        break
    else:
        print("Liczba nie spelnia warunek")

