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
First, we define two terms - Data Structure and Algorithm. Simply put, a data structure is a way of organizing and accessing data in computer memory, and an algorithm is a step-by-step procedure for performing some task. To analyze the running time of an algorithm without performing experiments, we perform analysis directly on a high-level description of the algorithm by counting primitive operations like assigning a variable, performing an arithmetic operation, comparing, etc.  

##  Big O Notation
To capture the order of growth of an algorithm's running time, we will associate, with each algorithm, a function f(n) that characterizes the number of primitive operations that are performed as a function of the input size n.