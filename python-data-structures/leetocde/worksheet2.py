from collections import OrderedDict

cache = OrderedDict()
cache[1] = 1

print(cache)

cache.move_to_end(1)
print(cache)


cache.popitem()
print(cache)