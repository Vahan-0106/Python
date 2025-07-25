from multiprocessing import Process
import urllib.request
import json
import threading
import time
import os
import asyncio
import aiohttp

url = "https://jsonplaceholder.typicode.com/posts/1"
req = urllib.request.Request(url, headers={"User-Agent": "MyApp 1.0"})

def func1_for_multi_threading():
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.load(resp)

    print("Hello")

def func2_for_multi_threading():
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.load(resp)

    print("Hello")

def func3_for_multi_threading():
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.load(resp)

    print("Hello")

async def func_for_async():
    url = "https://api.github.com/repos/psf/requests"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            print("Hello from asyncio")

async def main():
    page1 = asyncio.create_task(func_for_async())
    page2 = asyncio.create_task(func_for_async())
    page3 = asyncio.create_task(func_for_async())

    await asyncio.gather(page1, page2, page3)

    
if __name__ == "__main__":
    t1 = threading.Thread(target=func1_for_multi_threading, name = "t1", args=())
    t2 = threading.Thread(target=func2_for_multi_threading, name = "t2", args=())
    t3 = threading.Thread(target=func3_for_multi_threading, name = "t3", args=())

    start_time = time.time()
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()
    print(f"Execution time with multhithreading: {(end_time -start_time)*10**3}ms")

    p1 = Process(
        target=func1_for_multi_threading, args=()
    )
    p2 = Process(
        target=func2_for_multi_threading, args=()
    )
    p3 = Process(
        target=func3_for_multi_threading, args=()
    )

    start_time = time.time()

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end_time = time.time()

    print(f"Execution time with multiprocessing: {(end_time - start_time)*10**3}ms")


    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()

    print(f"Execution time with asyncio: {(end_time-start_time)*10**3}ms")
