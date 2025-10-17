with open('emps.csv', mode='r') as wejscie:
    wejscie.readline() # inny zapis: next(wejscie)
    for linia in wejscie:
        # print(linia)
        pola = linia.split(';')
        # print(pola)
        print(f'Pracownik {pola[1]} {pola[2]} zarabia {pola[4]}')


# następne zadanie: oblicz średnią pensję pracowników z całego pliku
# 6461.68....
