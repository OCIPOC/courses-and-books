class A:
    def __init__(self, name, count) -> None:
        self.name: str = name
        self.count: int = count

    def __lt__(self, other) -> bool:
        return self.count < other.count
    
    def __ge__(self, other) -> bool:
        return self.count >= other.count

x = A('avi', 7)
y = A('ben', 5)

print(y  > x)
