#!/usr/bin/env python3
"""This module defines a type-annotated function sum_list
that takes a list input_list of floats as argument
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function returns the sum of a list of floats."""
    return sum(input_list)
