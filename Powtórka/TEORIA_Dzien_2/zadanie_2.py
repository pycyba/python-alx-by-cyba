liczby = [0, 2, 5, 7, 10, 11, 14, 15]

parzyste = [x for x in liczby if x % 2 == 0]
nieparzyste_wieksze = [x for x in liczby if x % 2 != 0 and x > 10]
suma_zakres = sum(x for x in liczby if 5 <= x <= 12)

print("Parzyste:", parzyste)
print("Nieparzyste > 10:", nieparzyste_wieksze)
print("Suma [5,12]:", suma_zakres)