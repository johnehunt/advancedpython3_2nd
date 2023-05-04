from dataclasses import dataclass


@dataclass
class Trade:
    """Class for representing Equity Trades"""
    counter_party1: str
    counter_party2: str
    symbol: str
    amount: int = 0

    # dataclasses can still have methods defined for them
    def calculate_value(self, price):
        return self.amount * price


trade1 = Trade('John', 'Denise', 'IBM', 100)
print(trade1)

print(f'The value of this trade at 1.55 per share = {trade1.calculate_value(1.55)}')
