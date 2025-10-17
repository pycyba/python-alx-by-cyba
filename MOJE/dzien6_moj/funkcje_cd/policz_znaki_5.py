def policz_znaki(tekst, lewy='<', prawy='>'):
    poziom = 0    # poziom zagnieżdżenia
    wynik = 0
    for znak in tekst:
        if znak == lewy:          # otwarcie nawiasu
            poziom += 1
        elif znak == prawy:       # zamknięcie nawiasu
            if poziom > 0:
                poziom -= 1
        else:
            #if poziom > 0:
                wynik += poziom
    return wynik

def test1():
    assert  policz_znaki("Ala maa <kota> i tyle ") == 4
def test2():
    assert policz_znaki('Ala ma <kota> i <psa>') == 7
def test3():
    assert policz_znaki("Ala ma <k<otk>a> i <psa>") == 11
def test4():
    assert policz_znaki('0000<111<22<33<4>>2>11>000<11<2>>00') == 3*1 + 2*2 + 2*3 + 4 + 2 + 2*1 + 2*1 + 2
def test5():
    assert policz_znaki('Ala <ma> [kota] i [psa].', '[', ']') == 7

def test6():
    assert policz_znaki('Java i PythoN lalala', 'P', 'N') == 4

def test7():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
