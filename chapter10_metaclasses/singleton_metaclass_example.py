class SingletonMetaclass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print('In SingletonMetaclass.__call__')
        if cls not in cls._instances:
            print(f'Creating new instance of {cls}')
            cls._instances[cls] = super().__call__(*args, **kwargs)
        print('Returning instance')
        return cls._instances[cls]


class Session(metaclass=SingletonMetaclass):
    def __init__(self):
        print('In Session initialiser')


print('Starting')
s1 = Session()
s2 = Session()

print(f'id(s1): {id(s1)}')
print(f'id(s2): {id(s2)}')
# checks to see if they are the same instance
print(f's1 is s2: {s1 is s2}')
print('Done')

