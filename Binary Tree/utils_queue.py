class _Node:
    __slots__ = '_val', '_next_node'
    def __init__(self, val, next=None):
        self._val = val
        self._next_node = next


class Queue:
    __slots__ = '_length', '_first', '_last'
    def __init__(self):
        self._length = 0
        self._first = None
        self._last = None
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return self._length == 0
    
    def first(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        return self._first._val
    
    def enqueue(self, val):
        node = _Node(val)
        if self.is_empty():
            self._first = node
            self._last = self._first
        self._last._next_node = node
        self._last = node
        self._length += 1
    
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        value = self._first._val
        self._first = self._first._next_node
        self._length -= 1
        return value
