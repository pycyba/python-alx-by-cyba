from geometria import *

menu = '''Wybierz figurę
 K - kwadrat
 P - prostokąt
 O - koło
 T - tójkąt (trzy boki)
 Q - koniec programu
> '''

while True:
    wybor = input(menu)
    match wybor:
        case 'Q': break
        case 'K':
            a = float(input('Podaj długość boku: '))
            pole = pole_kwadratu(a)
            obw = obwod_kwadratu(a)
            print(f'pole: {pole}, obwód: {obw}')
        case 'P':
            a = float(input('podaj bok a: '))
            b = float(input('podaj bok b: '))
            pole = pole_prostokata(a, b)
            obwod = obwod_prostokata(a, b)
            print(f'pole jest równe {pole} a obwód {obwod}')
        case 'O':
            r = float(input('podaj promień: '))
            pole = pole_kola(r)
            obwod = obwod_kola(r)
            print(f'pole jest równe {pole} a obwód {obwod}')
        case 'T':
            a, b, c = map(float, input('Podaj trzy boki trójkąta: ').split())
            if poprawny_trojkat(a, b, c):
                pole = pole_trojkata(a, b, c)
                obwod = obwod_trojkata(a, b, c)
                print(f'pole jest równe {pole} a obwód {obwod}')
            else:
                print('Z tych boków nie da się ułożyć trójkąta')

