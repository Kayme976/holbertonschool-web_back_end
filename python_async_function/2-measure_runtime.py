#!/usr/bin/env python3
"""create a mesure time"""
import asyncio
import random
import time
from wait_random import wait_n


async def measure_time(n, max_delay):
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


async def main():
    n = 5
    max_delay = 10
    avg_time_per_delay = await measure_time(n, max_delay)
    print("Average time per delay:", avg_time_per_delay)

asyncio.run(main())
