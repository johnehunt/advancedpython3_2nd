# Immutable dataclasses

from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    title: str
    author: str = 'Anonymous'


book1 = Book('Python for ever!', 'John Smith')
print(book1)
# book1.author = 'Adam Davies'
