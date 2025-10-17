class A:
    # atrybuty klasowe
    str1 = 'Ala'
    int1 = 100
    list1 = []

    # atrybuty obiektowe tworzone w init:
    def __init__(self, str2, int2=0, list2=[]):
        self.str2 = str2
        self.int2 = int2
        self.list2 = list2
        self.list3 = list(list2)
        self.list4 = []

    def modyfikuj(self, x):
        self.str1 += ', ' + str(x)
        self.str2 += '; ' + str(x)
        self.int1 += x
        self.int2 += x
        self.list1.append(x)
        self.list2.append(x)
        self.list3.append(x)
        self.list4.append(x)

    def __str__(self):
        return f'''{super().__str__()}
    str1: {self.str1}
    str2: {self.str2}
    int1: {self.int1}
    int2: {self.int2}
    list1: {self.list1}
    list2: {self.list2}
    list3: {self.list3}
    list4: {self.list4}'''

    def print_info(self):
        print('atrybuty klasowe:', A.__dict__)
        print('atrybuty obiektowe:', self.__dict__)


a = A('Ola')
b = A('Basia')
print('a:', a)
a.print_info()

print('b:', b)
b.print_info()
print()

# modyfikuję obiekt a, a element 3 pojawia się także w napisie wyświetlanym przez b
a.modyfikuj(3)
a.modyfikuj(5)
a.modyfikuj(7)
print('a:', a)
a.print_info()

print('b:', b)
b.print_info()
print()

# Modyfikacja wartości atrybutów klasowych wpływa na te obiekty, które zmiennych str i int nie modyfikowały
print('Zmieniam atrybuty klasowe')
A.int1 = 500
A.str1 = 'Alicja'
A.list1.append(999)


print('a:', a)
b.print_info()

print('b:', b)
b.print_info()

d = A('Dorota')
print('d:', d)

