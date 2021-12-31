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
In applications where one cannot guarantee the random nature of updates, it is better to rely on variations of search trees

## Balanced Search Trees


## AVL Trees

## Splay Trees

## (2,4) Trees

## Red-Black Trees