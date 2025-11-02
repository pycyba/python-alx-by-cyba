a, b , c = map(int, input("Podaj liczby: ").split())
v = a*b*c
if v > 1000:
    print(f"Liczba {v} spelnia warunek")
else:
    print(f"Liczba {v} nie spelnia warunek")