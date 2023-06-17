class Person:

    def __init__(self, name, age):
        print('In __init__')
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.name}), {self.age})'

print('Starting')
p1 = Person('John', 21)
print(p1)
p2 = Person('Denise', 18)
print(p2)
print('Done')
