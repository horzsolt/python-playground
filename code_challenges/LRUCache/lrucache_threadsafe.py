from collections import OrderedDict
import threading
import unittest

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key in self.cache:
                # Move the key to the end to mark it as most recently used
                value = self.cache.pop(key)
                self.cache[key] = value
                return value
            else:
                return -1

    def put(self, key, value):
        with self.lock:
            if key in self.cache:
                # Remove the existing key to update its value
                self.cache.pop(key)
            elif len(self.cache) >= self.capacity:
                # Remove the least recently used key if the cache is full
                self.cache.popitem(last=False)
            self.cache[key] = value

class TestLRUCache(unittest.TestCase):

    def test_cache(self):

        cache = LRUCache(5)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)
        cache.put(5, 5)

        cache.get(1)
        cache.put(6, 6)

        print(cache) #OrderedDict([(3, 3), (4, 4), (5, 5), (1, 1), (6, 6)])

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLRUCache)
    unittest.TextTestRunner().run(suite)
    #unittest.main()        