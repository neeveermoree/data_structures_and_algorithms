class _Node:
    __slots__ = ('_val', '_next_node', '_previous_node')
    def __init__(self, val, next_node=None, previous_node=None):
        self._val = val
        self._next_node = next_node
        self._previous_node = previous_node


class DoublyLinkedList:
    __slots__ = ('_length', '_head', '_tail')
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._length
    

node = _Node(0)
dll = DoublyLinkedList()
print(len(dll))
