def read_next(*iterables):
    for iterable in iterables:
        for el in iterable:
            yield el


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
