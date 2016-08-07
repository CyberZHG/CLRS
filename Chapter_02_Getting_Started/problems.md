## Problems

### 2-1 Insertion sort on small arrays in merge sort

> Although merge sort runs in $$\Theta(n \lg n)$$ worst-case time and insertion sort runs in $$\Theta(n^2)$$ worst-case time, the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines. Thus, it makes sense to __coarsen__ the leaves of the recursion by using insertion sort within merge sort when subproblems become sufficiently small. Consider a modification to merge sort in which $$n=k$$ sublists of length $$k$$ are sorted using insertion sort and then merged using the standard merging mechanism, where $$k$$ is a value to be determined.

> __*a*__. Show that insertion sort can sort the $$n/k$$ sublists, each of length $$k$$, in $$\Theta(nk)$$ worst-case time.

$$\Theta(k^2) \cdot n/k = \Theta(nk)$$

> __*b*__. Show how to merge the sublists in $$\Theta(n\lg(n/k))$$ worst-case time.

* Layers: $$\lg(n/k)$$
* Each: $$n$$

> __*c*__. Given that the modified algorithm runs in $$\Theta(nk+n\lg(n/k))$$ worst-case time, what is the largest value of k as a function of n for which the modified algorithm has the same running time as standard merge sort, in terms of $$\Theta$$-notation?

Since $$n \lg (n/k) <= n \lg n$$, thus $$nk = n\lg n$$, $$k=\lg n$$.

> __*d*__. How should we choose $$k$$ in practice?

Profiling with large data set.

### 2-2 Correctness of bubblesort

> Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order.
```
BUBBLESORT(A)
1 for i= 1 to A.length - 1
2     for j = A.length downto i + 1
3         if A[j] < A[j - 1]
4             exchange A[j] with A[j - 1]
```

> __*a*__. Let $$A'$$ denote the output of BUBBLESORT(A). To prove that BUBBLESORT is correct, we need to prove that it terminates and that
>
> $$A'[1] \le A'[2] \le \cdots \le A'[n]$$  (2.3)
> 
> where $$n$$ = $$A$$.length. In order to show that BUBBLESORT actually sorts, what else do we need to prove?

$$A'$$ is a permutation of $$A$$.

> __*b*__. State precisely a loop invariant for the for loop in lines 2–4, and prove that this loop invariant holds. Your proof should use the structure of the loop invariant proof presented in this chapter.

* Initialization: A[1] is sorted
* Maintenance: Move the smallest element to the left
* Termination: A[1..i] is sorted with the next smallest element in A[i]

> __*c*__. Using the termination condition of the loop invariant proved in part (b), state a loop invariant for the for loop in lines 1–4 that will allow you to prove inequality (2.3). Your proof should use the structure of the loop invariant proof presented in this chapter.

* Initialization: A[1..i-1] is sorted with smallest elements
* Maintenance: Move the next smallest element to A[i] and A[i - 1] <= A[i]
* Termination: (2.3)

> __*d*__. What is the worst-case running time of bubblesort? How does it compare to the running time of insertion sort?

$$\Theta(n^2)$$

For average case insertion sort is better.

### 2-3 Correctness of Horner’s rule

> The following code fragment implements Horner’s rule for evaluating a polynomial
>
> $$\begin{matrix}
P(x) & = & \sum_{k=0}^n a_k x^k \\ 
 & = & a_0 + x(a_1 + x(a_x + \cdots + x(a_{n-1} + xa_n)\cdots))
\end{matrix}$$
>
> given the coefficients $$a_0, a_1, \cdots, a_n$$ and a value for $$x$$:
>
> ```
> 1 y = 0
> 2 for i = n downto 0
> 3     y = ai + x y
>```

> __*a*__. In terms of $$\Theta$$-notation, what is the running time of this code fragment for Horner’s rule?

$$\Theta(n)$$

> __*b*__. Write pseudocode to implement the naive polynomial-evaluation algorithm that computes each term of the polynomial from scratch. What is the running time of this algorithm? How does it compare to Horner’s rule?

```python
def polynomial_evaluation(a, x):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * x ** i
    return sum
```

$$\Theta(n^2)$$

> __*c*__. Consider the following loop invariant:
> 
> At the start of each iteration of the for loop of lines 2–3,
> 
> $$y=\sum_{k=0}^{n-(i+1)} a_{k+i+1}x^k$$.
>
> Interpret a summation with no terms as equaling 0. Following the structure of the loop invariant proof presented in this chapter, use this loop invariant to show that, at termination, $$y=\sum_{k=0}^n a_k x^k$$.

* Initialization: $$y=0$$
* Maintenance: $$y=a_i+x\sum_{k=0}^{n-(i+1)} a_{k+i+1}x^k$$ $$=a_ix^0+\sum_{k=0}^{n-(i+1)} a_{k+i+1}x^{k+1}$$ $$=a_ix^0+\sum_{k=1}^{n-i} a_{k+i}x^{k}$$ $$=\sum_{k=0}^{n-i} a_{k+i}x^{k}$$
* Termination: $$y=\sum_{k=0}^{n} a_{k}x^k$$

> __*d*__. Conclude by arguing that the given code fragment correctly evaluates a polynomial characterized by the coefficients
$$a_0, a_1, \cdots, a_n$$.

$$\sum y_i = P(x)$$

### 2-4 Inversions

> Let $$A[1..n]$$ be an array of n distinct numbers. If $$i < j$$ and A[i] > A[j], then the pair $$(i, j)$$ is called an __*inversion*__ of A.

> __*a*__. List the five inversions of the array $$\left \langle 2, 3, 8, 6, 1 \right \rangle$$.

* $$(2, 1)$$
* $$(3, 1)$$
* $$(8, 6)$$
* $$(8, 1)$$
* $$(6, 1)$$

> __*b*__. What array with elements from the set $$\{1,2,\cdots,n\}$$ has the most inversions? How many does it have?

* Most: $$\{n,n-1,\cdots,1\}$$
* How many: $$\frac{n(n-1)}{2}$$

> __*c*__. What is the relationship between the running time of insertion sort and the number of inversions in the input array? Justify your answer.

Equal

> __*d*__. Give an algorithm that determines the number of inversions in any permutation on $$n$$ elements in $$\Theta(n \lg n)$$ worst-case time. (Hint: Modify merge sort.)

```python
def count_inversion_sub(arr, l, r):
    if l >= r:
        return 0
    mid = (l + r) // 2
    cnt = count_inversion_sub(arr, l, mid) + count_inversion_sub(arr, mid+1, r)
    arr_l = [arr[i] for i in range(l, mid+1)]
    arr_l.append(1e100)
    arr_r = [arr[j] for j in range(mid+1, r+1)]
    arr_r.append(1e100)
    i, j = 0, 0
    for k in range(l, r+1):
        if arr_l[i] <= arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1
            cnt += len(arr_l) - i - 1
    return cnt


def count_inversion(arr):
    return count_inversion_sub(arr, 0, len(arr) - 1)
```
