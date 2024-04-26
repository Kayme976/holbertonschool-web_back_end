#!/usr/bin/env python3
"""takes an integer max delay and ruterns a asyncio"""
import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay):
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
