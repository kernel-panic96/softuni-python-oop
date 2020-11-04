from typing import Union


class Account:
    id: int
    name: str
    balance: int

    def __init__(self, id: int, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[str, int]:
        if self.balance - amount < 0:
            return 'Amount exceeded balance'
        self.balance -= amount
        return self.balance

    def info(self) -> str:
        return f'User {self.name} with account {self.id} has {self.balance} balance'


if __name__ == "__main__":
    account = Account(5411256, "Peter")
    print(account.debit(500))
    print(account.credit(1000))
    print(account.debit(500))
    print(account.info())
