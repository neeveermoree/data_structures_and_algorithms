class _Node:
    __slots__ = ('_val', '_next_node', '_previous_node')
    def __init__(self, val, next_node=None, previous_node=None):
        self._val = val
        self._next_node = next_node
        self._previous_node = previous_node


node = _Node(0)
