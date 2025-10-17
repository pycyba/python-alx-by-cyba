numer = 5

match numer:
    case 1: print('poniedziałek')
    case 2: print('wtorek')
    case 3: print('środa')
    case 4: print('czwartek')
    case 5:
        print('piątek')
        print('weekendu początek')
    case 6: print('sobota')
    case 7: print('niedziela')
    case _: print('Błędny numer')

print('a kuku')

# match case pojawił się dopiero w Python 3.10
# Ta konstrukcja jest nieco bardziej zaawansowana

dane = ['Ala', 30, 'Warszawa']

match dane:
    case 30: print('trzydzieści')
    case 'Ala': print('napis Ala')
    case ['Ola', wiek, miasto]:
        print('Lista z imieniem OLA, w ktorej są też:', wiek, miasto)
    case ['Ala', wiek, miasto]:
        print('Lista z imieniem ALA, w ktorej są też:', wiek, miasto)
    case [kto, wiek, miasto]:
        print('Lista z innym imieniem:', kto, wiek, miasto)
    case _: print('coś zupełnie innego')

