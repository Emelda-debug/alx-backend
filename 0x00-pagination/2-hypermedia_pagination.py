#!/usr/bin/env python3
"""
get_hyper method that takes the same arguments (and defaults) as
get_page and returns a dictionary containing the following key-value pairs:
page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """function to return a tuple of size two containing
    a start index and an end index """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        data = self.dataset()
        if start_idx > len(data):
            return []
        return data[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves page information """
        data = self.get_page(page, page_size)
        start_idx, end_idx = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end_idx < len(self.__dataset) else None,
            'prev_page': page - 1 if start_idx > 0 else None,
            'total_pages': total_pages
        }
