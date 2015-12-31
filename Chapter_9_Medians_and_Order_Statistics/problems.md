## Problems

### 9-1 Largest $$i$$ numbers in sorted order

> Given a set of $$n$$ numbers, we wish to find the $$i$$ largest in sorted order using a comparison-based algorithm. Find the algorithm that implements each of the following methods with the best asymptotic worst-case running time, and analyze the running times of the algorithms in terms of $$n$$ and $$i$$ .

> __*a*__. Sort the numbers, and list the $$i$$ largest.

Depends on the sorting algorithm, with heap sort the worst-case is $$O(n\lg n + i)$$.

> __*b*__. Build a max-priority queue from the numbers, and call EXTRACT-MAX $$i$$ times.

Build the heap is $$O(n)$$, extract is $$O(\lg n)$$, thus the worst time is $$O(n + i\lg n)$$.

> __*c*__. Use an order-statistic algorithm to find the $$i$$th largest number, partition around that number, and sort the $$i$$ largest numbers.

$$O(n + n + i\lg i) = O(n + i\lg i)$$.

### 9-2 Weighted median

> For $$n$$ distinct elements $$x_1, x_2, \dots, x_n$$ with positive weights $$w_1, w_2, \dots, w_n$$ such that $$\sum_{i=1}^n w_i = 1$$, the __*weighted (lower) median*__ is the element $$x_k$$ satisfying

> $$\displaystyle \sum_{x_i < x_k} w_i < \frac{1}{2}$$

> and

> $$\displaystyle \sum_{x_i > x_k} w_i \le \frac{1}{2}$$

> __*a*__. Argue that the median of $$x_1, x_2, \dots, x_n$$ is the weighted median of the $$x_i$$ with weights $$w_i = 1/n$$ for $$i=1,2,\dots,n$$.

$$
\begin{array}{lll}
\displaystyle \sum_{x_i < x_k} \frac{1}{n} < \frac{1}{2} & &
\displaystyle \sum_{x_i > x_k} \frac{1}{n} \le \frac{1}{2} \\
\displaystyle \frac{m-1}{n} < \frac{1}{2} & &
\displaystyle \frac{n - m}{n} \ge \frac{1}{2} \\
\displaystyle m < \frac{n}{2} + 1 & &
\displaystyle m \ge \frac{n}{2} \\
\end{array}
$$

$$
\displaystyle \therefore \frac{n}{2} \le m < \frac{n}{2} + 1
$$

$$
\displaystyle\therefore  m = \left \lfloor \frac{n}{2} \right \rfloor
$$

> __*b*__. Show how to compute the weighted median of $$n$$ elements in $$O(n \lg n)$$ worstcase time using sorting.

```python
def weighted_median(x):
    x.sort()
    s = 0.0
    for i in range(len(x)):
        s += x[i]
        if s >= 0.5:
            return x[i]
```

> __*c*__. Show how to compute the weighted median in $$\Theta(n)$$ worst-case time using a linear-time median algorithm such as SELECT from Section 9.3.

Use the median as pivot, the algorithm is exactly $$T(n)=T(n/2)+\Theta(n) = \Theta(n)$$.

```python
def black_box_median(a, p, r):
    return sorted(a[p:r])[(r - p - 1) // 2]


def partition(a, p, r, x):
    s = x
    i = p - 1
    for j in xrange(p, r - 1):
        if a[j] == x:
            a[j], a[r - 1] = a[r - 1], a[j]
            break
    for j in xrange(p, r - 1):
        if a[j] < x:
            i += 1
            s += a[j]
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i, s


def weighted_median(a, p, r, w=0.5):
    if p + 1 >= r:
        return a[p]
    x = black_box_median(a, p, r)
    q, s = partition(a, p, r, x)
    if s - a[q] < w and s >= w:
        return a[q]
    if s >= w:
        return weighted_median(a, p, q, w)
    return weighted_median(a, q + 1, r, w - s)
```
