# Algorithm Analysis  

## Introduction
We want to write fast and memory-efficient software programs that solve engineering and business problems. But how can we measure the efficiency of the implementation? Let's say we have two programs A and B, that compute a [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number), and we want to compare A and B from the run-time performance perspective. The simple approach is to gather experimental data by using the Python built-in time function:

```Python
from time import time, sleep
start_time = time()                  
# run algorithm
end_time = time()                    
elapsed = end_time - start_time 
``` 
The elapsed time is a decent representation of the efficiency, but it is dependent on the specific input, machine type, number of running processes, amount of free memory, etc. We need a method to measure the implementation efficiency without being dependent on specific hardware and input.  

##  Beyond Experimental Analysis
First, we define two terms - Data Structure and Algorithm. Simply put, a [Data Structure](https://en.wikipedia.org/wiki/Data_structure) is a way of organizing and accessing data in computer memory, and an [Algorithm](https://en.wikipedia.org/wiki/Algorithm) is a step-by-step procedure for performing some task. To analyze the running time of an algorithm without performing experiments, we perform analysis directly on a description of the algorithm by counting primitive operations like assigning a variable, performing an arithmetic operation, comparing, etc. To capture the order of growth of an algorithm's running time, we will associate, with each algorithm, a function f(n) that characterizes the number of primitive operations that are performed as a function of the input size n.

## The Seven Functions
The seven important functions for the algorithm analysis:
- The Constant Function => $f(n)=c$
- The Logarithm Function => $f(n)=log{_2}{n}$
- The Linear Function => $f(n)=n$
- The N-Log-N Function => $f(n) = nlog{_2}{n}$
- The Quadratic Function => $f(n) = n^2$
- The Polynomial Function => $f(n) = a+a{_2}n^2+a{_3}n^3+...+a{_d}n^d$
- The Exponential Function => $f(n) = b^n$

##  Big O Notation
The big-Oh notation allows us to say that a function f(n) is less than or equal to function g(n). For example, we can say that f(n) is O(g(n)) or f(n) is order of g(n).
The big-Oh notation is used widely to characterize running times and space bounds in terms of some parameter n.
For example, for the following code 
```python
def find_max(lst: list) -> int:
    biggest = lst[0]
    for x in lst:
        if x > biggest:
            biggest = x  
    return biggest
```
The algorithm 'find-max' runs in O(n) time.

$log{_2}{n} + n^2$

