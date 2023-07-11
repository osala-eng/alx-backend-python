#!/usr/bin/env python3
"""
Multiple coroutines at the same time with async
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> list:
    """[summary]

    Args:
        n (int, optional): [description]. Defaults to 0.
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        list: [description] - list of all the delays (float values)
        in assending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay = [await task for task in asyncio.as_completed(tasks)]
    return delay


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(15, 0)))
