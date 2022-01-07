import bisect

nums = []

for i in [5, 2, 1, 7]:
    print(i, nums, bisect.bisect(nums, i))
    bisect.insort(nums, i)

