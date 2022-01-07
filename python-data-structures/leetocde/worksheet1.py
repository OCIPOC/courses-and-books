nums = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b'), (1, 'b')]

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums.sort(key=lambda x: x[1])
print(nums)

nums.sort(key=lambda x: (x[1], x[0]))
print(nums)