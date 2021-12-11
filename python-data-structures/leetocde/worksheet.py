def f(x: int, d = {}) -> dict:
    d[x] = str(x)
    return d


print(f(1))