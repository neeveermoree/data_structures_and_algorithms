class _Node:
    __slots__ = ('_val', '_next_node', '_previous_node')
    def __init__(self, val, next_node=None, previous_node=None):
        self._val = val
        self._next_node = next_node
        self._previous_node = previous_node


# Circular
class DoublyLinkedList:
    __slots__ = ('_length', '_head', '_tail')
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._length

    def display(self):
        if not len(self):
            print("Doubly Linked List is empty")
            return None
        elif len(self) == 1:
            print(f'{self._head._val} -> ')
            return None
        s = f'{self._head._val} -> '
        cur_node = self._head
        while cur_node._next_node != self._head:
            cur_node = cur_node._next_node
            s += f'{cur_node._val} -> '
        print(s)
    
    def display_reverse(self):
        if not len(self):
            print("Doubly Linked List is empty")
            return None
        elif len(self) == 1:
            print(f'{self._tail._val} -> ')
            return None
        s = f'{self._tail._val} -> '
        cur_node = self._tail
        while cur_node._previous_node != self._tail:
            cur_node = cur_node._previous_node
            s += f'{cur_node._val} -> '
        print(s)
    
    def add_last(self, val):
        node = _Node(val)
        if not len(self):
            self._head = node
            self._tail = self._head
        self._tail._next_node = node
        self._head._previous_node = node
        node._previous_node = self._tail
        node._next_node = self._head
        self._tail = node
        self._length += 1
    
    def add_first(self, val):
        node = _Node(val)
        if not len(self):
            self._head = node
            self._tail = self._head
        self._head._previous_node = node
        self._tail._next_node = node
        node._previous_node = self._tail
        node._next_node = self._head
        self._head = node
        self._length += 1


node = _Node(0)
dll = DoublyLinkedList()
print(len(dll))
dll.display()
dll.add_last(1)
dll.display()
dll.add_last(2)
dll.display()
dll.add_last(3)
dll.display()
print(len(dll))
dll.display_reverse()
dll.add_first(4)
dll.display()
dll.display_reverse()
dll2 = DoublyLinkedList()
dll2.add_first(999)
dll2.display()
print(len(dll2))
