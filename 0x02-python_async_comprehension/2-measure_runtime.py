#!/usr/bin/env python3
"""This module defines a coroutine to measure runtime."""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of executing async_comprehension four times
    in parallel.

    Returns:
        The total runtime in seconds as a float.
    """
    start_time = time.perf_counter()  # Record the start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # Record the end time
    # Calculate and return the total runtime
    return float(end_time - start_time)
