#!/usr/bin/env python3
"""This module defines an async coroutine that takes in an int"""


from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Async Coroutine that takes in an int and returns a float"""
    delay: float = uniform(
        0, max_delay)  # random float between 0 and max_delay
    await asyncio.sleep(delay)
    return delay
