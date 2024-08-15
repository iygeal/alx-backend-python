#!/usr/bin/env python3
"""This module defines a type-annotated function sum_list
that takes a list input_list of floats as argument
and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """This function returns the sum of a list of floats."""
    return sum(input_list)
