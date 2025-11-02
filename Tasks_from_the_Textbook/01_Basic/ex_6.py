liczba = int(input("Liczba: "))

if liczba > 10:
    w1 = True
else:
    w1 = False
if liczba <= 15:
    w2 = True
else:
    w2 = False
if liczba % 2 == 0:
    w3 = True
else:
    w3 = False

print(f"Liczba: {liczba}: {w1}")
print(f"Liczba: {liczba}: {w2}")
print(f"Liczba: {liczba}: {w3}")