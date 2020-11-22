def numbers():
    i = 1
    while True:
        yield i

        i += 1


def take(count_to_take, sequence):
    return [x for _, x in zip(range(count_to_take), sequence)]


def halves():
    for x in numbers():
        yield x / 2


def solution():
    return take, halves, numbers


def main():
    def test_numbers():
        print(list(x for x, _ in zip(numbers(), range(4))))

    def test_halves():
        print(list(x for x, _ in zip(halves(), range(4))))

    def test_take():
        print(take(3, iter([1, 2, 3, 4])))

    test_numbers()
    test_halves()
    test_take()


if __name__ == "__main__":
    main()
