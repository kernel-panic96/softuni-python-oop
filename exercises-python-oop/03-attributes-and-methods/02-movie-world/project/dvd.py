class DVD:  # TODO(yavor): kata this ctor + instance attributes
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    _digit_to_month = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self) -> str:
        status = 'rented' if self.is_rented else 'not rented'
        return (f'{self.id}: {self.name} ({self.creation_month} {self.creation_year})'
                f' has age restriction {self.age_restriction}. Status: {status}')

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> 'DVD':
        day, month, year = date.split('.')

        return cls(name, id, creation_year=int(year), creation_month=cls._digit_to_month[month], age_restriction=age_restriction)
