def trap(height: list) -> int:
    
    total = 0
    left = 0
    right = len(height) - 1
    maxl = 0
    maxr = 0
    
    while left < right:
        if height[left] <= height[right]:
            if height[left] > maxl:
                maxl = height[left]
            else:
                total += maxl - height[left]
            left +=1
        else:
            if height[right] > maxr:
                maxr = height[right]
            else:
                total += maxr - height[right]
            right -=1
    return total


assert trap([4,2,0,3,2,5]) == 9
assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6