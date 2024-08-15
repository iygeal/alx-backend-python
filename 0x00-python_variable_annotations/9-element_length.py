#!/usr/bin/env python3
"""This module defines a type-annotated function element_length
that takes an iterable of sequences and returns a list of tuples,
where each tuple contains a sequence and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function returns a list of tuples containing
    each element and its length.
    """
    return [(i, len(i)) for i in lst]
