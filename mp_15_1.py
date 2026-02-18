import multiprocessing as mp
import random
import time
from datetime import datetime

def worker(proc_num: int) -> None:
    wait_time = random.random()  # 0.0 to 1.0
    time.sleep(wait_time)
    print(f"Process {proc_num} waited {wait_time:.3f}s and prints time: {datetime.now().isoformat(timespec='seconds')}")

if __name__ == "__main__":
    procs = []
    for n in range(1, 4):  # three processes
        p = mp.Process(target=worker, args=(n,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
