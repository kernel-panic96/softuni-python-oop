from typing import Any, Dict


class dictionary_iter:
    def __init__(self, data: Dict[Any, Any]):
        self.data = data
        self.__data = iter(self.data.items())

    def __iter__(self):
        self.__data = iter(self.data.items())
        return self

    def __next__(self):
        val = next(self.__data)
        return val


def main():
    def test():
        res = list(dictionary_iter({1: '1', 2: '2'}))
        print(f'{res} should be [(1, "1"), (2, "2")]')

    test()


if __name__ == "__main__":
    main()
