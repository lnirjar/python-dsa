class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        for index, (k, v) in enumerate(self.arr[hash]):
            if k == key:
                self.arr[hash][index] = (key, val)
                return
        self.arr[hash].append((key, val))

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for k, val in self.arr[hash]:
            if k == key:
                return val
        return None
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for index, (k, v) in enumerate(self.arr[hash]):
            if k == key:
                del self.arr[hash][index]
                return
    
    def print(self):
        print(list(enumerate(self.arr)))

if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.print()
    hash_table['march 6'] = 20
    hash_table.print()
    hash_table['march 17'] = 40
    hash_table.print()
    print(hash_table['march 6'])
    print(hash_table['march 17'])
    hash_table['march 17'] = 50
    hash_table.print()
    hash_table['may 3'] = 70
    hash_table.print()
    hash_table['may 4'] = 80
    hash_table.print()
    del hash_table['march 6']
    hash_table.print()
    del hash_table['march 17']
    hash_table.print()
    