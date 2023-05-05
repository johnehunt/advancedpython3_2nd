from dataclasses import dataclass


@dataclass
class Trade:
    """Class for representing Equity Trades"""
    counter_party1: str
    counter_party2: str
    symbol: str
    amount: int = 0

    def __post_init__(self):
        print('In __post_init__() method')


print('Starting')
trade1 = Trade('John', 'Denise', 'IBM', 100)
print(trade1)
print('Done')
