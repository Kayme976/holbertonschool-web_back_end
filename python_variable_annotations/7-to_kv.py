#!/usr/bin/env python3
"""that function return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple with a float anf a string"""
    return (k, v * v)
