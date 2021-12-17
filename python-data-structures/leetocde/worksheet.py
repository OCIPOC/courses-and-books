from typing import NamedTuple


class Node:
    def __init__(self, name, count) -> None:
        self.name = name
        self.count = count

class AccessFrequency:
    def __init__(self) -> None:
        self.items = {}

    def access(self, e):
        node = self.items.get(e, [e, ])
        self.items[e] = node[e, ]

    def remove(self, e):
        del self.items[e]

    def top(self, k):
        s = sorted(self.items.items(), key = lambda x: x[1])
        return [x[0] for x in s[:k]]


d = {'a': 1, 'b': 2, 'c': 3}
s = list(sorted(d.items(), key = lambda x: x[1], reverse=True))

print(s[])