from time import sleep

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(nums: list, start, end, msg = '') -> TreeNode:
    print(nums, start, end, msg)
    sleep(1)
    if start < end:
        mid = (end - start) // 2
        left = build(nums, start, mid, 'l')
        right = build(nums, mid + 1, end, 'r')
        return TreeNode(nums[mid], left, right)
    else:
        return None


nums = [-10,-3,0,5,9]
print(build(nums, 0, len(nums)-1))