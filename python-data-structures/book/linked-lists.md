# Linked Lists

## Introduction
[Stacks, Queues, and Deques](https://github.com/dimastatz/courses-and-books/blob/master/python-data-structures/book/stack-queues-deques.md) are fundamental data structures that can be implemented by using [Arrays](https://github.com/dimastatz/courses-and-books/blob/master/python-data-structures/book/array-based-sequences.md). The drawback of using arrays as an underlying structure is poor performance when size changes frequently. Both increase and shrink have the time complexity of O(n). Another way to implement stack, queues, and deques, is by using linked lists.

## Singly Linked Lists
A singly linked list is a collection of nodes that collectively form a linear sequence. Each node stores a value and a reference to the next node of the list.

```Python
class Node:
    def __init__(self, element, next=None):
        self.element: str = element
        self.next: Node = next
```
In Python you can find a linked list implementationin in [collection.deque](https://github.com/python/cpython/blob/main/Modules/_collectionsmodule.c#L71). Deque can be used as stack and queue. Implementing stack and queue using linked lists is easy. For example, see stack implementation:
```Python
class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.head: Node = None
        
    def push(self, element):
        node = Node(element, None)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            raise Exception('stack is empty')
        self.size -= 1
        item = self.head
        self.head = self.head.next
        return item.element

    def top(self):
        if self.size == 0:
            raise Exception('stack is empty')
        return self.head.element

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0
```


## Circularly Linked Lists
