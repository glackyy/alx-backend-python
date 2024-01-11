#!/usr/bin/env python3
"""type-annotated function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of a list of Sequences"""
    return [(i, len(i)) for i in lst]