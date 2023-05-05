from dataclasses import dataclass, field


class StockExchange:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'StockExchange({self.name})'


def make_stock_exchange():
    return StockExchange('London Stock Exchange')


@dataclass
class Trade:
    """Class for representing Equity Trades"""
    counter_party1: str
    counter_party2: str
    symbol: str
    amount: int = 0
    market: StockExchange = field(default_factory=make_stock_exchange)


trade1 = Trade('John', 'Denise', 'IBM', 100)
print(trade1)
