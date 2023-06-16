# Multiprocessing barriers example

from multiprocessing import Barrier, Process, set_start_method
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

if __name__ == '__main__':
    print('Main - Starting')

    set_start_method('fork')
    barrier = Barrier(3, callback)
    p1 = Process(target=print_it, args=('A', barrier))
    p2 = Process(target=print_it, args=('B', barrier))
    p3 = Process(target=print_it, args=('C', barrier))
    p1.start()
    p2.start()
    p3.start()

    print('Main - Done')
