class Konto:
    def __init__(self, numer, wlasciciel, saldo = 0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, wł {self._wlasciciel}, saldo: {self._saldo}'

    def wplata(self, kwota):
        self._saldo += kwota

    def wyplata(self, kwota):
        self._saldo -= kwota


konto = Konto(1, 'Ala')
print(konto)
konto.wplata(5000)
print(konto)

# gdy jakiś atrybut w obiekcie ma nazwę od podkreślenia _saldo
# to jest to sugestia dla innych programistów oraz dla narzędzi
# aby traktować ten atrybut jako prywatny
# np. PyCharm nie podpowiada tej zmiennej podczas pisania kodu
# Jeśli jednak wpiszę w kodzie, to uzyskam dostęp i Python tego nie zabrania
print(konto._saldo)
konto._saldo -= 3333
print(konto._saldo)
print(konto)
print()

# To nie daje takich gwarancji ochrony, jak pola prywatne w Java czy C++

# Istnieje też mechanizm oparty o podwójne podkreślenia
class Bankomat:
    def __init__(self, banknoty):
        self.__lista_banknotow = list(banknoty)

    def __str__(self):
        return f'Bankomat załadowany banknotami {self.__lista_banknotow}'


bankomat = Bankomat([100, 100, 200])
print(bankomat)

# Taki dostęp już nie działa
#ERR print(bankomat.__lista_banknotow)

print(bankomat.__dict__)
# atrybut istnieje, tylko ma zmienioną nazwę ('name mangling')
# i jeśli wiem o tym, to mogę uzyskać "nielegalny dostęp"
print(bankomat._Bankomat__lista_banknotow)

del bankomat._Bankomat__lista_banknotow[-1]
bankomat._Bankomat__lista_banknotow.append(50)
bankomat._Bankomat__lista_banknotow.append(20)

print(bankomat._Bankomat__lista_banknotow)
print(bankomat)
