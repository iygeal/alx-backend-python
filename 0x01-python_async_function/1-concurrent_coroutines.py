#!/usr/bin/env python3
"""This module defines an async coroutine that takes two int arguments"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays

    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay
    Returns:
        list of all the delays
    """
    # List of tasks to run wait_random n times
    tasks: List[asyncio.Task] = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]

    # As each task completes, add its delay to the list
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task  # Wait for each task to complete
        delays.append(delay)  # Add the delay to the list

    return delays  # Return the list of all the delays
