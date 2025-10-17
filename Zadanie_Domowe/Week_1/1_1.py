import math
while True: #Tutaj mamy nieskonczona pętle wyjdziemy dopiero jak będzie gdzieś Break
    try:
        a, b, c = map(int, input("Podaj 3 liczby: ").split())
    except ValueError:
        print("Błąd: musisz podać trzy liczby całkowite!")
        continue # Wraca na początek petli

    if a + b > c and a + c > b and b + c > a:
        print("Można zrobić z tego trójkąt liczymy...")
        p = (a + b + c) / 2
        pole_trojkata = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'Pole trójkąta to: {pole_trojkata:.2f}')
        break
    else:
        print("Nie zrobimy z tego trójkąta")

