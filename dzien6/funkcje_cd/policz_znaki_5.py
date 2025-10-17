"""
Napisz funkcję obliczającą liczbę znaków w zadanym napisie
pomiędzy zadanymi znakami. Znaki, pomiędzy którymi ma odbywać
się zliczanie, powinny być argumentami z wartościami domyślnymi -
odpowiednio < i >. Nawiasy mogą być zagnieżdżone i mogą
wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami
liczone są zgodnie z poziomem zagnieżdżenia.
Przykład użycia:
>>> policz_znaki('ala ma <kota> a kot ma ale')
4
>>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
18
>>> policz_znaki('a <a<a<a>>>')
6
"""

def policz_znaki(napis, lewy='<', prawy='>'):
    wynik = 0
    poziom = 0
    for znak in napis:
        if znak == lewy:
            poziom += 1
        elif znak == prawy:
            poziom -= 1
        elif poziom > 0:
            wynik += poziom
    return wynik


def test1():
    assert policz_znaki('Ala ma <kota> i tyle') == 4

def test2():
    assert policz_znaki('Ala ma <kota> i <psa>.') == 7

# znaki umieszczone na głębszych poziomach zagnieżdżenia mają być liczone z większą wagą
# podwójną, potrójną itd.
def test3():
    assert policz_znaki('Ala ma <k<otk>a> i <psa>.') == 11

def test4():
    assert policz_znaki('0000<111<22<33<4>>2>11>0000<11<2>>00') == 3*1 + 2*2 + 2*3 + 4 + 2 + 2*1 + 2*1 + 2

# ostatnie wymaganie:
# domyślnymi znakami oznaczającymi fragment są nawiasy trójkątne < >
# ALE jeśli do funkcji przekażemy drugi i trzeci parametr, to wtedy funkcja używa podanych znaków

def test5():
    assert policz_znaki('Ala <ma> [kota] i [psa].', '[', ']') == 7

def test6():
    assert policz_znaki('Java i PythoN lalala', 'P', 'N') == 4

def test7():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
