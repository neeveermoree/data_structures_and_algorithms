class Node:
    __slots__ = ('_val', '_next_node')
    def __init__(self, val, next_node=None):
       self._val = val
       self._next_node = next_node
