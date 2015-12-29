## 8.1 Lower bounds for sorting

### 8.1-1

> What is the smallest possible depth of a leaf in a decision tree for a comparison sort?

### 8.1-2

> Obtain asymptotically tight bounds on $$\lg(n!)$$ without using Stirling’s approximation. Instead, evaluate the summation $$\sum_{k=1}^n\lg k$$ using techniques from Section A.2.

### 8.1-3

> Show that there is no comparison sort whose running time is linear for at least half of the $$n!$$ inputs of length $$n$$. What about a fraction of $$1/n$$ of the inputs of length $$n$$? What about a fraction $$1/2^n$$?

### 8.1-4

> Suppose that you are given a sequence of $$n$$ elements to sort. The input sequence consists of $$n/k$$ subsequences, each containing $$k$$ elements. The elements in a given subsequence are all smaller than the elements in the succeeding subsequence and larger than the elements in the preceding subsequence. Thus, all that is needed to sort the whole sequence of length n is to sort the $$k$$ elements in each of the $$n/k$$ subsequences. Show an $$\Omega(n\lg k)$$ lower bound on the number of comparisons needed to solve this variant of the sorting problem.