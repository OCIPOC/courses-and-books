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


## Circularly Linked Lists
