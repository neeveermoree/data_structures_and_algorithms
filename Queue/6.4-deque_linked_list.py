class _Node:
    __slots__ = '_val', '_next_node'
    def __init__(self, val, next=None):
        self._val = val
        self._next_node = next
    

class DEQue:
    __slots__ = '_length', '_first', '_last'
    def __init__(self):
        self._length = 0
        self._first = None
        self._last = None
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return len(self) == 0
    
    def first(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        return self._first._val

    def last(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        return self._last._val
    
    def enqueue_first(self, val):
        node = _Node(val)
        if self.is_empty():
            self._first = node
            self._last = self._first
            self._first._next_node = self._last
        node._next_node = self._first
        self._first = node
        self._length += 1

    def enqueue_last(self, val):
        node = _Node(val)
        if self.is_empty():
            self._first = node
            self._last = node
            self._first._next_node = self._last
        self._last._next_node = node
        self._last = node
        self._length += 1 
    
    def dequeue_first(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        value = self._first._val
        node = self._first._next_node
        self._first = node
        self._length -= 1
        return value
    
    def dequeue_last(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        curr_node = self._first
        while curr_node._next_node != self._last:
            curr_node = curr_node._next_node
        value = self._last
        self._last = curr_node
        self._length -= 1
        return value


deque = DEQue()
deque.enqueue_first(23)
deque.enqueue_last(24)
print(deque.first())
print(deque.last())
deque.dequeue_last()
deque.dequeue_first()
print(deque.is_empty())
