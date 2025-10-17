# W tej wersji: warunki negatywne, ale każdą rzecz sprawdzam oddzielnie
# wypisywany jest PIERWSZY komunikat o błędzie
# tutaj widać, że opłaca się sprawdzać warunki negatywne - wtedy od razu reagujemy w przypadku błędu
# dzięki `elif` nie ma nadmiarowych wcięć w kodzie

a = float(input('Podaj długość: '))
b = float(input('Podaj szerokość: '))
c = float(input('Podaj wysokość: '))
obj = a*b*c

if a > 50:
    print('Bagaż odrzucony - zbyt duża długość')
elif b > 50:
    print('Bagaż odrzucony - zbyt duża szerokość')
elif c > 50:
    print('Bagaż odrzucony - zbyt duża wysokość')
elif obj > 50_000:
    print('Bagaż odrzucony - zbyt duża objętość')
else:
    print('Bagaż spełnia normy')
