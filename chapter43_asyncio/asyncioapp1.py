import asyncio
import time


async def do_something():
    print('do_something - will wait for worker')
    result = await worker()
    print('do_something - result:', result)


async def worker():
    print('worker - will take some time')
    time.sleep(3)
    print('worker - done it')
    return 42


print('Main - Starting')
asyncio.run(do_something())
print('Main - Done')
