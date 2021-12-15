from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
print(stack.pop())
print(stack.pop())

stack.append(1)
stack.append(2)
print(stack.popleft())
print(stack.popleft())


