from typing import ClassVar, List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    name: str
    customers: List[Customer]
    dvds: List[DVD]

    _DVD_CAPACITY: ClassVar[int] = 15
    _CUSTOMER_CAPACITY: ClassVar[int] = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    # NOTE(yavor): this makes more sense to be a class method rather than static method
    @classmethod
    def dvd_capacity(cls) -> int:
        return cls._DVD_CAPACITY

    # NOTE(yavor): this makes more sense to be a class method rather than static method
    @classmethod
    def customer_capacity(cls) -> int:
        return cls._CUSTOMER_CAPACITY

    # NOTE(yavor): what to do when the list exceeds capacity
    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) >= self._CUSTOMER_CAPACITY:
            return
        self.customers.append(customer)

    # NOTE(yavor): what to do when the list exceeds capacity
    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) >= self._DVD_CAPACITY:
            return   # XXX
        self.dvds.append(dvd)

    # NOTE(yavor): customer not found is not defined
    # NOTE(yavor): dvd not found is not defined
    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd      = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]

        if dvd_id not in map(lambda x: x.id, customer.rented_dvds):
            return f'{customer.name} does not have that DVD'

        dvd = [d for d in customer.rented_dvds if d.id == dvd_id][0]
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)

        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        return '\n'.join([repr(x) for x in (self.customers + self.dvds)])
