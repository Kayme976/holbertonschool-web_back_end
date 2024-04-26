#!/usr/bin/env python3
"""identical to wait n"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """identical to wait"""
    task = [task_wait_random(max_delay) for i in range(n)]
    delay = await asyncio.gather(*task)
    return sorted(delay)
