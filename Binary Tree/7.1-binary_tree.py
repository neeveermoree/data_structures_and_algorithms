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

    def preorder_traversal(self, node):
        if node is not None:
            print(node._val, end=' ')
            self.preorder_traversal(node._left)
            self.preorder_traversal(node._right)
            

left_node = _Node(2)
right_node = _Node(3)
root_node = _Node(1, left_node, right_node)
bt = BinaryTree(root_node)
bt.preorder_traversal(bt._root)
