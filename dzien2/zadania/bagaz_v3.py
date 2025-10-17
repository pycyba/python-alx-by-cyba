# w tej wersji: warunki pozytywne, ale każdą rzecz sprawdzam oddzielnie
# wypisywany jest PIERWSZY komunikat o błędzie
# efektem jest program o brzydkiej strukturze: zbyt wiele wcięć ("schodki"), else jest daleko od swojego ifa

a = float(input('Podaj długość: '))
b = float(input('Podaj szerokość: '))
c = float(input('Podaj wysokość: '))
obj = a*b*c

if a <= 50:
    if b <= 50:
        if c <= 50:
            if obj <= 50_000:
                print('Bagaż spełnia normy')
            else:
                print('Bagaż odrzucony - zbyt duża objętość')
        else:
            print('Bagaż odrzucony - zbyt duża wysokość')
    else:
        print('Bagaż odrzucony - zbyt duża szerokość')
else:
    print('Bagaż odrzucony - zbyt duża długość')
