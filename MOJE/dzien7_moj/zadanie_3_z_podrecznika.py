"""

Zaimplementuj klasę ElectricCar odwzorowującą zachowanie
samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
zadanego dystansu, który nie może przekroczyć maksymalnego
zasięgu zdefiniowanego dla samochodu. Samochód powinien
mieć także możliwość naładowania baterii.
 car = ElectricCar(100)
 car.drive(70)
70
 car.drive(50)
30
 car.drive(50)
0
 car.charge()
 car.drive(50)
50


"""
class ElectricCar:
    def __init__(self, dystans):
        self.dystans = dystans
        self.zasieg = dystans

    def drive(self, przebyte_km):
        if przebyte_km < 0:
            return 0
        if przebyte_km <= self.zasieg:
            self.zasieg -= przebyte_km
            return przebyte_km
        else:
            faktyczne_przebyte = self.zasieg
            self.zasieg = 0
            return faktyczne_przebyte
    def charge(self):
        self.zasieg = self.dystans

def main():
    car = ElectricCar(100)
    car.drive(70)
    car.drive(50)
    car.drive(50)
    car.charge()
    car.drive(50)

if __name__ == '__main__':
    main()
