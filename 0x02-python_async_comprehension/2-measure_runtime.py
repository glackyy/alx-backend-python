#!/usr/bin/env python3
"""Async Coroutine"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executing async_comprehension 4 times and measures
    the total exec time"""
    st_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - st_time
