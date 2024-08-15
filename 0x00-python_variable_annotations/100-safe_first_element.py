#!/usr/bin/env python3
"""This module defines a type-annotated function safe_first_element
that takes a sequence of unknown elements and returns the first element
or None if the sequence is empty.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function returns the first element of the sequence
    or None if empty.
    """
    if lst:
        return lst[0]
    else:
        return None
