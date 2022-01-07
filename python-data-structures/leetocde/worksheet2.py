
def next_permutation(nums: list) -> list:
    def find_lowest_gt(nums, idx):
        lowest = idx
        for i in range(idx + 1, len(nums)):
            if nums[i] 

    def sort()
    
    last_idx, max_val = None, None
    for i in range(len(nums) - 1, -1, -1):
        last_idx = i
        if max_val and max_val > nums[i]:
            idx = find_lowest_gt(nums, i)
            nums[i], nums[idx] = nums[idx], nums[i]
            break
        else:
            max_val = nums[i]
    sort(nums, i + 1)


print(next_permutation([1,3,2]))