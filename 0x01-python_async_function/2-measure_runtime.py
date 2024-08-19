#!/usr/bin/env python3
"""This module defines an async routine that measures the
execution time of another async routine
"""

from typing import List
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): number of coroutines to run
        max_delay (int): maximum delay for wait_random

    Returns:
        float: average time per coroutine
    """
    start_time: float = time()  # Start the timer

    asyncio.run(wait_n(n, max_delay))

    end_time = time()  # Stop the timer

    return (end_time - start_time) / n  # Calculate and return the average
