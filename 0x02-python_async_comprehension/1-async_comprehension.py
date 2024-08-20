#!/usr/bin/env python3
"""This module defines a coroutine that uses async comprehension"""

from typing import AsyncGenerator
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """Demonstrates the use of async comprehension"""
    return [num async for num in async_generator()]
