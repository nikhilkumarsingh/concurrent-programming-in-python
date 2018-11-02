import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(2)
    print("World!")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# for python 3.7
# asyncio.run(main())

