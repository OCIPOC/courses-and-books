# Array-Based Sequences

## Introduction
In computer science, an array data structure, or simply an array, is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. An array is stored such that the position of each element can be computed from its index tuple by a mathematical formula

## Low Level Arrays
The primary memory of a computer is composed of bits of information, and those bits are typically grouped into larger units that depend upon the precise system architecture. Such a typical unit is a byte (8 bits). Each byte of memory is associated with a unique number that serves as its address (random access memory - RAM). A group of related variables can be stored one after another in a contiguous portion of the computer's memory. Such a representation called an [array](https://en.wikipedia.org/wiki/Array_data_structure).

## Python's Array-Based Types
Python has the following built in array-based sequences: [list](https://docs.python.org/3/glossary.html#term-list), [tuple](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple) and [str](https://docs.python.org/3/library/stdtypes.html?highlight=str#str). There is significant commonality between these classes, most notably: each supports indexing to access an individual element of a sequence, using a syntax such as seq[k], and each uses a low-level concept known as an [array](https://docs.python.org/3/library/array.html) to represent the sequence.

## Array Complexity
- Peek O(1)
- Mutate in dynamic arrays:
    - Beginning O(n)
    - End O(1) [ammortized](https://en.wikipedia.org/wiki/Amortized_analysis)
    - Middle O(n)