
def pomiar_czasu(f):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        poczatek = datetime.now()
        try:
            return f(*args, **kwargs)
        finally:
            koniec = datetime.now()
            print('czas działania:', koniec - poczatek)

    return wrapper

@pomiar_czasu
def petla(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma


suma = petla(1000)
print(suma)

suma = petla(100_000_000)
print(suma)

