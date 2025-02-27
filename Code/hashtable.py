#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        # each bucket is a linked list that can store multiple items
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) where n is total number of key-value entries,
    because we need to traverse all buckets and entries.
"""
        all_values = []
         # loop through each bucket
        for bucket in self.buckets:       
        # look at each key-value pair in the bucket
        # ignore the key and add the value to a list
            for key, value in bucket.items():  
                all_values.append(value)    
        return all_values




    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        total = 0
        # count each item in each bucket and return the total
        for bucket in self.buckets:        
            for item in bucket.items():     
                total += 1                  
        return total


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find which bucket the key would be in
        index = self._bucket_index(key)    
        # Get that bucket
        bucket = self.buckets[index]       
        # Look through items in that bucket for the key
        for bucket_key, value in bucket.items():
            if bucket_key == key:
                return True
        return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
         # Find bucket
        index = self._bucket_index(key)   
        bucket = self.buckets[index]
        # Look for key in that bucket
        for bucket_key, value in bucket.items():
            if bucket_key == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)    # Find bucket
        bucket = self.buckets[index]
        # Look for key in that bucket
        for i, (bucket_key, val) in enumerate(bucket.items()):
            if bucket_key == key:          # If found, update value
                bucket.delete((bucket_key, val))
                bucket.append((key, value))
                return
        # If not found, add new pair
        bucket.append((key, value))



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)    # Find the bucket
        bucket = self.buckets[index]
        
        # Look for the key in the bucket
        for item_key, value in bucket.items():
            if item_key == key:
                bucket.delete((item_key, value))  # Use our LinkedList delete
                return
                
        # If we get here, key wasn't found
        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
