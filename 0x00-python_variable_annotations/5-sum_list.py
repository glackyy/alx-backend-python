#!/usr/bin/env python3
"""type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of float numbers"""
    return float(sum(input_list))
