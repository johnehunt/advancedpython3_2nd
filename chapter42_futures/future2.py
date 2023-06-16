from multiprocessing import set_start_method
from time import sleep
from concurrent.futures import ProcessPoolExecutor


def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    return i

if __name__ == '__main__':
    print('Starting')

    set_start_method('spawn')

    print('Setting up the ProcessPoolExecutor')
    pool = ProcessPoolExecutor(1)

    print('Submitting the worker to the pool')
    future = pool.submit(worker, 'A')

    print('Obtained a reference to the future object', future)
    print('future.result():', future.result())

    print('Done')
