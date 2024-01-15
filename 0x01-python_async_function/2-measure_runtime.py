#!/usr/bin/env python3
"""measure time function"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Computing the average runtime of wait_n"""
    st_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - st_time) / n