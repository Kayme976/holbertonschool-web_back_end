#!/usr/bin/env python3
"""takes an integer max delay and ruterns a asyncio"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return asyncio"""
    return asyncio.create_task(wait_random(max_delay))
