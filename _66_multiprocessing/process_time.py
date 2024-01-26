from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(f"cpu count: {cpu_count()}")

    for number in range(1, 10):
        print(f"starting process {number}")
        process = Process(target=counter, args=(10000000,))
        process.start()
        process.join()

    print("starting process a")
    a = Process(target=counter, args=(10000000,))
    a.start()
    a.join()

    print("starting process b")
    b = Process(target=counter, args=(10000000,))
    b.start()
    b.join()

    print(f"finished in {time.perf_counter()} seconds")

if __name__ == '__main__':
    main()