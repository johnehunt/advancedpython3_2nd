# dataclasses support inheritance

from dataclasses import dataclass

@dataclass
class Trade:
    """Class for representing Equity Trades"""
    counter_party1: str
    counter_party2: str


@dataclass
class EquityTrade(Trade):
    symbol: str
    amount: int = 0

trade1 = EquityTrade('John', 'Denise', 'IBM', 100)
print(trade1)
trade2 = EquityTrade('John', 'Adam', 'MSFT', 50)
print(trade2)
print(trade1 == trade2)
trade3 = EquityTrade('John', 'Denise', 'IBM', 100)
print(trade1 == trade3)
