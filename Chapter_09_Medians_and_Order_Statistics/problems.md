## Problems

### 9-1 Largest $i$ numbers in sorted order

> Given a set of $n$ numbers, we wish to find the $i$ largest in sorted order using a comparison-based algorithm. Find the algorithm that implements each of the following methods with the best asymptotic worst-case running time, and analyze the running times of the algorithms in terms of $n$ and $i$ .

> __*a*__. Sort the numbers, and list the $i$ largest.

Depends on the sorting algorithm, with heap sort the worst-case is $O(n\lg n + i)$.

> __*b*__. Build a max-priority queue from the numbers, and call EXTRACT-MAX $i$ times.

Build the heap is $O(n)$, extract is $O(\lg n)$, thus the worst time is $O(n + i\lg n)$.

> __*c*__. Use an order-statistic algorithm to find the $i$th largest number, partition around that number, and sort the $i$ largest numbers.

$O(n + n + i\lg i) = O(n + i\lg i)$.

### 9-2 Weighted median

> For $n$ distinct elements $x\_1, x\_2, \dots, x\_n$ with positive weights $w\_1, w\_2, \dots, w\_n$ such that $\sum\_{i=1}^n w\_i = 1$, the __*weighted (lower) median*__ is the element $x\_k$ satisfying

> $\displaystyle \sum\_{x\_i < x\_k} w\_i < \frac{1}{2}$

> and

> $\displaystyle \sum\_{x\_i > x\_k} w\_i \le \frac{1}{2}$

> __*a*__. Argue that the median of $x\_1, x\_2, \dots, x\_n$ is the weighted median of the $x\_i$ with weights $w\_i = 1/n$ for $i=1,2,\dots,n$.

$$
\begin{array}{lll}
\displaystyle \sum\_{x\_i < x\_k} \frac{1}{n} < \frac{1}{2} & &
\displaystyle \sum\_{x\_i > x\_k} \frac{1}{n} \le \frac{1}{2} \\\\
\displaystyle \frac{m-1}{n} < \frac{1}{2} & &
\displaystyle \frac{n - m}{n} \ge \frac{1}{2} \\\\
\displaystyle m < \frac{n}{2} + 1 & &
\displaystyle m \ge \frac{n}{2} \\\\
\end{array}
$$

$$
\displaystyle \therefore \frac{n}{2} \le m < \frac{n}{2} + 1
$$

$$
\displaystyle\therefore  m = \left \lfloor \frac{n}{2} \right \rfloor
$$

> __*b*__. Show how to compute the weighted median of $n$ elements in $O(n \lg n)$ worstcase time using sorting.

```python
def weighted_median(x):
    x.sort()
    s = 0.0
    for i in range(len(x)):
        s += x[i]
        if s >= 0.5:
            return x[i]
```

> __*c*__. Show how to compute the weighted median in $\Theta(n)$ worst-case time using a linear-time median algorithm such as SELECT from Section 9.3.

Use the median as pivot, the algorithm is exactly $T(n)=T(n/2)+\Theta(n) = \Theta(n)$.

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

> The __*post-office location problem*__ is defined as follows. We are given $n$ points $p\_1, p\_2, \dots, p\_n$ with associated wegihts $w\_1, w\_2, \dots, w\_n$. We wish to find a point $p$ that minimizes the sum $\sum\_{i=1}^n w\_i d(p, p\_i)$, where $d(a,b)$ is the distance between points $a$ and $b$.

> __*d*__. Argue that the weighted median is a best solution for the 1-dimensional postoffice location problem, in which points are simply real numbers and the distance between points $a$ and $b$ is $d(a, b) = |a - b|$.

Same as Exercise 9.3-9.

> __*e*__. Find the best solution for the 2-dimensional post-office location problem, in which the points are $(x,y)$ coordinate pairs and the distance between points $a=(x\_1, y-1)$ and $b=(x\_2, y\_2)$ is the __*Manhattan distance*__ given by $d(a,b)=|x\_1-x\_2|+|y\_1-y\_2|$.

Since $x$ and $y$ are independent, the best solution is the medians of $x$ and $y$ separately.

