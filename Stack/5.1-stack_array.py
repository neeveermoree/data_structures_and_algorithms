class Stack:
    __slots__ = '_data', '_length'
    def __init__(self):
        self._data = []
        self._length = 0
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return self._length == 0
    
    def push(self, val):
        self._data.append(val)
        self._length += 1
    
    def top(self):
        if self.is_empty():
            print('Stack is empty')
            return
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return
        self._length -= 1
        return self._data.pop()


stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
print(len(stack))
print(stack.pop())
print(stack.top())
print(stack.pop())
print(stack.is_empty())
stack.top()
stack.pop()
