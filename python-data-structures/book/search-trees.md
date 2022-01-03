# Search Trees

## Introduction
A Tree is a non-linear data structure. It can store hierarchical data. In case when tree nodes are ordered we can use trees for search. Another application is for storing large amounts of data. Unlike arrays, pointer implementation has no upper limit for the number of nodes.

## Binary Search Trees
A binary Search Tree is a Tree data structure whose internal nodes store a key that is greater than all the keys in the node’s left subtree and less than those in its right subtree. On average, a binary search tree with n keys generated from a random series of insertions and removals of keys has expected height O(log n). 
| Operation | Average       | Worst case      |
| :-------: | :-----------: | :-------------: |
| space     | O(n)          | O(n)            |
| search    | O(log n)      | O(n)            |
| delete    | O(log n)      | O(n)            |
| insert    | O(log n)      | O(n)            |  

In applications where one cannot guarantee the random nature of updates, it is better to rely on other variations of search trees

## Balanced Search Trees
BST can be rebalnced by rotation. During a rotation, we “rotate” a child to be above its parent in O(1)
```Python
def rotate(root: Node) -> Node:
    if root and root.left:
        right = root
        root = root.left
        right.left = root.right
        root.right = right
    return root
```
Another way to rebalance is to copy the tree to array by inorder, and then to rebuild the tree by using binary tree build from te middle.


## AVL Trees
AVL is a self-balancing binary search tree (BST) where the heights of the two child subtrees of any node differ by at most one. If at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.
```Python
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):
    ''' Recursive function to insert key in 
    subtree rooted with node and returns
    new root of subtree. '''
    def insert(self, root, key):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
```


## Splay Trees

## (2,4) Trees

## Red-Black Trees