### 9-3 Small order statistics

> We showed that the worst-case number $T(n)$ of comparisons used by SELECT to select the $i$th order statistic from $n$ numbers satisfies $T(n)=\Theta(n)$, but the constant hidden by the $\Theta$-notation is rather large. When $i$ is small relative to $n$, we can implement a different procedure that uses SELECT as a subroutine but makes fewer comparisons in the worst case.

> __*a*__. Describe an algorithm that uses $U\_i(n)$ comparisons to find the $i$th smallest of $n$ elements, where

> $\displaystyle U\_i(n) = \left \{ \begin{array}{ll}
T(n) & \text{if}~~i \ge n/2 \\\\
\lfloor n / 2 \rfloor + U\_i(\lceil n / 2 \rceil) + T(2i) & \text{otherwise}
\end{array} \right .$

Divide elements into pairs and compare each pair. Recursively deal with the set with the smaller elements in each pair, and return the $i$ smallest elements by partition, then the $i$th element belong to the pairs that appeared in the $i$ smallest elements.

> __*b*__. Show that, if $i < n/2$, then $U\_i(n)=n+O(T(2i)\lg(n/i))$.

Suppose $U\_i(n) \le n + cT(2i) \lg(n/i)$,

$$
\begin{array}{rlll}
T(n) &=& \lfloor n / 2 \rfloor + U\_i(\lceil n / 2 \rceil) + T(2i) \\\\
&\le& n/2 + n/2 + cT(2i) \lg(n/2i) + T(2i) \\\\
&=& n + cT(2i) \lg(n/i) + T(2i)(1-c) \\\\
&\le& n + cT(2i) \lg(n/i) & (c \ge 1) \\\\
\end{array}
$$

> __*c*__. Show that if $i$ is a constant less than $n/2$, then $U\_i(n)= n + O(\lg n)$.

$$
\begin{array}{rll}
U\_i(n) &=& n+O(T(2i)\lg(n/i)) \\\\
&=& n + O(O(1)(\lg n - lg i)) \\\\
&=& n + O(\lg n - O(1)) \\\\
&=& n + O(\lg n) \\\\
\end{array}
$$

> __*d*__. Show that if $i=n/k$ for $k \ge 2$, then $U\_i(n)=n+O(T(2n/k)\lg k)$.

$$
\begin{array}{rll}
U\_i(n) &=& n+O(T(2i)\lg(n/i)) \\\\
&=& n+O(T(2n/k)\lg(k/2)) \\\\
&=& n+O(T(2n/k)\lg k) \\\\
\end{array}
$$

### 9-4 Alternative analysis of randomized selection

> In this problem, we use indicator random variables to analyze the RANDOMIZED-SELECT procedure in a manner akin to our analysis of RANDOMIZED-QUICKSORT in Section 7.4.2.

> As in the quicksort analysis, we assume that all elements are distinct, and we rename the elements of the input array $A$ as $z\_1, z\_2, \dots, z\_n$, where $z\_i$ is the $i$th smallest element. Thus, the call RANDOMIZED-SELECT$(A, 1, n, k)$ returns $z\_k$.

> For $1 \le i < j \le n$, let 

> $X\_{ijk} = I \{z\_i$ is compared with $z\_j$ sometime during the execution of the algorithm to find $z\_k\}$.

> __*a*__. Give an exact expression for $\text{E}[X\_{ijk}]$.

$$
\text{E}[X\_{ijk}] = \left \{ 
\begin{array}{ll}
\displaystyle \frac{2}{j - k + 1} & (k \le i < j) \\\\
\displaystyle \frac{2}{j - i + 1} & (i \le k \le j) \\\\
\displaystyle \frac{2}{k - i + 1} & (i < j \le k) \\\\
\end{array}
\right .
$$

> __*b*__. Let $X\_k$ denote the total number of comparisons between elements of array $A$ when finding $z\_k$. Show that

> $$
\text{E}[X\_k] \le 2 \left ( 
\sum\_{i=1}^{k}\sum\_{j=k}^n \frac{1}{j-i+1} +
\sum\_{j=k+1}^{n} \frac{j-k-1}{j-k+1} +
\sum\_{i=1}^{k-2} \frac{k-i-1}{k-i+1}
\right )
$$

$$
\begin{array}{rll}
\text{E}[X\_k] &=& \displaystyle \sum\_{i=1}^{n-1} \sum\_{j=i+1}^n \text{E}[X\_{ijk}] \\\\
&=& \displaystyle \sum\_{i=k+1}^{n-1} \sum\_{j=i+1}^n \text{E}[X\_{ijk}] +
\sum\_{i=1}^{k} \sum\_{j=k}^n \text{E}[X\_{ijk}] +
\sum\_{i=1}^{k-2} \sum\_{j=i+1}^{k-1} \text{E}[X\_{ijk}] \\\\
&=& \displaystyle \sum\_{i=k+1}^{n-1} \sum\_{j=i+1}^n \frac{2}{j - k + 1} +
\sum\_{i=1}^{k} \sum\_{j=k}^n \frac{2}{j - i + 1} +
\sum\_{i=1}^{k-2} \sum\_{j=i+1}^{k-1} \frac{2}{k - i + 1} \\\\
&=& 2 \cdot \left (
\displaystyle \sum\_{i=k+1}^{n-1} \sum\_{j=i+1}^n \frac{1}{j - k + 1} +
\sum\_{i=1}^{k} \sum\_{j=k}^n \frac{1}{j - i + 1} +
\sum\_{i=1}^{k-2} \sum\_{j=i+1}^{k-1} \frac{1}{k - i + 1} 
\right ) \\\\
&=& 2 \left (
\displaystyle \sum\_{j=k+2}^{n-1} \sum\_{i=k+1}^{j-1} \frac{1}{j - k + 1} +
\sum\_{i=1}^{k} \sum\_{j=k}^n \frac{1}{j - i + 1} +
\sum\_{i=1}^{k-2} \sum\_{j=i+1}^{k-1} \frac{1}{k - i + 1}
\right ) \\\\
&=& 2 \left (
\displaystyle \sum\_{j=k+2}^{n-1} \frac{j-k-1}{j - k + 1} +
\sum\_{i=1}^{k} \sum\_{j=k}^n \frac{1}{j - i + 1} +
\sum\_{i=1}^{k-2} \frac{k-i-1}{k - i + 1}
\right ) \\\\
&\le& 2 \left (
\displaystyle \sum\_{j=k+1}^{n} \frac{j-k-1}{j - k + 1} +
\sum\_{i=1}^{k} \sum\_{j=k}^n \frac{1}{j - i + 1} +
\sum\_{i=1}^{k-2} \frac{k-i-1}{k - i + 1}
\right ) \\\\
&=& 2 \left ( 
\displaystyle 
\sum\_{i=1}^{k}\sum\_{j=k}^n \frac{1}{j-i+1} +
\sum\_{j=k+1}^{n} \frac{j-k-1}{j-k+1} +
\sum\_{i=1}^{k-2} \frac{k-i-1}{k-i+1}
\right )
\end{array}
$$

> __*c*__. Show that $E[X\_k] \le 4n$.

Based on [StackExchange](http://math.stackexchange.com/questions/529208/inequality-sumk-i-1-sumn-j-k1-overj-i-1-le-n), 

$$
\begin{array}{rll}
\displaystyle \sum\_{i=1}^{k}\sum\_{j=k}^n \frac{1}{j-i+1} &\le& n 
\end{array}
$$

And

$$
\displaystyle
\sum\_{j=k+1}^{n} \frac{j-k-1}{j-k+1} + \sum\_{i=1}^{k-2} \frac{k-i-1}{k-i+1} \le \sum\_{j=k+1}^{n} 1 + \sum\_{i=1}^{k-2} 1 = n - k + k - 2 = n - 2 < n
$$

Therefore $E[X\_k] \le 4n$.

> __*d*__. Conclude that, assuming all elements of array $A$ are distinct, RANDOMIZED-SELECT runs in expected time $O(n)$.

$O(4n) = O(n)$.
