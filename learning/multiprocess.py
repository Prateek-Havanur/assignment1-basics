from multiprocessing import Process, Pool
from concurrent.futures import ProcessPoolExecutor
import asyncio
import time


# async def square(x):
#     await asyncio.sleep(x)
#     return x * x


# def square(x):
#     time.sleep(x)
#     return x * x


async def square(x):
    await asyncio.sleep(x)
    return x * x


async def main():
    tasks = [square(x) for x in [1, 2, 3, 4, 5]]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    #     resultus = []
    #     with Pool(2) as P:
    #         resultus = P.map(square, [1, 2, 3, 4, 5])
    #     numbers = [30, 31, 32]

    #     with ProcessPoolExecutor() as executor:
    #         results = executor.map(square, numbers)

    #     print(results)

    print(asyncio.run(main()))
