def can_jump(nums: list) -> bool:
    if len(nums) == 1:
        return True
    elif not nums:
        return False
    elif nums[0] == 0:
        return False
    else:
        res = []
        for i in range(1, nums[0] + 1):
            res.append(can_jump(nums[i:]))
        return True in res

print(can_jump([2,3,1,1,4]))
print(can_jump([3,2,1,0,4]))