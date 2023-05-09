import sys
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print(f'Happy birthday {self.name}, you were {self.age}', end = '')
        self.age = self.age + 1
        print(f' but now you are {self.age}')

p1 = Person('Phoebe', 25)
print(f'p1: {p1.name} {p1.age}')
print(f'sys.getsizeof(p1) noslots - {sys.getsizeof(p1)}')

p1.address = '10 High Street'
print(f'p1.address: {p1.address}')

p2 = Person('Gryff', 24)
print(f'p2: {p2.name} {p2.age}')
# print(f'p2.address: {p2.address}')
