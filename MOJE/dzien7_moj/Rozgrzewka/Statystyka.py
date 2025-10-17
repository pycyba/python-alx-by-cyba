# takie podejście zadziała tylko dla kolekcji - gdy dane są w pamięci
# ale nie zadziała dla 'ulotnych' źródeł danych, jak iteratory i generatory
# dla których nie jest dostępna funkcja len, a dane "znikają" po ich pierwszym odczycie
# def statystyki(dane):
#     return len(dane), sum(dane), sum(dane)/len(dane), min(dane), max(dane)

def statystyki(dane):
    count = 0
    sum = 0
    min = float('+inf')
    max = float('-inf')
    for x in dane:
        count += 1
        sum += x
        if x > max:
            max = x
        if x < min:
            min = x
    if count > 0:
        return count, sum, sum/count, min, max
    else:
        return 0, 0, None, None, None


a = [10, 20, 5, -5, 33, 22, 0, 1]
wyniki = statystyki(a)
print(wyniki)

c, s, a, mn, mx = statystyki(a)
print(f'count={c}, sum={s}, avg={a}, min={mn}, max={mx}')

tekst = '5 10 15'
wyniki2 = statystyki(map(int, tekst.split()))
print(wyniki2)

