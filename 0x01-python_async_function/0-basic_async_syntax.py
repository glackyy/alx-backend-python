#!/usr/bin/env python3
"""an Asynchronous coroutine"""
import asyncio, random


async def wait_random(max_delay: int = 8) -> float:
    """Waiting for a random num of seconds"""
    w_time = random.random() * max_delay
    await asyncio.sleep(w_time)
    return w_time
