#!/usr/bin/env python3
"""identical to wait n"""
import asyncio
import random

async def task_wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_n(n, max_delay):
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

async def main():
    n = 5
    max_delay = 10
    delays = await task_wait_n(n, max_delay)
    print("Delays:", delays)

asyncio.run(main())