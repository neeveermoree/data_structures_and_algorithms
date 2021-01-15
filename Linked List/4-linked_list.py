class _Node:
    __slots__ = ('_val', '_next_node')

    def __init__(self, val, next_node=None):
       self._val = val
       self._next_node = next_node


class LinkedList:
    __slots__ = ('_head', '_tail', '_length')
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return len(self) == 0
    
    def add_node_end(self, val):
        new_node = _Node(val)
        # with self._head only
        """
        head = self._head
        if head is None:
            self._head = new_node
        else:
            while not head._next_node is None:
                head = head._next_node
            head._next_node = new_node
        """
        # with self._tail
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next_node = new_node
        self._tail = new_node
        self._length += 1

    def display(self):
        print('Total Length:', len(self))
        head = self._head
        while not head is None:
            print(head._val, end='')
            if head._next_node is None:
                print()
            else:
                print(' -> ', end='')
            head = head._next_node
    
    def search(self, val):
        node_idx = 0
        head = self._head
        while head:
            if head._val == val:
                return node_idx
            node_idx += 1
            head = head._next_node
        return -1

    def add_node_start(self, val):
        new_node = _Node(val)
        if self.is_empty(): 
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next_node = self._head
            self._head = new_node
        self._length += 1

    def add_node_position(self, val, idx):
        node_idx = 1
        head = self._head
        while node_idx < idx:
            node_idx += 1
            head = head._next_node
        new_node = _Node(val, head._next_node)
        head._next_node = new_node
        self._length += 1    

    def delete_first(self):
        if len(self) == 0:
            return None
        head = self._head
        self._head = head._next_node
        self._length -= 1
        return head._next_node


ll = LinkedList()
print(ll.is_empty())
ll.display()
ll.add_node_start(12)
print(ll.is_empty())
ll.display()
ll.add_node_end(123)
ll.add_node_end(1234)
ll.display()
print(ll.search(123))
print(ll.search(234))
ll.add_node_start(1)
ll.display()
ll.add_node_position(42, 2)
ll.display()
ll.delete_first()
ll.display()
