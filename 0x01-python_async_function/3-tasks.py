#!/usr/bin/env python3
"""Returns an asyncio.Task"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[summary]

    Args:
        max_delay (int): [description]

    Returns:
        asyncio.Task: [description]
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
