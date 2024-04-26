#!/usr/bin/env python3
"""asynchronus take in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous takes in an integer argument"""
    rdm_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rdm_delay)
    return rdm_delay
