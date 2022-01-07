# Sorting and Selection

## Introduction

## Merge Sort

## Quick Sort

## Comparing Sorting

## Python Built-in Sorting
Python has two ways for sorting. The first one is by using sort() function of the list class. This is in place sorting:
```Python
nums = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b')]
nums.sort() # nums = []
nums.sort(reverse=True) # 
nums.sort(key=lambda x: x[1])
```
This method reordering the elements of the list by using <em><</em> operator. Python also has more general <em>sorted</em> function. It can be used with any sequence and it is immutable. This function return the sorted version of the inyt sequence
```Python
sorted('green') # -> ['e', 'e', 'g', 'n', 'r']
nums = [1, 3, 2]
sorted(nums) # -> [1, 2, 3] and nums=[1, 3, 2]
```

## Selection