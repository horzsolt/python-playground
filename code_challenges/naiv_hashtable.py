class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return ord(key[0]) % self.size

    def set(self, key, value):
        hash_index = self._hash(key)
        for kvp in self.table[hash_index]:
            if kvp[0] == key:
                kvp[1] = value
                return

        self.table[hash_index].append([key, value])

    def get(self, key):
        hash_index = self._hash(key)
        for kvp in self.table[hash_index]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError(f'Key {key} not found')

    def remove(self, key):
        hash_index = self._hash(key)
        for i, kvp in enumerate(self.table[hash_index]):
            if kvp[0] == key:
                self.table[hash_index].pop(i)
                return

        raise KeyError(f'Key {key} not found')
    
hash_table = HashTable(10)

hash_table.set('Alice', 'January')
hash_table.set('Bob', 'May')

print(hash_table.get('Alice'))  # Outputs: 'January'

hash_table.remove('Bob')

# This will raise a KeyError, as 'Bob' was removed
print(hash_table.get('Bob'))