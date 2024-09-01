#!/usr/bin/env python3
"""Pagination Indexes"""

from typing import List, Tuple, Dict
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the Page

        Args:
            self
            page: The needed page (type int)
            page_size: The number of items per page (type int)

        Returns:
            page_list:A list of item on page (type list)
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0 and page_size > 0

        page_ranges = Server.index_range(self, page, page_size)
        startIndex: int = page_ranges[0]
        endIndex: int = page_ranges[-1]
        page_list = [i for i in Server.dataset(self)[startIndex:endIndex]]
        return page_list

    def index_range(self, page: int, page_size: int) -> Tuple:
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Gets data and a few other details

        Args:
            page: The selected page(type int)
            page_size: The total number allowed per page

        Returns:
            result: A dictionary containing details of page
        """
        c = 0
        for i in Server.dataset(self):
            c += 1

        result = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(self, page, page_size),
            'next_page': page + 1 if page < int(c / page_size) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.floor(c / page_size)
        }
        return result
