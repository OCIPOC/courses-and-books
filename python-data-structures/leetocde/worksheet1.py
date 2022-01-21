def can_jump(nums: list) -> bool:
    res = set()
    last = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= last:
            res.add(i)
        for j in res:
            if i + nums[i] >= j:
                res.add(i)
                break
    return 0 in res



print(can_jump([2,3,1,1,4]))
print(can_jump([3,2,1,0,4]))