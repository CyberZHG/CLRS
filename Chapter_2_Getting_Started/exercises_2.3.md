## Designing algorithms

### 2.3 - 1

> Using Figure 2.4 as a model, illustrate the operation of merge sort on the array $$A = \left \langle3, 41, 52, 26, 38, 57, 9, 49\right \rangle$$.

* $$A = \left \langle3, 41, 26, 52, 38, 57, 9, 49\right \rangle$$
* $$A = \left \langle3, 26, 41, 52, 9, 49, 38, 57\right \rangle$$
* $$A = \left \langle3, 9, 26, 38, 41, 49, 52, 57\right \rangle$$

### 2.3 - 2

> Rewrite the MERGE procedure so that it does not use sentinels, instead stopping once either array $$L$$ or $$R$$ has had all its elements copied back to A and then copying the remainder of the other array back into $$A$$.

```
MERGE(A, p, q, r)
1.  n1 = q - p + 1
2.  n2 = r - q
3.  let L[1..n1 + 1] and R[1..n_2+1] be new arrays
4.  for i = 1 to n1
5.      L[i] = A[p + i - 1]
6.  for j = 1 to n2
7.      R[j] = A[q + j]
8.  i = 1
9.  j = 1
10. k = 1
10. while i <= n1 or j <= n2
11.     if L[i] <= R[j]
12.         A[k] = L[i]
13.         i = i + 1
14.     else
15.         A[k] = R[j]
16.         j = j + 1
17.     k = k + 1
18. while i <= n1
19.     A[k] = L[i]
20.     i = i + 1
21.     k = k + 1
22. while j <= n2
23.     A[k] = R[j]
24.     j = j + 1
25.     k = k + 1
```

### 2.3 - 3

> Use mathematical induction to show that when $$n$$ is an exact power of 2, the solution of the recurrence
>
> $$T(n)=\left\{\begin{matrix}2 & \text{if}\; n = 2 \\ 2T(n/2)+n & \text{if}\; n = 2^k, \text{for}\; k>1\end{matrix}\right.$$
>
> is $$T(n)=n\lg n$$.

* $$T(2) = 2 = 2 \lg 2$$
* Assume that $$T(2^k)=2^k \lg 2^k$$, $$k > 1$$, then $$T(2^{k+1})=2T(2^k) + 2^{k+1}$$ $$=2^{k+1}\lg 2^k+2^{k+1}$$ $$=2^{k+1}(1 + \lg2^k)$$ $$=2^{k+1}(\lg2 + \lg2^k)$$ $$=2^{k+1}\lg2^{k+1}$$.

### 2.3 - 4

> We can express insertion sort as a recursive procedure as follows. In order to sort $$A[1..n]$$, we recursively sort $$A[1..n-1]$$ and then insert $$A[n]$$ into the sorted array $$A[1..n-1]$$. Write a recurrence for the running time of this recursive version of insertion sort.

$$T(n)=\left\{\begin{matrix}1 & \text{if}\; n=1 \\ T(n-1)+n-1 & \text{if}\; n>1\end{matrix}\right.$$

### 2.3 - 5

> Referring back to the searching problem (see Exercise 2.1-3), observe that if the sequence $$A$$ is sorted, we can check the midpoint of the sequence against $$v$$ and eliminate half of the sequence from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion of the sequence each time. Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is $$\Theta(\lg n)$$.

```
BINARY-SEARCH(A, v)
1.  l = 1
2.  r = A.length
3.  while l <= r
4.      mid = (l + r) / 2
5.      if A[mid] == v
6.          return mid
7.      elseif A[mid] < v
8.          l = mid + 1
9.      else
10.         r = mid - 1
11. return NIL
```

$$T(n)=T(n/2)+C$$

### 2.3 - 6

> Observe that the while loop of lines 5-7 of the INSERTION-SORT procedure in Section 2.1 uses a linear search to scan (backward) through the sorted subarray $$A[1..j-1]$$. Can we use a binary search (see Exercise 2.3 - 5) instead to improve the overall worst-case running time of insertion sort to $$\Theta(n\lg n)$$?

No, still has to move the elements for $$\Theta(n)$$ in each iteration.

### 2.3 - 7 $$\ast$$

> Describe a $$\Theta(n\lg n)$$-time algorithm that, given a set $$S$$ of $$n$$ integers and another integer $$x$$, determines whether or not there exist two elements in $$S$$ whose sum is exactly $$x$$.

Sort the elements then:
```
TWO-SUM(A, x)
1. l = 1
2. r = A.length
3. while l < r
4.     if A[l] + A[r] == x
5.         return true
4.     elseif A[l] + A[r] < x
5.         l = l + 1
6.     else
7.         r = r - 1
8. return false
```
