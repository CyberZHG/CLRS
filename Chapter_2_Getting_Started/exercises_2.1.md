## Insertion sort

### 2.1 - 1

> Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array $$A = \left \langle 31, 41, 59, 26, 41, 58 \right \rangle$$.

* $$A = \left \langle 31, 41, 59, 26, 41, 58 \right \rangle$$
* $$A = \left \langle 31, 41, 59, 26, 41, 58 \right \rangle$$
* $$A = \left \langle 26, 31, 41, 59, 41, 58 \right \rangle$$
* $$A = \left \langle 26, 31, 41, 41, 59, 58 \right \rangle$$
* $$A = \left \langle 26, 31, 41, 41, 58, 59 \right \rangle$$

### 2.1 - 2

> Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.

```
INSERTION-SORT(A)
1. for j = 2 to A.length
2.     key = A[j]
3.     i = j - 1
4.     while i > 0 and A[i] < key
5.         A[i + 1] = A[i]
6.         i = i - 1
7.     A[i + 1] = key
```

### 2.1 - 3

> Consider the __searching problem__:
>
> __Input__: A sequence of $$n$$ numbers $$A = \left \langle a_1, a_2, \cdots, a_n\right \rangle$$ and a value $$v$$.
>
> __Output__: An index $$i$$ such that $$v=A[i]$$ or the special value NIL if $$v$$ does not appear in A.
>
> Write pseudocode for __linear search__, which scans through the sequence, looking for $$v$$. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

```
LINEAR-SEARCH(A, v)
1. for i = 1 to A.length
2.     if A[i] == v
3.         return i
4. return NIL
```

### 2.1 - 4

> Consider the problem of adding two n-bit binary integers, stored in two n-element arrays $$A$$ and $$B$$. The sum of the two integers should be stored in binary form in an $$(n+1)$$-element array $$C$$. State the problem formally and write pseudocode for adding the two integers.

```
ADD-BINARY(A, B)
1.  n = A.length
2.  C = new Array(n + 1)
3.  carry = 0
3.  for i = 1 to n
4.      C[i] = A[i] + B[i] + carry
5.      if C[i] > 1
6.          C[i] = 0
7.          carry = 1
8.      else
9.          carry = 0
10. C[i] = carry
11. return C
```

