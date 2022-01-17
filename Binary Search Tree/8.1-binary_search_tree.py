from copy import deepcopy


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
    
    def search_recursive(self, node, val):
        if not node:
            return False
        if node._val == val:
            return True
        elif val < node._val:
            return self.search_recursive(node._left, val)
        else:
            return self.search_recursive(node._right, val)
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node._left)
            print(node._val, end='')
            self.inorder_traversal(node._right)

    def insert_iterative(self, val):
        new_node = _Node(val)
        node = self._root
        if not node:
            self._root = new_node
            return
        while node:
            if node._val <= val:
                if node._right:
                    node = node._right
                else:
                    node._right = new_node
                    return
            else:
                if node._left:
                    node = node._left
                else:
                    node._left = new_node
                    return
 
    def insert_recursive(self, node, val):
        if node:
            if node._val <= val:
                if not node._right:
                    node._right = _Node(val)
                else:
                    self.insert_recursive(node._right, val)
            else:
                if not node._left:
                    node._left = _Node(val)
                else:
                    self.insert_recursive(node._left, val)
        
    def preorder_traversal(self, node):
        if node:
            print(node._val, end='')
            self.preorder_traversal(node._left)
            self.preorder_traversal(node._right)
    
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node._left)
            self.postorder_traversal(node._right)
            print(node._val, end='')
    
    def levelorder_traversal(self, nodes):
        while len(nodes):
            node = nodes.pop(0)
            print(node._val, end=' -> ')
            if node._left:
                nodes.append(node._left)
            if node._right:
                nodes.append(node._right)
    
    def delete(self, val):
        left = True
        prev_node = self._root
        node = self._root
        while node._val != val:
            prev_node = node
            if node._val == val:
                return node
            elif node._val > val:
                node = node._left
            else:
                node = node._right
        if not node:
            print('No such element in Binary Search Tree')    
            return
        if not node._left and not node._right:
            # remove just the node 
            pass
        elif node._left and node._right:
            # find right node to replace deleted node
            pass
        else:
            # something
            pass

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

print('Iterative Search:')
print(bt1.search_iterative(1))
print(bt1.search_iterative(5))
print(bt1.search_iterative(8))
print(bt1.search_iterative(2))

print('\nRecursive Search:')
print(bt1.search_recursive(bt1._root, 1))
print(bt1.search_recursive(bt1._root, 5))
print(bt1.search_recursive(bt1._root, 8))
print(bt1.search_recursive(bt1._root, 2))

bt2 = deepcopy(bt1)

print('\nInorder Traversal')
bt1.inorder_traversal(bt1._root)
print()

print('\nPreorder Traversal')
bt1.preorder_traversal(bt1._root)
print() 

print('\nPostorder Traversal')
bt1.postorder_traversal(bt1._root)
print()

print('\nLevelorder Traversal')
bt1.levelorder_traversal([bt1._root])
print()

print('\nIterative Insertion')
bt1.insert_iterative(10)
bt1.inorder_traversal(bt1._root)
print()
bt1.insert_iterative(7)
bt1.inorder_traversal(bt1._root)
print()
bt1.insert_iterative(0)
bt1.inorder_traversal(bt1._root)
print()
bt1.insert_iterative(2)
bt1.inorder_traversal(bt1._root)

print('\n\nRecursive Insertion')
bt2.insert_recursive(bt2._root, 10)
bt2.inorder_traversal(bt2._root)
print()
bt2.insert_recursive(bt2._root, 7)
bt2.inorder_traversal(bt2._root)
print()
bt2.insert_recursive(bt2._root, 0)
bt2.inorder_traversal(bt2._root)
print()
bt2.insert_recursive(bt2._root, 2)
bt2.inorder_traversal(bt2._root)
print()

print('\n\nDelete')
bt1.delete(4)
