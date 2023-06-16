from threading import Thread, Semaphore, current_thread
from time import sleep


def worker(semaphore):
    with semaphore:
        print(current_thread().name + " - entered")
        sleep(0.5)
        print(current_thread().name + " - exiting")


print('MainThread - Starting')

semaphore = Semaphore(2)
for i in range(0, 5):
    thread = Thread(name='T' + str(i), target=worker, args=[semaphore])
    thread.start()

print('MainThread - Done')
