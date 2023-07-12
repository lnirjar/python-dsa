# Implement hash table where collisions are handled using linear probing. 
# We learnt about linear probing in the video tutorial. 
# Take the hash table implementation that uses chaining and modify methods to use linear probing. 
# Keep MAX size of arr in hashtable as 10.

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [(None, None) for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for i in self.indexes_generator(hash):
            k, v = self.arr[i]
            if k == key:
                return v

    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        # if key is present in hash table, then update the existing (k, v)
        for i in self.indexes_generator(hash):
            k, v = self.arr[i]
            if k == key:
                self.arr[i] = (key, val)
                return
        # if key is not found, then insert (k, v) in available empty slot
        for i in self.indexes_generator(hash):
            k, v = self.arr[i]
            if k is None:
                self.arr[i] = (key, val)
                return
        print('Memory full')

    def __delitem__(self, key):
        hash = self.get_hash(key)
        for i in self.indexes_generator(hash):
            k, v = self.arr[i]
            if k == key:
                self.arr[i] = (None, None)
                return
            
    def indexes_generator(self, hash):
        for i in range(hash, hash + self.MAX):
            yield i % self.MAX 
    
    def print(self):
        # print(list(enumerate(self.arr)))
        print(self.arr)

if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['march 6'] = 10
    hash_table.print()
    hash_table['march 17'] = 20
    hash_table.print()
    del hash_table['march 6']
    hash_table['march 17'] = 50
    hash_table.print()
    print(hash_table['march 6'])
    print(hash_table['march 17'])
    hash_table['may 3'] = 30
    hash_table.print()
    hash_table['may 4'] = 40
    hash_table.print()
    hash_table['may 5'] = 50
    hash_table['may 6'] = 60
    hash_table['may 7'] = 70
    hash_table['may 8'] = 80
    hash_table['may 9'] = 90
    hash_table['may 10'] = 100
    hash_table['may 11'] = 110
    hash_table.print()
    hash_table['may 12'] = 120
    hash_table['may 13'] = 130
    hash_table['may 11'] = 1111
    hash_table.print()
