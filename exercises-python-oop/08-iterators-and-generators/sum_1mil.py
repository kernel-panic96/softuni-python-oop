import sys
from collections.abc import Iterator
from datetime import datetime
from time import sleep
from typing import Any
from typing import Iterator as IteratorType


class Numbers(Iterator):
    def __init__(self, first_n):
        self.first_n = first_n

    def __iter__(self) -> IteratorType[Any]:
        self.i = 0
        return self

    def __next__(self):
        val = self.i
        self.i += 1
        if val == self.first_n + 1:
            raise StopIteration

        return val


def numbers(first_n: int):
    i = 0
    data = []
    while i <= first_n:
        data.append(i)
        sleep(0.001)
        i += 1
    return data


before = datetime.now()
iterator = iter(Numbers(1000))
after = datetime.now()
s = 0
for x in iterator:
    s += x
print(s)
print('time to first interaction with iterator', after - before)

before = datetime.now()
iterator = iter(numbers(1000))
after = datetime.now()
s = 0
for x in iterator:
    s += x
print(s)
print('time to first interaction without iterator', after - before)
