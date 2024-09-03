#!/usr/bin/env python3
"""Basic FIFO Caching System.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherited Cache Class"""
    def init(self):
        """Initialization method"""
        super().__init__()

    def put(self, key, item):
        """Method to put item into cache at index key"""
        if type(key) is None or type(item) is None:
            pass
        else:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    item_del = next(iter(self.cache_data.keys()))
                    del self.cache_data[item_del]
                    self.cache_data[key] = item
                    print("DISCARD {}".format(item_del))
                else:
                    self.cache_data[key] = item

    def get(self, key):
        """Method to get item from cache at index key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
