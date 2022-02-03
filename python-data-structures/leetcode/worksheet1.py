def trap(height: list) -> int:
    res = 0
    for i in range(1, len(height) - 1):
        left_max = max(height[:i])
        right_max = max(height[i+1:])
        if right_max > height[i] and left_max > height[i]:
            res += min(left_max, right_max) - height[i]
    return res


assert trap([4,2,0,3,2,5]) == 9
assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6