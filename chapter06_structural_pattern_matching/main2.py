class Person:
    __match_args__ = ("name", "age")

    def __init__(self, pos, age):
        self.name = pos
        self.age = age


def print_person(person):
    match person:
        case Person(name, age):
            print(f'Person name={name}, age={age}')
        case _:
            print('Not a person')


p = Person('John', 21)
print_person(p)
print_person(42)
