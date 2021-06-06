class Queue:
    __slots__= '_length', '_data'
    def __init__(self):
        self._length = 0
        self._data = []
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return self._length == 0
    
    def first(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        return self._data[0]
    
    def enqueue(self, val):
        self._data.append(val)
        self._length += 1
    
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        value = self.first()
        self._data.remove(value)
        self._length -= 1
        return value


queue = Queue()
queue.first()
queue.enqueue(23)
print(queue.first())
queue.enqueue(24)
print(queue.first())
print(len(queue))
print(queue.dequeue())
print(len(queue))
print(queue.dequeue())
queue.first()
