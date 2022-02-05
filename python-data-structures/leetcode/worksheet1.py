def max_prod(nums: list) -> int:
    if not nums:
        return 0
    else:
        res, mx, mn = nums[0], nums[0], nums[0]
        for curr in nums[1:]:
            print(curr, mx, mn, res)
            mx = max(curr, curr*mx, curr*mn)
            mn = min(curr, curr*mn, curr*mx)
            res = max(mx, res)
    return res


def max_prod2(nums: list) -> list:
    res = None
    for i in range(len(nums)):
        curr = 1
        for j in range(i, len(nums)):
            curr *= nums[j]
        
        if res is None or curr > res:
            res = curr
    return res 


print(max_prod2([2,-5,-2,-4,3]))
print(max_prod([2,-5,-2,-4,3]))