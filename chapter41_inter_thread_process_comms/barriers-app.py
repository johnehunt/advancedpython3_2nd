# Threading barriers example

from threading import Barrier, Thread
from time import sleep
from random import randint


def print_it(msg, barrier):
    print('print_it for:', msg)
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    sleep(randint(1, 6))
    print('Wait for barrier with:', msg)
    barrier.wait()
    print('Returning from print_it:', msg)


def callback():
    print('\nCallback Executing')


print('Main - Starting')

barrier = Barrier(3, callback)
t1 = Thread(target=print_it, args=('A', barrier))
t2 = Thread(target=print_it, args=('B', barrier))
t3 = Thread(target=print_it, args=('C', barrier))
t1.start()
t2.start()
t3.start()

print('Main - Done')
