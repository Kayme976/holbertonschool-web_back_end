#!/usr/bin/env python3
"""Import async_comprehension from the previous file """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """will execute async_comprehension four times"""
    begin_time = time.time()
    rdm = [async_comprehension() for i in range(4)]
    result = await asyncio.gather(*rdm)
    end_time = time.time()
    return end_time - begin_time
