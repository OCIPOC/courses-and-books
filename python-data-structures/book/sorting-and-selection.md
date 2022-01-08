# Sorting and Selection

## Introduction

## Merge Sort

## Quick Sort

## Comparing Sorting

## Python Built-in Sorting
Python has two ways for sorting. The first one is by using [sort](https://docs.python.org/3/tutorial/datastructures.html) function of the list class. This is in place sorting:
```Python
nums = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b')]
nums.sort() # nums = [(1, 'a'), (1, 'b'), (2, 'b'), (3, 'a'), (4, 'b')]
nums.sort(reverse=True) # nums = [(4, 'b'), (3, 'a'), (2, 'b'), (1, 'b'), (1, 'a')]
nums.sort(key=lambda x: x[1]) # nums = [(3, 'a'), (1, 'a'), (4, 'b'), (2, 'b'), (1, 'b')]
nums.sort(key=lambda x: (x[1], x[0])) # nums = [(1, 'a'), (3, 'a'), (1, 'b'), (2, 'b'), (4, 'b')]
```
This method reordering the elements of the list by using [<](https://docs.python.org/3/library/operator.html) operator. Python also has more general [sorted](https://docs.python.org/3/howto/sorting.html) function. It can be used with any sequence and it is immutable. This function return the sorted version of the inyt sequence
```Python
sorted('green') # -> ['e', 'e', 'g', 'n', 'r']
nums = [1, 3, 2]
sorted(nums) # -> [1, 2, 3] and nums=[1, 3, 2]
```

## Selection