from functools import reduce

def to_dict(lst: list) -> dict:
    d = {}
    for i, v in enumerate(lst):
        tmp = d.get(v, [])
        d[v] = tmp + [i]
    return d


lst = [1, 2, 1, 3, 4]

print(to_dict(lst))


