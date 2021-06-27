class _Node:
    __slots__ = '_val', '_left', '_right'
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right


class BinarySearchTree:
    __slots__ = '_root'
    def __init__(self, root=None):
        self._root = root
    
    def search_iterative(self, val):
        node = self._root
        while node:
            if val == node._val:
                return True
            elif val < node._val:
                node = node._left
            else:
                node = node._right
        return False        


"""
    Tree structure:
                        5
            
            3                       8
    
    1               4       6               9
"""

node1 = _Node(1)
node4 = _Node(4)

node6 = _Node(6)
node9 = _Node(9)

node3 = _Node(3, node1, node4)
node8 = _Node(8, node6, node9)

node5 = _Node(5, node3, node8)

bt1 = BinarySearchTree(node5)

print(bt1.search_iterative(1))
print(bt1.search_iterative(5))
print(bt1.search_iterative(8))
print(bt1.search_iterative(2))
