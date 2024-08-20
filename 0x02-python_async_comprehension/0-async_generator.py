#!/usr/bin/env python3
"""This module defines an async coroutine, a generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generates 10 random numbers between 0 and 10.

    The coroutine will loop 10 times, each time waiting 1 second
    before yielding a random number.

    Yields:
        A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
