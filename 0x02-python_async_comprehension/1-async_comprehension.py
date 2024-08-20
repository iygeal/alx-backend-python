#!/usr/bin/env python3
"""This module defines a coroutine that uses async comprehension"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension.

     The coroutine will use an async comprehension to gather 10 random
     numbers from async_generator, then return them.

     Returns:
         A list of 10 random float numbers collected from async_generator.
     """
    return [num async for num in async_generator()]
