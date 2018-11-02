import asyncio
import time


async def display_time():
    start_time = time.time()
    while True:
        dur = int(time.time() - start_time)
        if dur % 3 == 0:
            print("{} seconds have passed".format(dur))
        await asyncio.sleep(1)


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def main():
    task1 = asyncio.ensure_future(display_time())
    task2 = asyncio.ensure_future(print_nums())

    # for python 3.7
    # task1 = asyncio.create_task(display_time())
    # task2 = asyncio.create_task(print_nums())

    await asyncio.gather(task1, task2)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# for python 3.7
# asyncio.run(main())
