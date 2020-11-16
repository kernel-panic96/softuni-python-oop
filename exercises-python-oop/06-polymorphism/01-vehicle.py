from abc import ABC, abstractmethod


class Vehicle(ABC):
    fuel_quantity: int
    fuel_consumption: int

    def __init__(self, fuel, consumption):
        self.fuel_quantity = fuel
        self.fuel_consumption = consumption

    @abstractmethod
    def refuel(self, fuel: int):
        self.fuel_quantity += fuel

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self._CONSUMPTION_PER_KM)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    @property
    @abstractmethod
    def _CONSUMPTION_PER_KM(self):
        ...


class Car(Vehicle):
    _CONSUMPTION_PER_KM = 0.9

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle):
    _CONSUMPTION_PER_KM = 1.6

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


def test_vehicle_can_be_instantianted():
    Car(fuel=10, consumption=2)
    Truck(fuel=20, consumption=4)
    print('test_vehicle_can_be_instantianted passed')


def test_vehicle_should_be_able_to_drive():
    car = Car(fuel=10, consumption=2)
    car.drive(2)
    assert car.fuel_quantity == 4.2, car.fuel_quantity
    print('test_vehicle_should_be_able_to_drive passed')

    truck = Truck(100, 15)
    truck.drive(5)
    assert truck.fuel_quantity == 17.0, \
        truck.fuel_quantity


def test_vehicles_gain_fuel_when_refueled():
    car = Car(fuel=5, consumption=3)
    car.refuel(10)
    assert car.fuel_quantity == 15, \
        car.fuel_quantity

    truck = Truck(17.0, 15)
    truck.refuel(50)
    assert truck.fuel_quantity == 64.5, \
        truck.fuel_quantity

    print('test_vehicles_gain_fuel_when_refueled passed')


def test_drive_longer_than_being_able():
    car = Car(fuel=5, consumption=3)
    car.drive(10000)
    assert car.fuel_quantity == 5,\
        car.fuel_quantity

    truck = Truck(fuel=5, consumption=3)
    truck.drive(10000)
    assert truck.fuel_quantity == 5,\
        truck.fuel_quantity

    print('test_drive_longer_than_being_able passed')


test_vehicle_can_be_instantianted()
test_vehicle_should_be_able_to_drive()
test_vehicles_gain_fuel_when_refueled()
test_drive_longer_than_being_able()
