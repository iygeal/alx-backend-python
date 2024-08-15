#!/usr/bin/env python3
"""This module defines a type-annotated function sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function returns the sum of a list of integers and floats."""
    return sum(mxd_lst)
