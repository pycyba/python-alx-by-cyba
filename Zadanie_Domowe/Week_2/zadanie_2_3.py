def trojkat_pita(n):
    wyniki = []   # ← stwórz pustą listę NA POCZĄTKU
    for a in range(1, n+1):
        for b in range(a, n+1):
            c2 = a*a + b*b
            c_int = int(c2**0.5)
            if c_int**2 == c2 and c_int > b and c_int <= n:
                wyniki.append((a, b, c_int))
    return wyniki

print(trojkat_pita(1000))