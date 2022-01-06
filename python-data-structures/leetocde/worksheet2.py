from typing import NamedTuple


nums = [[0, '', 2], [3, 4, 5], [6, 7, 8]]
rows, cols = range(len(nums)), range(len(nums[0]))

print(nums)
print([[nums[i][j] for j in cols if nums[i][j] != ''] for i in rows])
print([[nums[j][i] for j in rows if nums[j][i] != ''] for i in cols])