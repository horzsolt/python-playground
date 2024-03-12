import unittest

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __str__(self) -> str:
        return str(self.cache)
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  # dummy head node
        self.tail = Node(None, None)  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_end(self, node):
        # Move a node to the end of the linked list
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_end(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move the node to the end
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used node from the front
                lru_node = self.head.next
                del self.cache[lru_node.key]
                self.head.next = lru_node.next
                lru_node.next.prev = self.head

            # Add the new node to the end
            new_node = Node(key, value)
            self.cache[key] = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node

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