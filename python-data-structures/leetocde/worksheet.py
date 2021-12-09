from typing import NamedTuple
class Node(NamedTuple):
    x: int
    next: NamedTuple

n = Node(1, Node(2, None))

while n:
    print('Current', n.x, n.next)
    n = n.next

