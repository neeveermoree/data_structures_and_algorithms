class DEQue:
    __slots__ = '_length', '_data'
    def __init__(self):
        self._length = 0
        self._data = []
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return len(self) == 0
    
    def first(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        return self._data[0]
    
    def last(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        return self._data[-1]
    
    def enqueue_first(self, val):
        self._data.insert(0, val)
        self._length += 1
    
    def enqueue_last(self, val):
        self._data.append(val)
        self._length += 1
    
    def dequeue_first(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        value = self._data[0]
        self._data.remove(value)
        return value
    
    def dequeue_last(self):
        if self.is_empty():
            print('DEQue is empty')
            return None
        value = self._data.pop()
        return value


deque = DEQue()
deque.enqueue_first(23)
deque.enqueue_last(24)
print(deque.first())
print(deque.last())
deque.dequeue_first()
deque.dequeue_last()
print(deque.is_empty())
