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
A very naive implementation of Hash Tables is based on arrays. Array indices are keys of Hash Tables and values are elements of the array. We have two challenges in such a scenario. <strong>First</strong>, we may not wish to devote an array of length N if it is the case that N >> n. <strong>Second</strong>, Hash Table keys aren't necessarily integers.   
To solve these problems, we will use hash and compression functions
- Hash functions - map any key to an integer 
    - Bit Representation as Integer: any var with the size less or equal to the integer size can be mapped. In case when var is larger than the size of int, we can do XOR on all parts
    ```Python
    def hash_code(s):
        from operator import xor
        from functools import reduce
        return reduce(lambda x, y: xor(x, ord(y)), s, 0)
    ```
    - Polynomial HashCodes: the XOR method doesn't work for strings that consist of the same chars but in a different order. In this case we can use  polynomial hashcodes. The idea is to give for diffrent parts diffrent weights
    - Cyclic Shift HashCodes  
    ```Python
    def hash_code(s):
        mask = (1 << 32) − 1                   # limit to 32-bit integers
        h = 0
        for character in s:
            h = (h << 5 & mask) | (h >> 27)      # 5-bit cyclic shift of running sum
         h += ord(character)                  # add in value of next character
        return h
    ```
- Compression functions - in some cases, the result of the hash function can't be used immediatly. The result can be negative or exceet the capacity of the underlying array. In such cases we need compressions functions.
    - The Division Method - <strong>i mod N</strong>
    - The MAD (Multiply-Add-and-Divide) Method - <strong>((a*i + b) mod p)  mod N</strong>
    - Collision-Handling Schemes
        - Separate Chaining - use secondary container. For example, the value of the Hash Table is a list of values
        - Open Addressing - 
            - Linear Probing - if h(k) = j and j is taken, try j+1
            - Quadratic Probing - h(k) + i^2 for i = 0...n  


## Sorted Maps
[TBD]

## Skip Lists
[TBD]

## Sets, Multisets, and Multimaps
- A set is an unordered collection of elements, without duplicates, that typically supports efficient membership tests. In essence, elements of a set are like keys of a map, but without any auxiliary values.
- A multiset (also known as a bag) is a set-like container that allows duplicates.
- A multimap is similar to a traditional map, in that it associates values with keys; however, in a multimap the same key can be mapped to multiple values. For example, the index of this book maps a given term to one or more locations at which the term occurs elsewhere in the book.


