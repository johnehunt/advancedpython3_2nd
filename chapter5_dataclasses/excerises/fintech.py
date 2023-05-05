from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    """represents a customer within a financial system"""
    name: str
    address: str
    email: str


@dataclass
class Account:
    number: str
    customer: Customer
    balance: float


@dataclass
class CurrentAccount(Account):
    overdraft_limit: float

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit:
            self.balance = self.balance - amount
        else:
            raise ValueError(f'{self.balance - amount} Exceeds Overdraft Limit of {self.overdraft_limit}')


@dataclass
class DepositAccount(Account):
    interest_rate: float


customer1 = Customer('John',
                     '10 High Street',
                     'john@gmail.com')

acc1 = CurrentAccount("123", customer1, 10.0, -100.00)
print(acc1)
acc1.withdraw(1)
print(acc1)

customer2 = Customer('Denise',
                     '11 Main Street',
                     'denise@gmail.com')
acc2 = DepositAccount("345", customer2, 23.55, 0.5)
print(acc2)

try:
    acc1.withdraw(200)
except ValueError as err:
    print(err)
