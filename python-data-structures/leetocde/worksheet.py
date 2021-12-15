class ArrayStack:
    def __init__(self, capacity: int) -> None:
        self.stack = [None for i in range(capacity)]
        self.top_idx = -1
    
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
        if self.length == len(self.stack):
            raise Exception('stack is full')
        self.top_idx += 1
        self.stack[self.top_idx] = x

    def length(self):
        return self.top_idx + 1
    
    def is_empty(self):
        return self.top_idx == -1


stack = ArrayStack(10)
assert stack.length() == 0
assert stack.is_empty() == True

for i in range(10):
    stack.push(i)
    assert stack.top() == i
    assert stack.length() == i + 1
    assert stack.is_empty() == False

