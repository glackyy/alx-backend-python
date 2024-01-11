#!/usr/bin/env python3
"""type-annotated function"""
from typing import List, Union


def sum_mixed_mist(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of int and float numbers"""
    return float(sum(mxd_lst))