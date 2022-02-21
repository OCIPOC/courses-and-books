
class Node:
    def __init__(self, x) -> None:
        self.x = x

tmp = Node(3)
lst = [Node(1), Node(2), tmp]

print(lst.index(tmp))

