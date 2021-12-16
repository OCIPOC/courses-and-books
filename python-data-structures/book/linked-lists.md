# Linked Lists

## Introduction
The most fundamental data structures are array-based sequences. Array-based sequences allow accessing elements by index in constant time. [Stacks, Queues and Deques](https://github.com/dimastatz/courses-and-books/blob/master/python-data-structures/book/stack-queues-deques.md) can be implemented by using arrays. The drawback of arrays is poor performance when a size change is needed frequently. Both increase and shrink have the time complexity of O(n). So, if random access is not needed, but it is important to change the size efficiently, linked-list is a data structure to go with.

## Singly Linked Lists
A singly linked list is a collection of nodes that collectively form a linear sequence. Each node stores a value and a reference to the next node of the list.

```Python
class Node:
    def __init__(self, element, next=None):
        self.element: str = element
        self.next: Node = next
```


## Circularly Linked Lists
