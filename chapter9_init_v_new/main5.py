class CallableClass:
    def __call__(self, *args, **kwargs):
        print("The object was called!")


print('Start')
obj = CallableClass()
obj()
print('Done')
