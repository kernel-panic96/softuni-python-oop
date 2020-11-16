from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel, consumption):
        self.fuel_quantity = fuel
        self.fuel_consumption = consumption

    @abstractmethod
    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._AC_CONSUMPTION())
        if fuel_needed > self.fuel_quantity:
            return
        self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    @classmethod
    def _AC_CONSUMPTION(cls):
        return 0.9

    def drive(self, distance):
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle):
    @classmethod
    def _AC_CONSUMPTION(cls) -> float:
        return 1.6

    def drive(self, distance):
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


def test1():
    car = Car(20, 5)
    car.drive(3)
    assert car.fuel_quantity == 2.299999999999997, car.fuel_quantity
    car.refuel(10)
    assert car.fuel_quantity == 12.299999999999997, car.fuel_quantity


def test2():
    truck = Truck(fuel=100, consumption=15)
    truck.drive(5)
    assert truck.fuel_quantity == 17.0, truck.fuel_quantity
    truck.refuel(50)
    assert truck.fuel_quantity == 64.5, truck.fuel_quantity


test1()
test2()
print('test passed')
