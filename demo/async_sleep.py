import asyncio

loop = asyncio.get_event_loop()


async def sleep(n: int) -> None:
    await asyncio.sleep(3)
    print(f'finished {n} iteration')


async def gather():
    tasks = []
    for iteration in range(10):  # type: int
        tasks.append(loop.create_task(sleep(iteration)))
    for n in tasks:
        await n


if __name__ == '__main__':
    loop.run_until_complete(asyncio.gather(*(sleep(i) for i in range(10))))
