"""
Program ma wypisać 'tabliczkę mnożenia' 10x10

wersja 4x4 wygląda tak:
 1  2  3  4
 2  4  6  8
 3  6  9 12
 4  8 12 16
"""

for x in range(1, 11):
    for y in range(1, 11):
        print(x*y, end=' ')
    print()
