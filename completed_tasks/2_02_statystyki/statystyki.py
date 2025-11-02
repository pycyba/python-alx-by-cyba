# Ta wersja jest dobra dla listy liczb itp:
def statystyki(numbers):
    if not numbers:
        return 0, 0, None, None, None
    cnt, sum, min, max = 0, 0, numbers[0], numbers[0]
    for x in numbers:
        cnt += 1
        sum += x
        if x < min:
            min = x
        if x > max:
            max = x
    return cnt, sum, sum / cnt, min, max


# Ta wersja będzie lepsza, jeśli źródłem danych będzie generator lub inna rzecz,
# dla której nie jest dostępne sprawdzenie niepustości i pobranie "zerowego elementu".
def statystyki_v2(numbers):
    try:
        pierwszy = next(numbers)
        cnt, sum, min, max = 1, pierwszy, pierwszy, pierwszy
    except StopIteration:
        return 0, 0, None, None, None
    for x in numbers:
        cnt += 1
        sum += x
        if x < min:
            min = x
        if x > max:
            max = x
    return cnt, sum, sum / cnt, min, max
