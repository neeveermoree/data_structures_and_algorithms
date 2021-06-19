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
        if node:
            print(node._val, end=' ')
            self.preorder_traversal(node._left)
            self.preorder_traversal(node._right)
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node._left)
            print(node._val, end=' ')
            self.inorder_traversal(node._right)
            

"""
    Tree structure:
                        1
            
            2                       3
    
    4               5       6               7
"""

node4 = _Node(4)
node5 = _Node(5)

node6 = _Node(6)
node7 = _Node(7)

node2 = _Node(2, node4, node5)
node3 = _Node(3, node6, node7)

node1 = _Node(1, node2, node3)

bt = BinaryTree(node1)

print('Preorder traversal')
bt.preorder_traversal(bt._root)
print('\nInorder traversal')
bt.inorder_traversal(bt._root)
