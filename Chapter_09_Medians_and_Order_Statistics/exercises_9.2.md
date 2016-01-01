## 9.2 Selection in expected linear time

### 9.2-1

> Show that RANDOMIZED-SELECT never makes a recursive call to a 0-length array.

$$\dots$$

### 9.2-2

> Argue that the indicator random variable $$X_k$$ and the value $$T(max(k - 1, n - k))$$ are independent.

$$\dots$$

### 9.2-3

> Write an iterative version of RANDOMIZED-SELECT.

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
    return i


def randomized_partition(a, p, r):
    x = random.randint(p, r - 1)
    a[x], a[r - 1] = a[r - 1], a[x]
    return partition(a, p, r)


def randomized_select(a, p, r, i):
    while True:
        if p + 1 == r:
            return a[p]
        q = randomized_partition(a, p, r)
        k = q - p + 1
        if i == k:
            return a[q]
        if i < k:
            r = q
        else:
            p = q + 1
            i -= k
```

### 9.2-4

> Suppose we use RANDOMIZED-SELECT to select the minimum element of the array $$A = \langle 3; 2; 9; 0; 7; 5; 4; 8; 6; 1 \rangle$$. Describe a sequence of partitions that results in a worst-case performance of RANDOMIZED-SELECT.

Select 9, 8, 7, 6, 5, 4, 3, 2, 1.
