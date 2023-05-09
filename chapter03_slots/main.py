import sys
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.address = None

    def __repr__(self):
        return f'Person({self.name} is {self.age})'


p1 = Person('Phoebe', 25)
print(p1)
print(f'p1: {p1.name} {p1.age}')

# p1.address = '10 High Street'

print(f'sys.getsizeof(p1) slots - {sys.getsizeof(p1)}')
