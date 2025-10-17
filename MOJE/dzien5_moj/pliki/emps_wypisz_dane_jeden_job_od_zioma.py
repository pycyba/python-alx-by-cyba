# Programmer, Accountant, President, Stock Clerk, ...
szukany_job = input('Podaj nazwę stanowiska: ')

# Oblicz średnią pensję na podanym stanowisku
suma = 0
ile = 0
with open('emps.csv', mode='r') as wejscie:
    wejscie.readline()
    for linia in wejscie:
        pola = linia.split(';')
        if pola[3] == szukany_job:
            suma += int(pola[4])
            ile += 1

if ile > 0:
    srednia = suma / ile
    print(f'Na stanowisku {szukany_job} pracuje {ile} osób, a ich średnia pensja wynosi {srednia:.2f}.')
else:
    print(f'Nikt nie pracuje na stanowisku {szukany_job}.')

# wersja z comprehension
import statistics
with open('emps.csv', mode='r') as wejscie:
    wejscie.readline()
    srednia = statistics.mean(float(pola[4])
                              for pola in (linia.split(';') for linia in wejscie)
                              if pola[3] == szukany_job)
print('wersja statistics.mean:', srednia)

# policzenie sztuk bez tworzenia listy - ale to taka sztuka dla sztuki...
with open('emps.csv', mode='r') as wejscie:
    wejscie.readline()
    ile_jest = sum(1 for linia in wejscie if linia.split(';')[3] == szukany_job)
    print(ile_jest)


# a jeśli zależy nam na obliczeniu kilku statystyk dla tych samych danych,
# to najlepiej będzie utworzyć listę i wywołać na niej różne funkcje - o ile dane mieszczą się w pamięci
with open('emps.csv', mode='r') as wejscie:
    wejscie.readline()
    lista = [float(pola[4])
              for pola in (linia.split(';') for linia in wejscie)
              if pola[3] == szukany_job]

print('len:', len(lista))
print('sum:', sum(lista))
print('avg:', statistics.mean(lista))
print('min:', min(lista))
print('max:', max(lista))
print('std:', statistics.stdev(lista))
print('median:', statistics.median(lista))
