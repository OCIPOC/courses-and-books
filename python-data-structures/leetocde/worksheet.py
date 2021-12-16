class Node:
    def __init__(self, element, next=None) -> None:
        self.element: str = element
        self.next: Node = next

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

    def __str__(self):
        s = []
        current = self.head
        while current:
            s.append(str(current.element))
            current = current.next
        return '->'.join(s)


s = Stack()
print(s)

print(s.push(1), s)
print(s.push(2), s)
print(s.push(3), s)
print(s.len(), s.pop(), s)
print(s.len(), s.pop(), s)
print(s.len(), s.pop(), s)
print(s.len())