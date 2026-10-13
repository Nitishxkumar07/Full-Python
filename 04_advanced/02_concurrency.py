"""02 - Threads, processes, asyncio. The GIL: threads help I/O, processes help CPU."""
import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def io_task(n):
    time.sleep(0.1)                       # simulates network wait
    return n * 2

def cpu_task(n):
    return sum(i * i for i in range(n))

# --- threading with a lock ---
counter, lock = 0, threading.Lock()
def work():
    global counter
    for _ in range(10_000):
        with lock:
            counter += 1
threads = [threading.Thread(target=work) for _ in range(4)]
[t.start() for t in threads]; [t.join() for t in threads]
print("counter:", counter)

# --- Thread pool for I/O ---
with ThreadPoolExecutor(max_workers=5) as ex:
    print(list(ex.map(io_task, range(5))))
    futures = [ex.submit(io_task, i) for i in range(3)]
    print(sorted(f.result() for f in as_completed(futures)))

# --- asyncio: cooperative multitasking, single thread ---
async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    results = await asyncio.gather(fetch("a", 0.2), fetch("b", 0.1))
    print(results)
    async with asyncio.TaskGroup() as tg:          # structured concurrency (3.11+)
        t1 = tg.create_task(fetch("c", 0.1))
        t2 = tg.create_task(fetch("d", 0.1))
    print(t1.result(), t2.result())
    try:
        async with asyncio.timeout(0.05):          # 3.11+
            await asyncio.sleep(1)
    except TimeoutError:
        print("timed out")
    q = asyncio.Queue()
    async def producer():
        for i in range(3): await q.put(i)
        await q.put(None)
    async def consumer():
        while (item := await q.get()) is not None:
            print("got", item)
    await asyncio.gather(producer(), consumer())
    print(await asyncio.to_thread(io_task, 21))    # run blocking code off the loop

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    # Processes (guard with __main__ on Windows/macOS):
    with ProcessPoolExecutor(max_workers=2) as ex:
        print(list(ex.map(cpu_task, [10_000, 20_000])))
    print(f"total {time.perf_counter() - start:.2f}s")
