from pympler import asizeof

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'

data = [1, 2, (3, 4), 'Denise', True, Person('John')]
print(f'asizeof.asizeof(data): {asizeof.asizeof(data)}')

print(f'asizeof.asized(obj, detail=1).format():\n{asizeof.asized(data, detail=1).format()}')
