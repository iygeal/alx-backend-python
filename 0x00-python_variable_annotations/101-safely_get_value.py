#!/usr/bin/env python3
"""This module defines a type-annotated function safely_get_value
that retrieves a value from a dictionary by key or returns a default value.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a type variable for the value type
T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """This function returns the value associated with the key
    in the dictionary or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
