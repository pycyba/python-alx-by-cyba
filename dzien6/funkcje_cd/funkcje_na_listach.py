def suma(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma


# dopisz funkcje i ich testy
# suma_parzystych - liczy sumę tylko tych liczb z listy, które są parzyste
def suma_parzystych(lista):
    suma = 0
    for x in lista:
        if x % 2 == 0:
            suma += x
    return suma

def suma_parzystych_alt(lista):
    return sum(x for x in lista if x % 2 == 0)


# drugi_najwiekszy - zwraca drugą co do wielkości wartość z listy
# Jeśli drugiego elementu nie ma (bo lista jest pusta albo zawiera jedną wartość)
# to wtedy funkcja ma zwrócić None
def drugi_najwiekszy(dane):
    zbior = set(dane)
    if len(zbior) < 2:
        return None
    max1 = max(zbior)
    zbior.remove(max1)
    return max(zbior)

