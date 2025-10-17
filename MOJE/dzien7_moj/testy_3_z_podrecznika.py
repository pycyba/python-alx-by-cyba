from zadanie_3_z_podrecznika import *

def test_scenariusz_zadania():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30  # zostało tylko 30
    assert car.drive(50) == 0   # brak zasięgu
    car.charge()
    assert car.drive(50) == 50

def test_pelny_zasieg():
    car = ElectricCar(200)
    assert car.drive(100) == 100
    assert car.drive(100) == 100
    assert car.drive(1) == 0  # wyczerpany

def test_charge_przywraca_pelny_zasieg():
    car = ElectricCar(150)
    car.drive(100)
    car.charge()
    assert car.current_range == 150

def test_dystans_zero_lub_ujemny():
    car = ElectricCar(100)
    assert car.drive(0) == 0
    assert car.drive(-10) == 0
    assert car.current_range == 100  # nie zmienił się

def test_wielokrotne_ladowanie():
    car = ElectricCar(50)
    car.drive(50)
    car.charge()
    car.charge()  # drugie ładowanie nic nie zmienia
    assert car.current_range == 50

