def three_sum(nums: list) -> list:
    nums.sort()
    ans = []
        
    for i in range(len(nums)):
        j, k = i+1, len(nums)-1
            
        while j < k:
            if nums[i] + nums[j] + nums[k]  > 0:
                k -= 1                    
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                l = [nums[i],nums[j],nums[k]]
                if l not in ans:
                    ans.append(l)
                j, k = j + 1, k - 1  
    return ans
        
print(three_sum([-1,0,1,2,-1,-4]))