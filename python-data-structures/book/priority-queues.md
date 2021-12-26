# Priority Queues

## Introduction
A Queue is a basic concept in software engineering. When we haven't enough resources to supply at once, we create a waiting list. As a simple approach, we create a queue that is managed by a [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) principle. By using a FIFO principle, each new item goes to the back of the queue. Once there is an available resource, items are fecthed from the head of the queue and served. Sometimes, not all queue items are equal. Some items are more important and should get resources as soon as possible. 

## The Priority Queue Abstract Data Type
A Priority Queue P is defined in the following way:
- P.add(k, v) - inserts and item with the key k and value v
- P.min() - returns a tuple (k,v) with the minimal key k
- P.remove_min() - performs P.min() and remove the element from the queue  
- P.is_empty() - check of P is empty
- len(P) - returns the number of items in queue

Sorted and Unsorted lists implementation of Priority Queues:
| Operation | Sorted Queues | Unsorted Queues |
| :-------: | :-----------: | :-------------: |
| add       | O(n)          | O(1)            |
| min       | O(1)          | O(n)            |
| rem_min   | O(1)          | O(n)            |
| is_empty  | O(1)          | O(1)            |
| len       | O(1)          | O(1)            |

Both implementations have at least one operation with the time complexity of O(n). The question is it possible to create a data structure that can do all of these operations more efficiently.


## Heaps
Heaps are [complete binary trees](https://www.programiz.com/dsa/complete-binary-tree) for which every parent node has a value less than or equal to any of its children.
Heaps implementation of Priority Queues:
| Operation | Sorted Queues | Unsorted Queues | Heaps    |
| :-------: | :-----------: | :-------------: | :---:    |
| add       | O(n)          | O(1)            | O(log n) |
| min       | O(1)          | O(n)            | O(log n) |
| rem_min   | O(1)          | O(n)            | O(log n) |
| is_empty  | O(1)          | O(1)            | O(1)     |
| len       | O(1)          | O(1)            | O(1)     |




## Python heapq




##  Sorting with a Priority Queue

## Adaptable Priority Queues


