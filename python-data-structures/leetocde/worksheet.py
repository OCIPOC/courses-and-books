from _typeshed import Self


class Node:
    def __init__(self, element, next=None) -> None:
        self.element: str = element
        self.next: Node = next

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        
    def add_first(self, element):
        node = Node(element, None)
        
        if self.head:
            node.next = self.head.next
        self.head = node

        if not self.tail:
            self.tail = node
        
    def remove()

