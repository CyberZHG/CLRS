## 27.3 Multithreaded merge sort

### 27.3-1

> Explain how to coarsen the base case of P-MERGE.

### 27.3-2

> Instead of finding a median element in the larger subarray, as P-MERGE does, consider a variant that finds a median element of all the elements in the two sorted subarrays using the result of Exercise 9.3-8. Give pseudocode for an efficient multithreaded merging procedure that uses this median-finding procedure. Analyze your algorithm.

### 27.3-3

> Give an efficient multithreaded algorithm for partitioning an array around a pivot, as is done by the PARTITION procedure on page 171. You need not partition the array in place. Make your algorithm as parallel as possible. Analyze your algorithm. (Hint: You may need an auxiliary array and may need to make more than one pass over the input elements.)

Parallel for then merge.

### 27.3-4

> Give a multithreaded version of RECURSIVE-FFT on page 911. Make your implementation as parallel as possible. Analyze your algorithm.

### 27.3-5 $$\star$$

> Give a multithreaded version of RANDOMIZED-SELECT on page 216. Make your implementation as parallel as possible. Analyze your algorithm. (Hint: Use the partitioning algorithm from Exercise 27.3-3.)

$$T_\infty = \Theta(\lg^2n)$$

### 27.3-6 $$\star$$

> Show how to multithread SELECT from Section 9.3. Make your implementation as parallel as possible. Analyze your algorithm.

$$T_\infty = \Theta(\lg^2n)$$
