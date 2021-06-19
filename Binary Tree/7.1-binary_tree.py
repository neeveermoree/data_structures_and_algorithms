from utils_queue import Queue


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
            
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node._left)
            self.postorder_traversal(node._right)
            print(node._val, end=' ')
    
    def levelorder_traversal(self, node_list):
        if not len(node_list):
            return
        new_node_list = []
        for node in node_list:
            if not node:
                continue
            print(node._val, end=' ')
            new_node_list.append(node._left)
            new_node_list.append(node._right)
        self.levelorder_traversal(new_node_list)
    
    def levelorder_traversal_queue(self):
        queue = Queue()
        if self._root:
            queue.enqueue(self._root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node:
                print(node._val, end=' ')
                queue.enqueue(node._left)
                queue.enqueue(node._right)


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
print('\nPostorder traversal')
bt.postorder_traversal(bt._root)
print('\nLevelorder traversal')
bt.levelorder_traversal([bt._root])
print('\nLevelorder traversal queue')
bt.levelorder_traversal_queue()


"""
    Another tree structure
                                1

                    2                       3

            4                                           6
"""

node_4 = _Node(4)
node_2 = _Node(2, left=node_4)

node_6 = _Node(6)
node_3 = _Node(3, right=node_6)

node_1 = _Node(1, node_2, node_3)

bt_ = BinaryTree(node_1)

print('\nPreorder traversal')
bt_.preorder_traversal(bt_._root)
print('\nInorder traversal')
bt_.inorder_traversal(bt_._root)
print('\nPostorder traversal')
bt_.postorder_traversal(bt_._root)
print('\nLevelorder traversal')
bt_.levelorder_traversal([bt_._root])
print('\nLevelorder traversal queue')
bt_.levelorder_traversal_queue()
