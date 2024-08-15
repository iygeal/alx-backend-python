#!/usr/bin/env python3
"""This module defines a type-annotated function zoom_array
that creates a zoomed-in version of the input tuple by a given factor.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """The zoom_ray function creates a zoomed-in version of the input tuple"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
