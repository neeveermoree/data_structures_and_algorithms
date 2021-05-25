class _Node:
    __slots__ = ('_val', '_next_node')
    def __init__(self, val, next_node=None):
        self._val = val
        self._next_node = next_node


class CircularLinkedList:
    __slots__ = ('_head', '_length')
    def __init__(self):
        self._head = None
        self._length = 0
    
    def __len__(self):
        return self._length
    
    def add_last(self, val):
        node = _Node(val)
        if not len(self):
            node._next_node = node
            self._head = node
        cur_node = self._head
        while cur_node._next_node != self._head:
            cur_node = cur_node._next_node
        node._next_node = self._head
        cur_node._next_node = node
        self._length += 1

    def display(self):
        if not len(self):
            print('Circular Linked List is empty')
            return None
        cur_node = self._head
        print(f'{cur_node._val} --> ', end='')
        while cur_node._next_node != self._head:
            print(f'{cur_node._next_node._val} --> ', end='')
            cur_node = cur_node._next_node
        print()

    def search(self, val):
        cur_node = self._head
        idx = 0
        while idx < len(self):
            if cur_node._val == val:
                return idx
            cur_node = cur_node._next_node
            idx += 1
        return -1
    
    def add_first(self, val):
        node = _Node(val)
        if not len(self):
            node._next_node = node
            self._head = node
        cur_node = self._head
        while cur_node._next_node != self._head:
            cur_node = cur_node._next_node
        node._next_node = self._head
        cur_node._next_node = node
        self._head = node
        self._length += 1
    
    def add_node_position(self, val, idx):
        node = _Node(val) 
        counter = 0
        cur_node = self._head
        while counter + 1 != idx:
            cur_node = cur_node._next_node
            counter += 1
        node._next_node = cur_node._next_node
        cur_node._next_node = node
        self._length += 1
    
    def delete_from_beginning(self):
        cur_node = self._head
        while cur_node._next_node != self._head:
            cur_node = cur_node._next_node
        cur_node._next_node = self._head._next_node
        self._head = cur_node._next_node
        self._length -= 1
    
    def delete_from_end(self):
        curr_node = self._head
        while curr_node._next_node._next_node != self._head:
            curr_node = curr_node._next_node
        curr_node._next_node = self._head
        self._length -= 1

    def delete_at_idx(self, idx):
        node_id = 0
        curr_node = self._head
        while node_id != (idx - 1):
            node_id += 1
            curr_node = curr_node._next_node
        next_item = curr_node._next_node._next_node
        curr_node._next_node = next_item
        self._length -= 1


cll = CircularLinkedList()
cll.display()
cll.add_last(1)
print(len(cll))
cll.display()
cll.add_last(5)
print(len(cll))
cll.display()
cll.add_last(12)
cll.display()
print(cll.search(5))
print(cll.search(8))
cll.add_first(2)
cll.display()
cll.add_first(5)
cll.display()
cll2 = CircularLinkedList()
cll2.add_first(0)
cll2.display()
cll.add_node_position(3, 2)
cll.display()
cll.add_node_position(2, 8)
cll.display()
cll2.delete_from_beginning()
cll2.display()
cll.delete_from_beginning()
cll.display()
cll.delete_from_end()
cll.display()
cll.delete_at_idx(1)
cll.display()
cll.delete_at_idx(2)
cll.display()
