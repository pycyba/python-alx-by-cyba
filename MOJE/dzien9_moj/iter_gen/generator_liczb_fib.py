"""
Generator dostarcza kolejnych liczb ciągu Fibonacciego
od 0 do liczby nr n włącznie.
0 1 1 2 3 5 8 13 21 34 55 89 144
"""
def fib_gen(n):
    a, b = 0, 1
    for i in range(0, n + 1):
        yield a
        a, b = a+b, a


def fib_genw(n):
    a, b = 0, 1
    while n >= 0:
        yield a
        a, b, n = a+b, a, n-1

def main():
    n = int(input('Podaj n: '))
    for x in fib_gen(n):
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()

