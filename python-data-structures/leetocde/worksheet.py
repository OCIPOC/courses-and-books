from queue import LifoQueue

stack = LifoQueue(10)
stack.put(1)
print(stack.qsize())
