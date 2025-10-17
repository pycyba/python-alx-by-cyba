def suma(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma
# suma_parzystych - liczbe sume tylko tych licz z listy ktore sa parzyste

def suma_parzystych(lista):
    suma = 0
    for x in lista:
        if x % 2 == 0:
            suma += x
        else:
            continue
    return suma

# drugi_najwiekszy - zwraca druga co do wielkosci wartosc z listy
#jezeli drugiego elemtu nie ma( bo lista jest pusta albo ma jedno wartosc)
# to wtedy funckja ma zwrocic None


def drugi_najwieksz(lista):
    drugi = sorted(lista)
    if len(drugi) >1:
        return ((drugi[-2]))
    else:
        return None

def drugi_najwiekszy(lista):
    zbior = set(lista)
    max1 = max(zbior)
    zbior.remove(max1)
    max2 = max(zbior)
    return max2


