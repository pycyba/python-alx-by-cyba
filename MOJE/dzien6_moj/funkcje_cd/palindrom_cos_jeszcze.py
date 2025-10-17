def palindrom(napis):
    lista = []
    for znak in napis.lower():
        lista.append(znak)

    lista2 = list(lista)
    lista2.reverse()

    if lista == lista2:
        a = True
    else:
        a = False
    return a


def palindromv1(napis):
    return napis == napis[::-1]

def ile_samoglosek(napis):
    ile = 0
    samogloski = set('aeiouyąęó')
    for znak in napis.lower():
        if znak in samogloski:
            ile += 1
    return ile


def main():
    while True:
        napis = input("Podaj napis: ")
        if not napis:
            break
        if palindromv1(napis):
            print("To jest Palindrom")
        else:
            print("To nie jest Palindrom")
        print("Liczba samochoglosek", ile_samoglosek(napis))

if __name__ == "__main__":
    main()

