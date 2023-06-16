from multiprocessing import Pool


def collect_results(result):
    print('In collect_results: ', result)


def worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=2) as pool:
        # get based example
        res = pool.apply_async(worker, [6])
        print('Result from async: ', res.get(timeout=1))

    # callback based example
    pool = Pool(processes=2)
    pool.apply_async(worker, args=[4], callback=collect_results)
    pool.close()
    # Need to wait for asynchronous process to complete
    pool.join()


if __name__ == '__main__':
    main()
