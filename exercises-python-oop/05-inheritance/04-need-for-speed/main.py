from project.car import Car
from project.cross_motorcycle import CrossMotorcycle
from project.family_car import FamilyCar
from project.motorcycle import Motorcycle
from project.race_motorcycle import RaceMotorcycle
from project.sport_car import SportCar
from project.vehicle import Vehicle

# How the inheritance hierarchy is determined - C3 linearization https://en.wikipedia.org/wiki/C3_linearization
# useful approximation of C3 linearization (may not be the same) - DFS - Depth First Search, Breadth First Search


def test_inheritance_is_correct():
    for kls in [Vehicle, Motorcycle, Car, RaceMotorcycle, CrossMotorcycle, FamilyCar, SportCar]:
        print(kls.__name__, kls.__mro__[1].__name__)


def test_car_drive():
    c = Car(30, 50)
    print(c.drive(11))
    print(c.fuel)


def test_default_fuel_consumption_is_correct():
    assert SportCar.DEFAULT_FUEL_CONSUMPTION == 10, f'was {SportCar.DEFAULT_FUEL_CONSUMPTION}'
    assert RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION == 8, f'was {RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION}'
    assert Car.DEFAULT_FUEL_CONSUMPTION == 3
    assert FamilyCar.DEFAULT_FUEL_CONSUMPTION == 3
    assert Vehicle.DEFAULT_FUEL_CONSUMPTION == 1.25


test_default_fuel_consumption_is_correct()
