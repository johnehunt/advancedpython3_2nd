from concurrent.futures import ProcessPoolExecutor
from multiprocessing import set_start_method
from time import sleep


def worker(msg):
    for i in range(0,10):
        print(msg,end='', flush=True)
        sleep(1)
    return i


if __name__ == '__main__':
    print('Starting')
    set_start_method('spawn')

    pool = ProcessPoolExecutor(3)
    future1 = pool.submit(worker, 'A')
    future2 = pool.submit(worker, 'B')
    future3 = pool.submit(worker, 'C')
    future4 = pool.submit(worker, 'D')
    print('\nfuture4.result():', future4.result())
    print('All Done')
