## Analyzing algorithms

### 2.2-1

> Express the function $$n^3/1000 - 100n^2 - 100n + 3$$ in terms of $$\Theta$$-notation.

$$\Theta(n^3)$$

### 2.2-2

> Consider sorting $$n$$ numbers stored in array $$A$$ by first finding the smallest element of $$A$$ and exchanging it with the element in $$A[1]$$. Then find the second smallest element of $$A$$, and exchange it with $$A[2]$$. Continue in this manner for the first $$n-1$$ elements of A. Write pseudocode for this algorithm, which is known as __selection sort__. What loop invariant does this algorithm maintain? Why does it need to run for only the first $$n - 1$$ elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in $$\Theta$$-notation.

```python
def selection_sort(a):
    for i in range(len(a)):
        k = i
        for j in range(i + 1, len(a)):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
```

* Best-case: $$\Theta(n^2)$$
* Worst-case: $$\Theta(n^2)$$

### 2.2-3

> Consider linear search again (see Exercise 2.1 - 3). How many elements of the input sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear search in $$\Theta$$-notation? Justify your answers.

* Average: $$n/2$$ elements. $$\Theta(n)$$
* Worst: $$n$$ elements. $$\Theta(n)$$

### 2.2-4

> How can we modify almost any algorithm to have a good best-case running time?

Adding special case.

