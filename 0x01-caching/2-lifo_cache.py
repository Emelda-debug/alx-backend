#!/usr/bin/env python3
"""class LIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents object that allows storing and
    retrieval using LIFO of items from a dictionary
    """
    def __init__(self):
        """ cache Initializations
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ item addition in cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ item retrieval by key"""
        return self.cache_data.get(key, None)