class Trade:
    """Class for representing Equity Trades"""

    def __init__(self, counter_party1, counter_party2, symbol, amount):
        self.counter_party1 = counter_party1
        self.counter_party2 = counter_party2
        self.symbol = symbol
        self.amount = amount

    def __repr__(self):
        return f'Trade(counter_party1={self.counter_party1}, ' \
               f'counter_party_2={self.counter_party2}' \
               f'symbol={self.symbol},' \
               f'amount={self.amount})'

    def __eq__(self, other):
        if not isinstance(other, Trade):
            return False
        return self.counter_party1 == other.counter_party1 and \
            self.counter_party2 == other.counter_party2 and \
            self.symbol == other.symbol and \
            self.amount == other.amount

trade1 = Trade('John', 'Denise', 'IBM', 100)
print(trade1)
trade2 = Trade('John', 'Adam', 'MSFT', 50)
print(trade2)
print(trade1 == trade2)
trade3 = Trade('John', 'Denise', 'IBM', 100)
print(trade1 == trade3)
