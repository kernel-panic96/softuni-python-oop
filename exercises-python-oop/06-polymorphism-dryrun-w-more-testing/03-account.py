from typing import List


class Account:
    owner: str
    amount: int
    _transactions: List[int]

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')

        self._transactions.append(amount)

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: 'Account', amount: int):
        if account.balance + amount < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount)
        return f'New balance: {account.balance}'

    def __getitem__(self, key):
        return self._transactions[key]

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_acc = Account(self.owner, self.amount)
        new_acc._transactions = self._transactions + other._transactions

        return new_acc
