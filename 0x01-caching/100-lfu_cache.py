#!/usr/bin/env python3
"""  class LFUCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents object that allows storing and
    retrieving items from a dictionary using LFU
     when limit is reached.
    """

    def __init__(self):
        """  cache Initialization
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders items based on the most
        recently used item in the cache .
        """
        max_positions = []
        mst_rcntly_usd_frqncy = 0
        mst_rcntly_usd_position = 0
        ins_position = 0
        for x, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mst_rcntly_usd_frqncy = key_freq[1] + 1
                mst_rcntly_usd_position = x
                break
            elif len(max_positions) == 0:
                max_positions.append(x)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(x)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mst_rcntly_usd_frqncy:
                break
            ins_position = pos
        self.keys_freq.pop(mst_rcntly_usd_position)
        self.keys_freq.insert(ins_position, [mru_key, mst_rcntly_usd_frqncy])

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """item retrieval by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
