class Foo:
    def __init__(self):
        self.foo = 'FOO'

    def method(self, arg):
        print(f'{self.foo} {arg}')


class Bar(Foo):
    def __init__(self):
        self.foo = 'BAZ'
        self.bar = 'BAR'

Bar.method = Foo.method


print(Bar().method('BAZ'))
