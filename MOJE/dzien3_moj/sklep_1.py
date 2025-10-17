cennik = {
    'woda': 3.90,
    'kawa': 12.50,
    'herbeta': 14.40,
    'mleko': 4.40,
}

# x = input("Podaj nazwę towaru: ")
# ilosc = int(input("Podaj ile sztuk: "))
#
# if x in cennik:
#     do_zaplaty = cennik[x] * ilosc
#     print(f"Do zapłaty: {do_zaplaty:.2f} zł")
# else:
#     print("Nie mamy takiego produktu w cenniku")

#Wersja rozbudowa:
#program w petli prosi o podowanie nazw produkt i ich ilosc
#podaje laczna sume
#mozna przyjac np.

suma_calosc = 0

while True:
    x = input("Podaj nazwę towaru (ENTER kończy zakupy): ").lower()

    if x == '':  # najpierw sprawdzamy puste!
        break

    if x in cennik:
        ilosc = int(input("Podaj ile sztuk: "))
        do_zaplaty = cennik[x] * ilosc
        suma_calosc += do_zaplaty
        print(f"Do zapłaty: {do_zaplaty:.2f} zł")
        print(f"Do zapłaty w sumie : {suma_calosc:.2f} zł\n")
    else:
        print("Nie mamy takiego produktu w cenniku\n")

print(f"Twoje zakupy zakończone. Łączna kwota: {suma_calosc:.2f} zł")

