class _Node:
    __slots__ = '_val', '_next_node'
    def __init__(self, val, next=None):
        self._val = val
        self._next_node = next

class Stack:
    __slots__ = '_length', '_top_node'
    def __init__(self):
        self._length = 0
        self._top_node = None
    
    def __len__(self):
        return self._length
    
    def is_empty(self):
        return self._length == 0
    
    def top(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        return self._top_node._val
    
    def push(self, val):
        next_node = None if self.is_empty() else self._top_node
        node = _Node(val, next_node)
        self._top_node = node
        self._length += 1
    
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        value = self._top_node._val
        self._top_node = self._top_node._next_node
        self._length -= 1
        return value


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
