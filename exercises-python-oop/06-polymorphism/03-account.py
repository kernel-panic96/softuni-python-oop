from functools import total_ordering
from typing import List


@total_ordering
class Account:
    owner: str
    amount: int
    _transactions: List[int]

    def __init__(self, owner: str, amount: int = 0):   # NOTE: gotcha optional arguments
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: 'Account', amount: int):
        if account.balance + amount < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount)
        return f'New balance: {account.balance}'

    def __add__(self, other):
        # good to have type checks for other and exceptions
        new_acc = Account(self.owner + '&' + other.owner, self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions

        return new_acc

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index: int) -> int:
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'


def main():
    def test_add_transaction():
        acc = Account('john doe', amount=20)
        acc.add_transaction(10)
        acc.add_transaction(20)

        print(acc._transactions, 'should be [10, 20]')

    def test_balance():
        acc = Account('john doe', amount=20)
        acc.add_transaction(10)
        acc.add_transaction(20)

        print(acc.balance, 'should be 50')

    def test_safe_transaction():
        acc = Account('john doe', amount=0)
        acc.add_transaction(-10)

        print(acc.balance, 'should be -10')
        try:
            Account.validate_transaction(acc, -10)
        except ValueError:
            print('transaction failed, should have failed')

    def test_account_to_string():
        acc = Account('bob', amount=20)
        print(str(acc), 'should be "Account of bob with starting amount: 20"')

    def test_account_repr():
        acc = Account('bob', amount=20)
        print(repr(acc), 'should be "Account(bob, 20)"')

    def test_len_account():
        acc = Account('bob', amount=20)
        acc.add_transaction(10)
        acc.add_transaction(10)
        print(len(acc), 'should be 2')

    def test_iteration_account():
        acc = Account('bob', amount=20)
        acc.add_transaction(10)
        acc.add_transaction(11)
        acc.add_transaction(12)

        print(list(acc), 'should be [10, 11, 12]')  # [transaction for transaction in acc ]

    def test_indexing_account():
        acc = Account('bob', amount=20)
        acc.add_transaction(10)
        acc.add_transaction(11)
        acc.add_transaction(12)

        print(acc[1], 'should be 11')  # [transaction for transaction in acc ]

    def test_reversing_account():
        acc = Account('bob', amount=20)
        acc.add_transaction(10)
        acc.add_transaction(11)
        acc.add_transaction(12)

        print(list(reversed(acc)), 'should be [12, 11, 10]')

    def test_account_comparison():
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)

        acc2 = Account('alice')
        acc2.add_transaction(10)
        acc2.add_transaction(60)

        print(acc > acc2, 'should be False, acc > acc2')
        print(acc >= acc2, 'should be False, acc >= acc2')
        print(acc < acc2, 'Should be True, a < a2')
        print(acc <= acc2, 'Should be True, a < a2')
        print(acc == acc2, 'Should be False, a == a2')
        print(acc != acc2, 'Should be True, a != a2')

    def test_adding_accounts():
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)

        acc2 = Account('alice')
        acc2.add_transaction(10)
        acc2.add_transaction(60)

        print((acc + acc2)._transactions, 'should be [20, -20, 30, 10, 60]')

    test_add_transaction()
    test_balance()
    test_safe_transaction()
    test_account_to_string()
    test_account_repr()
    test_len_account()
    test_iteration_account()
    test_indexing_account()
    test_reversing_account()
    test_account_comparison()
    test_adding_accounts()


if __name__ == "__main__":
    main()
