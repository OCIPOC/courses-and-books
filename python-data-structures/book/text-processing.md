# Text Processing

## Abundance of Digitized Text
Processing, indexing, analyzing, and archiving texts are usual tasks for software applications. Dealing with data volumes of PB and more are regular today. So we need efficient algorithms to deal with texts. Character strings are fair representation of text. For example, in python text can be represented by a [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) class.

## Pattern-Matching Algorithms
In the classic pattern-matching problem, we are given a text string T of length n and a pattern string P of length m, and want to find whether P is a substring of T. If so, we may want to find the lowest index j within T at which P begins, such that T[j:j+m] equals P, or perhaps to find all indices of T at which pattern P begins.  

### Brute Force
In brute force we just find all possible solutions. The brute force runs  with the Time Complexity of 
O(nm) where n is the length of text T and m is the length of pattern P.
```Python
def find_brute(T, P):
    n, m = len(T), len(P) 
    for i in range(n−m+1):
        k = 0
        while k < m and T[i + k] == P[k]: 
            k += 1 
            if k == m:
                return i 
    return −1
```
### The Boyer-Moore Algorithm



## Dynamic Programming

## Text Compression and the Greedy Method

## Tries