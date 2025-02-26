#!python


class Node(object):
# create Node objects, each one holds data (the values) and a reference (pointer to the next node)
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
       Running time: O(n) where n is the number of nodes in the linked list
    because we must traverse through each node once to count it."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
         Running time: O(1) maintain a tail pointer will always be O(1) as long as the tail node is tracked
        and appends only happen at the end of the list"""
        new_node = Node(item)
    
        if self.is_empty():
            # list is empty, set both head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # add new node after tail
            self.tail.next = new_node
            self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1), maintain a head pointer will always be O(1) as long as the head node is tracked
        and appends only happen at the beginning of the list"""
        new_node = Node(item)
    
        if self.is_empty():
            # List is empty, set both head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # Add new node before head
            new_node.next = self.head
            self.head = new_node


    def find(self, matcher):
        """Return an item from this linked list if it is present.
        Running time: 
    Best case: O(1) when the item is at the head
    Worst case: O(n) when:
    1. Item is at the tail
    2. Item isn't in the list at all
    3. We have to check every node to find it"""

        current = self.head       # O(1) - start at head
    
        while current is not None:  # Loop through all nodes
            if current.data == matcher:  # O(1) - check if current node matches
                return True
            current = current.next      # O(1) - move to next node
        
        return False  # Item not found after checking all nodes



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Running time: O(n) because we might need to traverse the whole list.
    Under what conditions: Best case O(1) if item is at head, worst case O(n) 
    if item is at tail or not found.
"""
        current = self.head
        previous = None
        found = False

        # Find the node to delete
        while current is not None:
            if current.data == item:
                found = True
                break
            previous = current
            current = current.next

        if not found:
            raise ValueError('Item not found: {}'.format(item))

        # Update head/tail if needed
        if previous is None:  # Deleting head
            self.head = current.next
        else:  # Deleting non-head node
            previous.next = current.next

        # Update tail if needed
        if current.next is None:  # If we're deleting the tail
            self.tail = previous



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
