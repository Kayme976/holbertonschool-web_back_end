#!/usr/bin/env python3*
"""containig index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """return the start of index and the end"""
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
