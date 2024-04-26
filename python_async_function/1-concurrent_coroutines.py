#!/usr/bin/env python3
"""import wait random"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async wait n and takes 2 int arguments
    """
    task = [wait_random(max_delay) for i in range(n)]
    delay = await asyncio.gather(*task)
    return sorted(delay)
