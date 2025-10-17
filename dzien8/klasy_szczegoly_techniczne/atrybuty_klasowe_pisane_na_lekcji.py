class Klasa:
    atrybut_klasowy = 100
    lista_klasowa = []

    def __init__(self, kto):
        self.kto = kto

    def wypisz(self):
        print(f'{self.kto}: {self.atrybut_klasowy=} {self.lista_klasowa=}')
        print('atrybuty klasowe:', Klasa.__dict__)
        print('atrybuty obiektowe:', self.__dict__)
        print()

    def zmien(self):
        self.atrybut_klasowy += 1
        # równoważnie do:
        # self.atrybut_klasowy = self.atrybut_klasowy + 1

        self.lista_klasowa.append('nowy')
        # self.lista_klasowa += ['nowy']


print('Początek programu')
# do atrybutu klasowego można dostać się poprzez nazwę klasy
print(f'{Klasa.atrybut_klasowy=} {Klasa.lista_klasowa=}')

# ale można też dostać się do nich poprzez obiekty
obiekt1 = Klasa('obiekt1')
obiekt2 = Klasa('obiekt2')
print(f'{obiekt1.atrybut_klasowy=}')
print(f'{obiekt2.atrybut_klasowy=}')
obiekt1.wypisz()
obiekt2.wypisz()
print()

# Co się dzieje, gdy poprzez obiekt "modyfikujemy" atrybut klasowy?...
obiekt1.zmien()

obiekt1.wypisz()
obiekt2.wypisz()
print(f'{Klasa.atrybut_klasowy=} {Klasa.lista_klasowa=}')

