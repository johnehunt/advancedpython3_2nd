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

et = EquityTrade('John', 'Denise', 'IBM', 100)
print(et)
