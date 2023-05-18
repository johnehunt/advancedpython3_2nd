class MyClass:
    def __new__(cls, *args, **kwargs):
        print('Entering __new__')
        # Custom object creation logic
        instance = super().__new__(cls)
        print('New instance created')
        # Additional initialisation of the instance if needed
        return instance

    def __init__(self):
        print('In __init__')


print('Starting')
obj = MyClass()
print('Done')
