class Play:
    __slots__ = ['title', 'author', 'year']

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Play("{self.title}", by {self.author} in {self.year})'


play = Play('Alls Well That Ends Well',
            'William Shakespeare',
            '1598')
print(play)

# play.publisher = 'First Folio Team'

