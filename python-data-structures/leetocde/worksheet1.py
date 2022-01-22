def all_perm(nums: list) -> list:
    if not nums:
        return []
    elif len(nums) == 1:
        return [nums]
    else:
        res = []
        for i in range(len(nums)):
            for per in all_perm(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + per)
        return res

def get_change(coins: list, target: int) -> list:
    if target == 0:
        return [[]]
    elif target < 0:
        return [[-1]]
    else:
        res = []
        for i in range(len(coins)):
            for perm in get_change(coins, target - coins[i]):
                if not -1 in perm:
                    res.append([coins[i]] + perm)
        return res

print(get_change([1, 5], 10))

