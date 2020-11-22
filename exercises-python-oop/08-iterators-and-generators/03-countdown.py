class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.__current = count

    def __iter__(self):
        self.__current = self.count
        return self

    def __next__(self):
        val, self.__current = self.__current, self.__current - 1

        if val == -1:
            raise StopIteration

        return val


def main():
    res = list(countdown_iterator(3))
    print(f'{res} should 3 2 1 0')


if __name__ == "__main__":
    main()
