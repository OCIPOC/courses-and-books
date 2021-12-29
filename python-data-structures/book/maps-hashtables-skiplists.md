# Maps, Hash Tables, and Skip Lists

## Introduction
There are a lot of scenarios in software engineering when we need to map a key to a certain value. Consider a lookup table that maps countries to currencies, ip addresses to geo-locations, phone models to os names, etc. We note that the keys (the country names) are assumed to be unique, but the values (the currency units) are not necessarily unique

## Maps and Dictionaries
Python's [dict class](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) represents an abstraction known as a dictionary in which unique keys are mapped to associated values. Consider the problem of counting the number of occurrences of words in a list.
```Python
def count_words(text: str) -> dict:
    d = {}
    for w in text.split(' '):
        count = d.get(w, 0)
        d[w] = count + 1
    return d
```

## Hash Tables
A very naive implementation of Hash Tables is based on arrays. Array indices are keys of Hash Tables and values are elements of the array. We have two challenges in such a scenario. <strong>First</strong>, we may not wish to devote an array of length N if it is the case that N >> n. <strong>Second<strong>, Hash Table keys aren't necessarily integers.   
To solve these problems we will use hash and compression functions
- Hash functions - map any key to an integer 
    - Bit Representation as Integer: any var which size is less or equal to size of integer can be mapped. In case when var is larger then size of int, we can do XOR on all parts
    - Polynomial HashCodes:
    - Cyclic Shift HashCodes
- Compression functions - map any integer to an integer in the given range [ 1...N-1 ]





## Sorted Maps

## Skip Lists

## Sets, Multisets, and Multimaps


