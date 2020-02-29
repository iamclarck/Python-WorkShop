import time
import multiprocessing


def squaresum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
    return sm


# n = 4
if __name__ == '__main__':

    t1 = time.time()

    tasks = [20000022, 3000022, 40000022]
    processes = []
    for task in tasks:
        print(squaresum(task))
        process = multiprocessing.Process(target=squaresum, args=[task])
        process.start()
        processes.append(process)

    for pr in processes:
        pr.join()
    t2 = time.time()

    print(t2-t1)

# GIL(Global Interpreter Lock) because of this their is time bound between io and cpu operation
