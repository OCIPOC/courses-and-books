def fb1(n: int) -> list:
    if n <= 1:
        return n
    else:
        return fb1(n - 1) + fb1(n-2)

def fb2(n: int) -> list:
    prev1, prev2 = 0, 1
    current = 0
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return current

print(fb1(7))
print(fb2(7))
