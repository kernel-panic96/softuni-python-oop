from typing import ClassVar


class Circle:
    radius: int
    pi: ClassVar[float] = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self) -> float:
        return self.pi * self.radius ** 2

    def get_circumference(self) -> float:
        return 2 * self.pi * self.radius


if __name__ == "__main__":
    c = Circle(10)
    c.set_radius(12)
    print(c.get_area())
    print(c.get_circumference())
