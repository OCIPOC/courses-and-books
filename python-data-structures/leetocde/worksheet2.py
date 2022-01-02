def subtract(x, y):
    if y == 0:
        return x
    else:
        return subtract(x ^ y, ((~x) & y) << 1)


def divide(x, y):
    res = 0
    while x > 0:
        x = subtract(x, y)
        res += 1
    return res

print(subtract(10, -2))
print(divide(600, 15))


