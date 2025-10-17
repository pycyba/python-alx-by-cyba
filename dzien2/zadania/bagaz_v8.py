# Tutaj z kolei przerywamy program, od razu gdy zobaczymy, że jest źle.

a = float(input('Podaj długość bagażu: '))
if a > 50:
    print('Długość zbyt duża')
    exit(1)

b = float(input('Podaj szerokość bagażu: '))
if b > 50:
    print('Szerokość zbyt duża')
    exit(1)

c = float(input('Podaj wysokość bagażu: '))
if c > 50:
    print('Wysokość zbyt duża')
    exit(1)

obj = a*b*c
if obj > 50_000:
    print('Objętość zbyt duża')
    exit(1)

print('Bagaż spełnia normy')
