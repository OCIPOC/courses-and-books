def fourSum(nums: list, target: int) -> list:
    nums.sort()

    def two_sum(nums: list, target: int, start) -> list:
        res = []
        stop = len(nums) - 1
        while start < stop:
            if nums[start] + nums[stop] == target:
                res.append([nums[start], nums[stop]])
                start, stop = start + 1, stop - 1
            elif nums[start] + nums[stop] > target:
                stop -= 1
            else:
                start += 1
        return res
        
    res = []
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            tmp_target = target - (nums[i] + nums[j])
            if tmp_target < 0:
                continue
            else:
                tmp_res = two_sum(nums, tmp_target, j + 1)     
                res.append([[nums[i], nums[j]] + x for x in tmp_res if x])
    return res


fourSum([1,0,-1,0,-2,2], 0)