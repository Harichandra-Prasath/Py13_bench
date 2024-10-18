import threading
import time

from multiprocessing import Process

def benchmark(no_debug: bool):
    def fib(n):
            if n<=1:
                return n
            else:
                return fib(n-1)+fib(n-2)
    
    if not no_debug:
        start = time.perf_counter()

    n = 30
    for i in range(5):
        fib(n)
        n+=1
    
    if not no_debug:
        print("Time taken to complete one Job: ", time.perf_counter()-start)



def multi_proc_flow():
    _procs : list[Process] = list()

    print("Starting Multi-Process Flow")
    start = time.perf_counter()
    for i in range(3):
        proc = Process(target=benchmark, args=(True,))
        _procs.append(proc)
        proc.start()

    for _,proc in enumerate(_procs):
        proc.join()
    print("Time taken to complete three jobs with three Processes: ", time.perf_counter()-start)

def thread_flow():
    _threads : list[threading.Thread] = list()

    print("Starting Multi-Threaded Flow")
    start = time.perf_counter()
    for i in range(3):
        x = threading.Thread(target=benchmark, args=(True,))
        _threads.append(x)
        x.start()

    for _,thread in enumerate(_threads):
        thread.join()
    print("Time taken to complete three Jobs with three Threads: ", time.perf_counter()-start)

def linear_flow():
    print("Starting Linear Flow")
    start = time.perf_counter()
    for i in range(3):
        benchmark(bool(i))
    print("Time taken to complete three Jobs Linearly: ", time.perf_counter()-start)

print("----------------")
linear_flow()
print("----------------")
thread_flow()
print("----------------")
multi_proc_flow()
print("----------------")