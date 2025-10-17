from sklep import *
Menu = """
Menu
Q - wyjście z programu, a przy tym wypisanie sumarycznej kwoty za towary zakupione w czasie sesji
–
K - zakupy - pytanie o nazwę towaru i liczbę sztuk
–
C - zmiana ceny towaru - pytanie o nazwę towaru oraz nową cenę i aktualizacja słownika
–
N - dodanie nowego towaru do cennika
–
U - usunięcie towaru z 


"""
while True:
    wybor = str(input(f"{Menu}: ")).upper()
    match wybor:
        case "Q": break
        case "K": print("Zakupy")
        case "C": print("zmiana cen towarow")
        case "N": print("Dodanie nowego towaru")
        case "U": print("Usunięcie towaru z cennika")
        case "D": print("Dostawa towaru, w której program pyta o nazwę towaru \n"
                        " oraz liczbę sztuk i zwiększa stan towaru o podaną liczbę sztuk.")
        case "R": print("odczyt danych z pliku")
        case "W": print("zapis aktualnego cennika i ilości produktów do pliku")

