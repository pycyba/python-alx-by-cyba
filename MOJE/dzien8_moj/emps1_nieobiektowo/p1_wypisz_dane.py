"""
Chcemy odczytać plik emps.csv i dla każdego pracownika wypisać tekst jak 'Steven King zarabia 24000'
"""
with open('emps.csv', mode='r', encoding='UTF-8') as wejscie:
    wejscie.readline() # pomiń pierwszą linię
    # alternatywnie: next(wejscie)
    for linia in wejscie:
        t = linia.strip().split(';')
        # print(t)
        print(f'Pracownik {t[1]} {t[2]} zarabia {t[4]}.')
