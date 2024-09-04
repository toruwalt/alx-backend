#!/usr/bin/env python3
"""Basic LRU Caching System.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherited Cache Class"""
    def __init__(self):
        """Initialization method"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.least_used = {}

    def put(self, key, item):
        """Method to put item into cache at index key"""
        if key is None or item is None:
            return
        else:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, True)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    del_item_key, val = self.cache_data.popitem(last=False)
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key, True)
                    print("DISCARD {}".format(del_item_key))
                else:
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key, True)

    def get(self, key):
        """Method to get item from cache at index key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, True)
            return self.cache_data.get(key, None)
