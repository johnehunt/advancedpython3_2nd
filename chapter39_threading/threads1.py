from threading import Thread


def simple_worker():
    print('hello')


t1 = Thread(target=simple_worker)
t1.start()

# Get information about a Thread
print(t1.name)
print(t1.ident)
print(t1.is_alive())
