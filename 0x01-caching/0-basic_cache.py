#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherited Cache Class"""
    def init(self):
        """Initialization method"""
        super().__init__()

    def put(self, key, item):
        """Method to put item into cache at index key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Method to get item from cache at index key"""
        if key in self.cache_data:
            return self.cache_data.get(key, None)
