szukany_job = input("Podaj Stanowisko: ")

suma = 0
ile = 0
with open('emps.csv', mode='r') as wejscie:
    wejscie.readline()
    for linia in wejscie:
        pola = linia.split(';')
        if szukany_job == pola[3]:
            suma += int(pola[4])
            ile += 1

srednia = suma / ile
print('suma:', suma)
print("Ile pracownikow:", ile)
print('średnia1:', srednia)

#
# # wersja z listą:
# salaries = []
# with open('emps.csv', mode='r') as wejscie:
#     wejscie.readline()
#     for linia in wejscie:
#         pola = linia.split(';')
#         salaries.append(float(pola[4]))
# srednia = sum(salaries) / len(salaries)
# print('średnia2:', srednia)
#
# # wersja z comprehension
# import statistics
# with open('emps.csv', mode='r') as wejscie:
#     wejscie.readline()
#     srednia = statistics.mean(float(linia.split(';')[4]) for linia in wejscie)
#
# print('średnia3:', srednia)
#
