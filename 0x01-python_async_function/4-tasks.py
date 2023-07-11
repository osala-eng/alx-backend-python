#!/usr/bin/env python3
"""Task wait n => task wait random"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        list: [description]
    """
    return [await task_wait_random(max_delay) for _ in range(n)]


if __name__ == "__main__":
    print(asyncio.run(task_wait_n(5, 5)))
    print(asyncio.run(task_wait_n(10, 7)))
    print(asyncio.run(task_wait_n(15, 0)))
