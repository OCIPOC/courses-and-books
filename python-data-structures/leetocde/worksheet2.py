
def load_numbers(nums: list) -> list:
    d = {}
    for i, v in enumerate(nums):
        if v in d:
            d[v].add(i)
        else:
            d[v] = set([i])
    return d


def tree_sum(nums: list) -> list:
    d = load_numbers(nums)
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            num = 0 - (nums[i] + nums[j])
            if num in d:
                for k in num[d].difference([i, j]):
                    res.append([i, j, k])
    return res

