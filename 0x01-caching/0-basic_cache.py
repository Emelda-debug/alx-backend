#!/usr/bin/env python3

""" class BasicCache that inherits from BaseCaching and is a caching system"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class `BasicCache` that inherits from `BaseCaching`
       and is a caching system"""

    def put(self, key, item):
        """assigns self.cache_data to the dictionary and
           `item` for the `key` value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return value in `self.cache_data` linked to `key`"""

        return self.cache_data.get(key, None)
