from timeit import timeit, Timer, repeat

TIMES_TO_RUN_FUNCTION = 1000


def sample_function():
    result = 0
    for i in range(100000):
        result = result + (i * i * i)
    return result


# Using the timer function
time_taken = timeit(sample_function, number=TIMES_TO_RUN_FUNCTION)
print(f'total time: {time_taken}, average time: {time_taken / TIMES_TO_RUN_FUNCTION}')

print('-' * 25)
# Using the repeat function
print(repeat(sample_function, repeat=5, number=TIMES_TO_RUN_FUNCTION))

print('-' * 25)
timer = Timer(sample_function)
print(timer.timeit(number=1000))
