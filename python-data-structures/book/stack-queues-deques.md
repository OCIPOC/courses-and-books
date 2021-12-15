# Stacks, Queues, and Deques

## Introduction
[FIFO](https://en.wikipedia.org/wiki/FIFO_and_LIFO_accounting) first-in-first-out and [LIFO](https://en.wikipedia.org/wiki/FIFO_and_LIFO_accounting) last-in-first-out are methods used in managing inventory and financial matters. For instance, they are used to manage assumptions of costs related to inventory, stock repurchases (if purchased at different prices), and various other accounting purposes. Stack (FIFO) and Queue (LIFO) are fundamental data structures in computer science and are widely used in different scenarios.

## Stack
Stack is a data structure that manages a collections of objects by FIFO principle. Stack supports the following operations:
- push O(1): add new element to the top of the stack
- pop O(1): remove and return the element from the top of the stack
- top O(1): return and element from the top of stack
- is_empty O(1): return true if stack is empty, otherwise return false
- length O(1): return the number of elements in the stack
In Python we can implement stack using list:
```python
class ArrayStack:
    def __init__(self, capacity: int) -> None:
        self.top_idx = -1
        self.stack = [None for i in range(capacity)]
        
    def top(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.stack[self.top_idx]
    
    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')   
        self.top_idx -= 1
        return self.stack[self.top_idx + 1]
    
    def push(self, x):
        if self.length() == len(self.stack):
            raise Exception('stack is full')
        self.top_idx += 1
        self.stack[self.top_idx] = x

    def length(self):
        return self.top_idx + 1
    
    def is_empty(self):
        return self.top_idx == -1
```

