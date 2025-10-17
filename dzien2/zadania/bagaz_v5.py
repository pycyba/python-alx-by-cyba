# wersja kompromisowa pod względem szczegółowości
# przy okazji pokazuję technikę wczytywania kilku wartości podanych w jednej linii
# oraz porównanie wartości maksymalnej zamiast trzech porównań.

a, b, c = map(float, input('Podaj trzy liczby  wymiary bagażu:\n').split())
if max(a, b, c) > 50:
    print('Bagaż odrzucony - jeden z boków przekracza normę')
elif a*b*c > 50_000:
    print('Bagaż odrzucony - zbyt duża objętość')
else:
    print('Bagaż spełnia normy')
