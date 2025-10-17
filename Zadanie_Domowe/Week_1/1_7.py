x = int(input("Podaj liczbę całkowitą, która będzie limitem: "))
liczby = []
ilosc = 0
for i in range(1,x+1):
    if i % 3 == 0 or i % 5 == 0:
        liczby.append(i) #dodajemy element do listy
        ilosc += 1
    else:
        continue
print(liczby)
print(*liczby) # gwiazdka = wypisanie bez nawiasów i przecinków
print(f"Takich licz było: {ilosc}")
print(f"Takich liczb było: {len(liczby)} ")

