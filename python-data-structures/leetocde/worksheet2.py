from typing import NamedTuple


def has_missing_values(nums: list) -> bool:
    result = [0 for _ in nums]
    for num in nums:
        if num < len(result) - 1 and num > 0:
            result[num] = 1
        else:
            return True
    return sum(result) < len(nums) - 1