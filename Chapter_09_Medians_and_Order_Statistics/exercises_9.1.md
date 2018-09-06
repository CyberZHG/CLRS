## 9.1 Minimum and maximum

### 9.1-1

> Show that the second smallest of $n$ elements can be found with $n +  \lceil \lg n\rceil - 2$ comparisons in the worst case.

Divide the elements into the leaves of a binary tree. In each node, we compare the minimum values of its two sub-trees, then in the root node we know which is the smallest element using $n-1$ comparisons. Since only the smallest element is less than the second smallest element, the two elements must have been compared in order to knock out the second smallest element when finding the minimum. In other words, the second smallest number must have been appeared as the opponent in the path to the leaf which has the smallest element. The depth of the tree is $\lceil \lg n\rceil$, thus we need $\lceil \lg n\rceil - 1$ comparisons to find the second smallest element.

```python
def find_second_smallest(a, l, r):
    if l + 1 == r:
        return a[l], []
    mid = (l + r + 1) // 2
    min_l, lst_l = find_second_smallest(a, l, mid)
    min_r, lst_r = find_second_smallest(a, mid, r)
    if min_l <= min_r:
        min_val, lst = min_l, lst_l + [min_r]
    else:
        min_val, lst = min_r, lst_r + [min_l]
    if l == 0 and r == len(a):
        idx = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[idx]:
                idx = i
        return lst[idx]
    return min_val, lst
```


### 9.1-2 $\star$

> Prove the lower bound of $\lceil 3n/2 \rceil - 2$ comparisons in the worst case to find both the maximum and minimum of $n$ numbers.

If $n$ is odd, there are

$$
1 + \frac{3(n-3)}{2} + 2 = \frac{3n}{2} - \frac{3}{2} = \left ( \left \lceil \frac{3n}{2} \right \rceil - \frac{1}{2} \right ) - \frac{3}{2} = \left \lceil \frac{3n}{2} \right \rceil - 2
$$

comparisons.

If $n$ is even, there are

$$
1 + \frac{3(n-2)}{2} = \frac{3n}{2} - 2 = \left \lceil \frac{3n}{2} \right \rceil - 2
$$

comparisons.
