def find_larger_right(nums) -> int:
            for i in range(len(nums) - 1, -1, -1):
                if i > 0 and nums[i] > nums[i-1]:
                    return i-1  
            return 0
        
def sort_from_index(idx, nums):
    for i in range(idx, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

def next_perm(nums: list):
    idx = find_larger_right(nums)
    
    start = idx + 1 if idx != 0 else 0
    sort_from_index(start, nums)
    
    print(idx, nums)
    if idx > 0:
        for i in range(idx + 1, len(nums)):
            if nums[idx] < nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]

nums = [3, 2, 1]
next_perm(nums)
print(nums)

'''
nums = [1,2,3]
next_perm(nums)
print(nums)

nums = [1,1,5]
next_perm(nums)
print(nums)
'''


