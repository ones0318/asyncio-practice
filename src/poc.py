import asyncio
import time


async def wait(seconds):
    await asyncio.sleep(seconds)
    print('waited {}'.format(seconds))


async def main(loop):
    tasks = []
    for seconds in [1, 2, 3, 4, 5]:
        tasks.append(loop.create_task(wait(seconds)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(main(loop))
    print('total {}'.format(time.time()-start))

