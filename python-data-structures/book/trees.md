# Trees

## Introduction
In many different domains, we need to organize data in hierarchical structures. Think for example, about big organizations,file systems, data bases, class hierarchies, family tries etc. Linear data structures like arrays, queues, and linked lists aren't expressive enough to represent such data. 

## General Trees
Tree is a data structure that consists of a root and nodes. Root is a special node that has no parent. All other nodes have exactly one parent and 0 or more children. Children that share the same parent are called siblings. Nodes that have no children are called leaves. Nodes that have children are called internal nodes.
```Python
class TreeNode
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent: TreeNode = parent
        self.children: list = children
``` 
A tree is <em>ordered</em> if there is a meaningful linear order among the children of each node; that is, we purposefully identify the children of a node as being the first, second, third, and so on. 
The tree T then supports the following accessor methods:
- T.root: returns 

## Binary Trees
A Binary Tree is a Tree that has root and 

## Implementing Trees

## Tree traversal algorithms

## Example: Expression Trees



