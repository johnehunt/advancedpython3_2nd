from dataclasses import dataclass


@dataclass
class Trade:
    """Class for representing Equity Trades"""
    counter_party1: str
    counter_party2: str
    symbol: str
    amount: int = 0


trade1 = Trade('John', 'Denise', 'IBM', 100)
print(trade1)
trade2 = Trade('John', 'Adam', 'MSFT', 50)
print(trade2)
print(trade1 == trade2)
trade3 = Trade('John', 'Denise', 'IBM', 100)
print(trade1 == trade3)
