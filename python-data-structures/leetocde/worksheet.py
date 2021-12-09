from typing import NamedTuple

class Node(NamedTuple):
    x: int
    next: NamedTuple

n = Node(1, None)
print(n)

n.next = Node(2, None)
print(n)
