## Problems

### 7-1 Hoare partition correctness

> The version of PARTITION given in this chapter is not the original partitioning algorithm. Here is the original partition algorithm, which is due to C. A. R. Hoare:

> ```
HOARE-PARTITION(A, p, r)
1  x = A[p]
2  i = p - 1
3  j = r + 1
4  while TRUE
5      repeat
6          j = j - 1
7      until A[j] <= x
8      repeat
9          i = i + 1
10     until A[i] >= x
11     if i < j
12         exchange A[i] with A[j]
13     else return j
```

> __*a*__. Demonstrate the operation of HOARE-PARTITION on the array $$A = \left \langle 13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21 \right \rangle$$, showing the values of the array and auxiliary values after each iteration of the while loop in lines 4-13.

![](img/7-1_1.png)

![](img/7-1_2.png)

![](img/7-1_3.png)

![](img/7-1_4.png)

> The next three questions ask you to give a careful argument that the procedure HOARE-PARTITION is correct. Assuming that the subarray $$A[p \dots r]$$ contains at least two elements, prove the following:

> __*b*__. The indices $$i$$ and $$j$$ are such that we never access an element of $$A$$ outside the subarray $$A[p \dots r]$$.

In the first loop, $$i$$ will terminate at the pivot, the smallest $$j$$ would be the pivot, therefore no invalid position is accessed. In the next loops, $$i$$ will finally terminate at last $$j$$ and $$i$$ will finally terminate at last $$i$$, and since $$i \ge p$$ and $$j <= r$$ after the first loop, there is no change to access an element outside $$A[p \dots r]$$.

> __*c*__. When HOARE-PARTITION terminates, it returns a value $$j$$ such that $$p \le j < r$$.

In __*b*__, we know $$p \le j \le r$$, the largest $$j$$ in the first loop is $$r$$, while $$i$$ will be at $$p$$, if $$p \ne r$$, then $$i<r$$, the loop will not terminate. In the second loop, $$j$$ has to move at least one step, therefore $$j$$ must be less than $$r$$.

> __*d*__. Every element of $$A[p \dots j]$$ is less than or equal to every element of $$A[j+1 \dots r]$$ when HOARE-PARTITION terminates.

Small values are moved to the front and large values are moved to the end.

> The PARTITION procedure in Section 7.1 separates the pivot value (originally in $$A[r]$$) from the two partitions it forms. The HOARE-PARTITION procedure, on the other hand, always places the pivot value (originally in $$A[p]$$) into one of the two partitions $$A[p \dots j]$$ and $$A[j+1 \dots r]$$. Since $$p \le j < r$$, this split is always nontrivial.

> __*e*__. Rewrite the QUICKSORT procedure to use HOARE-PARTITION.

```python
def hoare_partition(a, p, r):
    x = a[p]
    i = p - 1
    j = r
    while True:
        while True:
            j -= 1
            if a[j] <= x:
                break
        while True:
            i += 1
            if a[i] >= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j


def quicksort(a, p, r):
    if p < r - 1:
        q = hoare_partition(a, p, r)
        quicksort(a, p, q + 1)
        quicksort(a, q + 1, r)
```

### 7-2 Quicksort with equal element values

> The analysis of the expected running time of randomized quicksort in Section 7.4.2 assumes that all element values are distinct. In this problem, we examine what happens when they are not.

> __*a*__. Suppose that all element values are equal. What would be randomized quicksort’s running time in this case?


$$\Theta(n^2)$$

> __*b*__. The PARTITION procedure returns an index $$q$$ such that each element of $$A[p \dots q - 1]$$ is less than or equal to $$A[q]$$ and each element of $$A[q + 1 \dots r]$$ is greater than $$A[q]$$. Modify the PARTITION procedure to produce a procedure PARTITION'(A,p,r), which permutes the elements of $$A[p \dots r]$$ and returns two indices $$q$$ and $$t$$, where $$p \le q \le t \le r$$, such that

> * all elements of $$A[q \dots t]$$ are equal,
* each element of $$A[p \dots q - 1]$$ is less than $$A[q]$$, and
* each element of $$A[t + 1 \dots r]$$ is greater than $$A[q]$$.

> Like PARTITION, your PARTITION' procedure should take $$\Theta(r-p)$$ time.

```python
def partition(a, p, r):
    x = a[r - 1]
    i = p - 1
    for k in range(p, r - 1):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    j = i
    for k in range(i + 1, r):
        if a[k] == x:
            j += 1
            a[j], a[k] = a[k], a[j]
        k -= 1
    return i, j
```

> __*c*__. Modify the RANDOMIZED-QUICKSORT procedure to call PARTITION0, and
name the new procedure RANDOMIZED-QUICKSORT'. Then modify the QUICKSORT procedure to produce a procedure QUICKSORT'$$(p, r)$$ that calls RANDOMIZED-PARTITION' and recurses only on partitions of elements not
known to be equal to each other.

```
def randomized_partition(a, p, r):
    x = random.randint(p, r - 1)
    a[x], a[r - 1] = a[r - 1], a[x]
    return partition(a, p, r)


def quicksort(a, p, r):
    if p < r - 1:
        q, t = randomized_partition(a, p, r)
        quicksort(a, p, q)
        quicksort(a, t + 1, r)
```

> __*d*__. Using QUICKSORT', how would you adjust the analysis in Section 7.4.2 to avoid the assumption that all elements are distinct?





