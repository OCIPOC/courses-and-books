from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(m, len(nums1)):
        print(i, m, i -m)
        nums1[i] = nums2[i - m]

    nums1.sort()
    print(nums1)


print(merge(nums1=[1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n=3))