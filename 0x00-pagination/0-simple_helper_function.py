#!/usr/bin/env python3
"""Pagination Indexes"""

from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Calculates and returns the start and end indexes.

    Args:
        page: The selected page(type int)
        page_size: The total number allowed per page

    Returns:
        x: A tuple containing start and end indexes
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    x: Tuple = (start_index, end_index)
    return x
