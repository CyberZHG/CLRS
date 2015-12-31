## 9.3 Selection in worst-case linear time

### 9.3-1

> In the algorithm SELECT, the input elements are divided into groups of 5. Will the algorithm work in linear time if they are divided into groups of 7? Argue that SELECT does not run in linear time if groups of 3 are used.

Suppose the input elements are divided into $$7$$ groups, then

$$
4 \left (\left \lceil \frac{1}{2} \left \lceil \frac{n}{7} \right \rceil \right \rceil - 2 \right ) \ge \frac{2n}{7} - 8
$$

$$
T(n) = T(\lceil n / 7 \rceil) + T(5n/7 + 8) + O(n)
$$

Suppose $$T(n) \le cn$$,

$$
\begin{array}{rll}
T(n) &\le& cn/7 + c + 8c + 5cn/7 + an \\
&=& 6cn / 7 + 9c + an \\
&=& cn + (-cn/7+9c+an) \\
&\le& cn
\end{array}
$$

Suppose the input elements are divided into $$3$$ groups, then

$$
2 \left (\left \lceil \frac{1}{2} \left \lceil \frac{n}{3} \right \rceil \right \rceil - 2 \right ) \ge \frac{n}{3} - 4
$$

$$
T(n) = T(\lceil n / 3 \rceil) + T(2n/3 + 4) + O(n)
$$

Suppose $$T(n)\ge cn$$,

$$
\begin{array}{rll}
T(n) &\ge& cn/3 + c + 4c + 2cn/3 + an \\
&=& cn + 5c + an \\
&>& cn \\
\end{array}
$$

Therefore SELECT does not run in linear time if groups of 3 are used.

### 9.3-2

> Analyze SELECT to show that if $$n \ge 140$$, then at least $$\lceil n/4 \rceil$$ elements are greater than the median-of-medians $$x$$ and at least $$\lceil n/4 \rceil$$ elements are less than $$x$$.

$$
\begin{array}{rll}
\displaystyle \frac{3n}{10} - 6 &\ge& \displaystyle \left \lceil \frac{n}{4} \right \rceil \\
\displaystyle \frac{3n}{10} - 6 &\ge& \displaystyle \frac{n}{4} + 1 \\
12n - 240 &\ge& 10n + 40 \\
n &\ge& 140 \\
\end{array}
$$

### 9.3-3

> Show how quicksort can be made to run in $$O(n \lg n)$$ time in the worst case, assuming that all elements are distinct.

Use median as pivot, since we can find median in $$O(n)$$, and based on Problem 7-2 (b), we have $$T(n)=T(n/2)+O(n)$$.

### 9.3-4 $$\star$$

> Suppose that an algorithm uses only comparisons to find the $$i$$th smallest element in a set of $$n$$ elements. Show that it can also find the $$i - 1$$ smaller elements and $$n-i$$ larger elements without performing additional comparisons.

$$\dots$$

### 9.3-5

> Suppose that you have a "black-box" worst-case linear-time median subroutine. Give a simple, linear-time algorithm that solves the selection problem for an arbitrary order statistic.

```python
def black_box_median(a, p, r):
    return sorted(a)[(p + r) // 2]


def partition(a, p, r, x):
    i = p - 1
    for k in range(p, r):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    return i


def select(a, p, r, i):
    if p + 1 == r:
        return a[p]
    x = black_box_median(a, p, r)
    q = partition(a, p, r, x)
    k = q - p + 1
    if i <= k:
        return select(a, p, q + 1, i)
    return select(a, q + 1, r, i - k)
```

### 9.3-6

> The $$k$$th __*quantiles*__ of an $$n$$-element set are the $$k - 1$$ order statistics that divide the sorted set into $$k$$ equal-sized sets (to within 1). Give an $$O(n \lg k)$$-time algorithm to list the $$k$$th quantiles of a set.

Pre-calculate the positions of the quantiles in $$O(k)$$, we use the $$O(n)$$ select algorithm to find the $$\lfloor k/2 \rfloor$$th position, after that the elements are divided into two sets by the pivot the $$\lfloor k/2 \rfloor$$th position, we do it recursively in the two sets to find other positions. Since the maximum depth is $$\lceil \lg k \rceil$$, the total running time is $$O(n \lg k)$$.

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
            return p, a[p]
        q = randomized_partition(a, p, r)
        k = q - p + 1
        if i == k:
            return q, a[q]
        if i < k:
            r = q
        else:
            p = q + 1
            i -= k


def k_quantiles_sub(a, p, r, pos, f, e, quantiles):
    if f + 1 > e:
        return
    mid = (f + e) // 2
    q, val = randomized_select(a, p, r, pos[mid])
    quantiles[mid] = val
    k_quantiles_sub(a, p, q, pos, f, mid, quantiles)
    k = q - p + 1
    for i in xrange(mid + 1, e):
        pos[i] -= k
    k_quantiles_sub(a, q + 1, r, pos, mid + 1, e, quantiles)


def k_quantiles(a, k):
    num = len(a) / k
    mod = len(a) % k
    pos = [num for _ in xrange(k)]
    for i in xrange(mod):
        pos[i] += 1
    for i in xrange(1, k):
        pos[i] += pos[i - 1]
    quantiles = [0 for _ in xrange(k)]
    k_quantiles_sub(a, 0, len(a), pos, 0, len(pos), quantiles)
    return quantiles
```

### 9.3-7

> Describe an $$O(n)$$-time algorithm that, given a set $$S$$ of $$n$$ distinct numbers and a positive integer $$k \le n$$, determines the $$k$$ numbers in $$S$$ that are closest to the median of $$S$$.

Find the median in $$O(n)$$; create a new array, each element is the absolute value of the original value subtract the median; find the $$k$$th smallest number in $$O(n)$$,  then the desired values are the elements whose absolute difference with the median is less than or equal to the $$k$$th smallest number in the new array.

```python
def black_box_kth(a, k):
    return sorted(a)[k-1]


def black_box_median(a):
    return black_box_kth(a, len(a) // 2)


def k_closest(a, k):
    median = black_box_median(a)
    b = [abs(a[i] - median) for i in xrange(len(a))]
    kth = black_box_kth(b, k)
    closest = []
    for i in xrange(len(a)):
        if abs(a[i] - median) < kth:
            closest.append(a[i])
    for i in xrange(len(a)):
        if abs(a[i] - median) == kth:
            closest.append(a[i])
        if len(closest) >= k:
            break
    return closest
```
