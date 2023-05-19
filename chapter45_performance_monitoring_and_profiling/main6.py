from pympler import classtracker

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'

tracker = classtracker.ClassTracker()
# Set up which class should be tracked
tracker.track_class(Person)

# Capture statistics
tracker.create_snapshot()
p1 = Person('John')
p2 = Person('Denise')
p3 = Person('Phoebe')
tracker.create_snapshot()

# Generate the report
tracker.stats.print_summary()
