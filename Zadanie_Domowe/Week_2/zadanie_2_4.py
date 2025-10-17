def merge(dict1, dict2):
    wynik = {}
    # Unia kluczy z obu słowników
    wszystkie_klucze = dict1.keys() | dict2.keys()

    for k in wszystkie_klucze:
        # „Bezpieczne” pobranie wartości; jeśli klucza nie ma, zwraca 0
        v1 = dict1.get(k, 0)
        v2 = dict2.get(k, 0)
        wynik[k] = v1 + v2
    return wynik


a = {'a': 10, 'b': 20}
b = {'b': 3, 'c': 4}
print(merge(a, b))  # {'a': 10, 'b': 23, 'c': 4}

# Chciabym wyjasniuenie wersji zawansowanej
