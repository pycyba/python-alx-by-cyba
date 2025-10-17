t = [5, 0, 2]

for i in range(4):
    print('Początek obrotu pętli for nr', i)
    try:
        print('Teraz sprawdzam liczbę:', t[i])
        wynik = 100 / t[i]
        print(f'Wynik dzielenia 100 / {t[i]} = {wynik}')
        print('Tu też widać, że nie było wyjątku...')
    except ZeroDivisionError:
        print('except: wystąpił błąd dzielenia przez 0')
    except ValueError:
        print('except: błąd wartości')
    else:
        print('else: czyli oficjalnie wiem, że nie było wyjątku')
    finally:
        print('finally: kolejna liczba sprawdzona')
    print('OK, koniec obrotu pętli for\n')
print('Koniec wszystkiego')

