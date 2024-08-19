#!/usr/bin/env python3
"""Module to return an asyncio.Task from a regular function"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): maximum delay for wait_random.

    Returns:
        asyncio.Task: a task that will execute wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
