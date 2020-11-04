import math


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int) -> None:
        self.x = new_x

    def set_y(self, new_y: int) -> None:
        self.y = new_y

    def distance(self, x, y) -> float:
        delta_x = abs(x - self.x)
        delta_y = abs(y - self.y)
        return math.sqrt(delta_x ** 2 + delta_y ** 2)


if __name__ == "__main__":
    p = Point(3, 5)
    print(p.distance(10, 2))
