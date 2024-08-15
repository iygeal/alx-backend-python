#!/usr/bin/env python3
"""This module defines a type-annotated function to_kv"""


def to_kv(k: str, v: int | float) -> tuple:
    """This function returns a tuple"""
    return (k, v**2)
