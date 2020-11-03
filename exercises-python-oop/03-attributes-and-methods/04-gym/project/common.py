@classmethod
def _get_next_id(cls):
    return cls._id


def generic_init(self, *args):
    attributes = self.__annotations__

    for attr, value in zip(attributes, args):
        if attr == '_id':
            continue

        setattr(self, attr, value)

    self.id = self.__class__._id
    self.__class__._id += 1


def dataclass(attributes, repr_format):
    klass = type('_', (), {})
    klass._id = 1
    klass.__init__ = generic_init
    klass.get_next_id = _get_next_id
    klass.__annotations__ = attributes

    def repr_implementation(self):
        return repr_format.format(self=self)

    klass.__repr__ = repr_implementation

    return klass
