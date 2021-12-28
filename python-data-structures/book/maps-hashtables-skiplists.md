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

## Sorted Maps

## Skip Lists

## Sets, Multisets, and Multimaps


