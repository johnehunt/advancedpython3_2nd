class Singleton:

    instance = None

    def __new__(cls, *args, **kwargs):
        print('Entering __new__')
        if Singleton.instance is None:
            print('Creating instance')
            # create the single instance
            Singleton.instance = super().__new__(cls)

        print('Returning instance')
        return Singleton.instance


print('Starting')
s1 = Singleton()
print('-' * 25)
s2 = Singleton()
print('-' * 25)
s3 = Singleton()
print('-' * 25)

print(id(s1))
print(id(s2))
print(id(s3))
print('Done')
