## 2.1 Insertion sort

### 2.1-1

> Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array $$A = \left \langle 31, 41, 59, 26, 41, 58 \right \rangle$$.

* $$A = \left \langle 31, 41, 59, 26, 41, 58 \right \rangle$$
* $$A = \left \langle 31, 41, 59, 26, 41, 58 \right \rangle$$
* $$A = \left \langle 26, 31, 41, 59, 41, 58 \right \rangle$$
* $$A = \left \langle 26, 31, 41, 41, 59, 58 \right \rangle$$
* $$A = \left \langle 26, 31, 41, 41, 58, 59 \right \rangle$$

### 2.1-2

> Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.

```python
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
```

### 2.1-3

> Consider the __searching problem__:
>
> __Input__: A sequence of $$n$$ numbers $$A = \left \langle a_1, a_2, \cdots, a_n\right \rangle$$ and a value $$v$$.
>
> __Output__: An index $$i$$ such that $$v=A[i]$$ or the special value NIL if $$v$$ does not appear in A.
>
> Write pseudocode for __linear search__, which scans through the sequence, looking for $$v$$. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

```python
def linear_search(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return None
```

### 2.1-4

> Consider the problem of adding two n-bit binary integers, stored in two n-element arrays $$A$$ and $$B$$. The sum of the two integers should be stored in binary form in an $$(n+1)$$-element array $$C$$. State the problem formally and write pseudocode for adding the two integers.

```python
def add_binary(a, b):
    n = len(a)
    c = [0 for _ in range(n + 1)]
    carry = 0
    for i in range(n):
        c[i] = a[i] + b[i] + carry
        if c[i] > 1:
            c[i] -= 2
            carry = 1
        else:
            carry = 0
    c[n] = carry
    return c
```

