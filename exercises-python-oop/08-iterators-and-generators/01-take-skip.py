from typing import Iterable


class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self) -> Iterable[int]:
        self.current = 0
        return self

    def __next__(self):
        val, self.current = self.current, self.current + self.step
        generated_so_far = (val / self.step)
        if generated_so_far == self.count:
            raise StopIteration

        return val


def main():
    def test_take_skip():
        res = list(iter(take_skip(step=2, count=6)))
        print(f'{res} should be [0, 2, 4, 6, 8, 10]')

    test_take_skip()


if __name__ == "__main__":
    main()
