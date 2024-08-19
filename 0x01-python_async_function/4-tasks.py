#!/usr/bin/env python3
"""This module alters wait_n to use task_wait_random"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all delays in ascending order.

    Args:
        n (int): number of times to spawn task_wait_random.
        max_delay (int): maximum delay for each task.

    Returns:
        List[float]: list of delays in ascending order.
    """
    # Create n tasks using task_wait_random
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]

    # Collect delays as each task completes
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task  # Wait for each task to complete
        delays.append(delay)  # Add the delay to the list

    return delays  # Return the list of all the delays
