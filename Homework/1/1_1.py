"""
Task 1.1: Triangle Area

Write a program that reads three numbers, checks if these numbers can form the sides of a triangle
(e.g., you can't make a triangle from 2, 2, and 5, right?), and if they can, calculates the area
of the triangle with those sides.

Heron's formula: area = sqrt(p * (p - a) * (p - b) * (p - c))
where p is half the perimeter: p = (a + b + c) / 2

Square root is the sqrt function from the math module, or you can raise to the power of 0.5.
"""
while True:
    import math

    try:
        a, b, c = map(float, input("Podaj 3 boki (oddziel spacją): ").split())

        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Pole trójkąta: {pole:.2f}")
        else:
            print("Z tych boków nie da się zbudować trójkąta.")

    except Exception as e:
        print(f"Błąd: podaj trzy poprawne liczby: {e}")