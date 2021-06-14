class _Node:
    __slots__ = '_val', '_left', '_right'
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right


class BinaryTree:
    __slots__ = '_root'
    def __init__(self, root=None):
        self._root = root
