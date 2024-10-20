"""
An example of a very basic hash table as an abstract data type.

We utilise an in-built python List with a default starting size of 1024.

The hash function is a simple character addition method, which is flawed in that a reversed string,
or a set of characters, whose combined "ord" positions add up to the same number, will be placed in the same index.

But for the sake of demonstration it works. 

(A slightly improved method would be to insert another List inside the colliding index,
with each element an array where the 0th index is the full string key, and the 1st being the value.)

Upon adding a key=>value it checks if there are enough blocks in the array for the calculated index, if not, 
it appends None values up to that index.

"""

class HashTable:
    def __init__(self, size=1024):
        self.table = []
        self.init_range(0, size-1)
        
    def init_range(self, i_start, i_end):
        for i in range(i_start, i_end):
            self.table.append(None)
        return self
    
    def get(self, key):
        return self.table[self.get_index(key)]
        
    @staticmethod
    def get_index(str):
        index = None
        for s in str:
            if index is None:
                index = ord(s)
            else:
                index += ord(s)
        return index
    
    def last_index(self):
        return len(self.table)-1
        
    def ensure_index_is_available(self, index):
        if len(self.table) > index:
            self.init_range(
                self.last_index(), 
                index)
        return self
            
    def add(self, key, value):
        index = self.get_index(key)
        self.ensure_index_is_available(index)
        self.table[index] = value


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add('hamburger', '£1.50')
    hash_table.add('nuggets', '£0.75')
    hash_table.add('pizza', '£12.50')

for food in ['hamburger', 'nuggets', 'pizza']:
  print(f"{food} costs {hash_table.get(food)}")
"""
Output:
hamburger costs £1.50
nuggets costs £0.75
pizza costs £12.50
"""
