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

> __*a*__. Demonstrate the operation of HOARE-PARTITION on the array $A = \left \langle 13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21 \right \rangle$, showing the values of the array and auxiliary values after each iteration of the while loop in lines 4-13.

![](img/7-1_1.png)

![](img/7-1_2.png)

![](img/7-1_3.png)

![](img/7-1_4.png)

> The next three questions ask you to give a careful argument that the procedure HOARE-PARTITION is correct. Assuming that the subarray $A[p \dots r]$ contains at least two elements, prove the following:

> __*b*__. The indices $i$ and $j$ are such that we never access an element of $A$ outside the subarray $A[p \dots r]$.

In the first loop, $i$ will terminate at the pivot, the smallest $j$ would be the pivot, therefore no invalid position is accessed. In the next loops, $i$ will finally terminate at last $j$ and $i$ will finally terminate at last $i$, and since $i \ge p$ and $j <= r$ after the first loop, there is no change to access an element outside $A[p \dots r]$.

> __*c*__. When HOARE-PARTITION terminates, it returns a value $j$ such that $p \le j < r$.

In __*b*__, we know $p \le j \le r$, the largest $j$ in the first loop is $r$, while $i$ will be at $p$, if $p \ne r$, then $i<r$, the loop will not terminate. In the second loop, $j$ has to move at least one step, therefore $j$ must be less than $r$.

> __*d*__. Every element of $A[p \dots j]$ is less than or equal to every element of $A[j+1 \dots r]$ when HOARE-PARTITION terminates.

Small values are moved to the front and large values are moved to the end.

> The PARTITION procedure in Section 7.1 separates the pivot value (originally in $A[r]$) from the two partitions it forms. The HOARE-PARTITION procedure, on the other hand, always places the pivot value (originally in $A[p]$) into one of the two partitions $A[p \dots j]$ and $A[j+1 \dots r]$. Since $p \le j < r$, this split is always nontrivial.

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


$\Theta(n^2)$

> __*b*__. The PARTITION procedure returns an index $q$ such that each element of $A[p \dots q - 1]$ is less than or equal to $A[q]$ and each element of $A[q + 1 \dots r]$ is greater than $A[q]$. Modify the PARTITION procedure to produce a procedure PARTITION'(A,p,r), which permutes the elements of $A[p \dots r]$ and returns two indices $q$ and $t$, where $p \le q \le t \le r$, such that

> * all elements of $A[q \dots t]$ are equal,
* each element of $A[p \dots q - 1]$ is less than $A[q]$, and
* each element of $A[t + 1 \dots r]$ is greater than $A[q]$.

> Like PARTITION, your PARTITION' procedure should take $\Theta(r-p)$ time.

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
name the new procedure RANDOMIZED-QUICKSORT'. Then modify the QUICKSORT procedure to produce a procedure QUICKSORT'$(p, r)$ that calls RANDOMIZED-PARTITION' and recurses only on partitions of elements not
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

### 7-3 Alternative quicksort analysis

> An alternative analysis of the running time of randomized quicksort focuses on the expected running time of each individual recursive call to RANDOMIZED-QUICKSORT, rather than on the number of comparisons performed.

> __*a*__. Argue that, given an array of size $n$, the probability that any particular element is chosen as the pivot is $1/n$. Use this to define indicator random variables $X_i = I \{i$th smallest element is chosen as the pivot$\}$. What is $\text{E}[X_i]$?

$\text{E}[X_i] = 1/n$

> __*b*__. Let $T(n)$ be a random variable denoting the running time of quicksort on an array of size $n$. Argue that

> $$
\text{E}[T(n)] = \text{E} \left [ \sum_{q=1}^n X_q (T(q-1) + T(n-q) + \Theta(n)) \right ]
$$

Obviously.

> __*c*__. Show that we can rewrite equation (7.5) as

> $$
\text{E}[T(n)] = \frac{2}{n} \sum_{q=2}^{n-1} \text{E}[T(q)] + \Theta(n)
$$

$$
\begin{array}{rll}
\text{E}[T(n)] &=& \displaystyle \text{E} \left [ \sum_{q=1}^n X_q (T(q-1) + T(n-q) + \Theta(n)) \right ] \\
&=& \displaystyle \frac{1}{n} \left [ \sum_{q=1}^{n} \text{E}[T(q - 1)] + \sum_{q=1}^{n} \text{E}[T(n - q)] \right ] + \Theta(n) \\
&=& \displaystyle \frac{1}{n} \left [ \sum_{q=0}^{n-1} \text{E}[T(q)] + \sum_{q=0}^{n-1} \text{E}[T(q)] \right ] + \Theta(n) \\
&=& \displaystyle \frac{2}{n} \sum_{q=0}^{n-1} \text{E}[T(q)] + \Theta(n) \\
&=& \displaystyle \frac{2}{n} \sum_{q=2}^{n-1} \text{E}[T(q)] + \Theta(n) \\
\end{array}
$$

> __*d*__. Show that

> $$
\sum_{k=2}^{n-1}k \lg k \le \frac{1}{2} n^2 \lg n - \frac{1}{8} n^2
$$

$$
\begin{array}{rll}
\displaystyle \sum_{k=2}^{n-1} k \lg k &=& \displaystyle \sum_{k=2}^{\left \lceil n / 2 \right \rceil - 1} k \lg k + \sum_{k=\left \lceil n / 2 \right \rceil}^{n-1} k \lg k \\
&\le& \displaystyle \sum_{k=2}^{\left \lceil n / 2 \right \rceil - 1} k \lg (n/2) + \sum_{k=\left \lceil n / 2 \right \rceil}^{n-1} k \lg n \\
&=&  \displaystyle \sum_{k=2}^{\left \lceil n / 2 \right \rceil - 1} k \lg n -  \displaystyle \sum_{k=2}^{\left \lceil n / 2 \right \rceil - 1} k + \sum_{k=\left \lceil n / 2 \right \rceil}^{n-1} k \lg n \\
&=& \displaystyle \sum_{k=2}^{n - 1} k \lg n -  \displaystyle \sum_{k=2}^{\left \lceil n / 2 \right \rceil - 1} k \\
&\le& \displaystyle \frac{\left [ 2 + (n - 1) \right ] \cdot (n - 2)}{2} \cdot \lg n -  \frac{\left [ 2 + (n / 2 - 1) \right ] \cdot (n / 2 - 2)}{2} \cdot \lg k \\
&=& \displaystyle \frac{n^2 - n - 2}{2} \cdot \lg n - \frac{n^2 - 2n - 8}{8} \cdot \lg k \\
&=& \displaystyle \frac{1}{2} n^2 \lg n - \frac{1}{8} n^2 - \frac{1}{2} (n + 2) \lg n + \frac{1}{4} (n + 4) \\
&=& \displaystyle \frac{1}{2} n^2 \lg n - \frac{1}{8} n^2 + \frac{1}{4} n (1 - 2 \lg n) + (1 - \lg n) \\
&\le& \displaystyle \frac{1}{2} n^2 \lg n - \frac{1}{8} n^2
\end{array}
$$

> __*e*__. Using the bound from equation (7.7), show that the recurrence in equation (7.6) has the solution $\text{E}[T(n)] = \Theta(n \lg n)$.

Suppose $\text{E}[T(n)] \le cn \lg n$,

$$
\begin{array}{rll}
\text{E}[T(n)] &=& \displaystyle \frac{2}{n} \sum_{q=2}^{n-1} \text{E}[T(q)] + \Theta(n) \\
&\le& \displaystyle \frac{2}{n} \sum_{q=2}^{n-1} cq\lg q + \Theta(n) \\
&\le& \displaystyle \frac{2c}{n} \left ( \frac{1}{2}n^2 \lg n - \frac{1}{8}n^2 \right ) + \Theta(n) \\
&=& \displaystyle cn \lg n - \frac{1}{4}cn + \Theta(n) \\
&=& \displaystyle \Theta(n \lg n) \\
\end{array}
$$

### 7-4 Stack depth for quicksort

> The QUICKSORT algorithm of Section 7.1 contains two recursive calls to itself. After QUICKSORT calls PARTITION, it recursively sorts the left subarray and then it recursively sorts the right subarray. The second recursive call in QUICKSORT is not really necessary; we can avoid it by using an iterative control structure. This technique, called tail recursion, is provided automatically by good compilers. Consider the following version of quicksort, which simulates tail recursion:

> ```
TAIL-RECURSIVE-QUCIKSORT(A, p, r)
1 while p < r
2     // Partition and sort left subarray
3     q = PARTITION(A, p, r)
4     TAIL-RECURSIVE-QUCIKSORT(A, p, q - 1)
5     p = q + 1
```

> __*a*__. Argue that TAIL-RECURSIVE-QUICKSORT$(A, 1, A.length)$ correctly sorts the array $A$.

The function needs to call QUCIKSORT$(A, q + 1, r)$, set $p$ to $q + 1$ then go to line 1 is exactly the same form of calling the function.

> Compilers usually execute recursive procedures by using a stack that contains pertinent information, including the parameter values, for each recursive call. The information for the most recent call is at the top of the stack, and the information for the initial call is at the bottom. Upon calling a procedure, its information is pushed onto the stack; when it terminates, its information is popped. Since we assume that array parameters are represented by pointers, the information for each procedure call on the stack requires $O(1)$ stack space. The stack depth is the maximum amount of stack space used at any time during a computation.

> __*b*__. Describe a scenario in which TAIL-RECURSIVE-QUICKSORT’s stack depth is $\Theta(n)$ on an $n$-element input array.

$T(n)=T(1) + T(n-1) + \Theta(n)$

> __*c*__. Modify the code for TAIL-RECURSIVE-QUICKSORT so that the worst-case stack depth is $\Theta(\lg n)$. Maintain the $O(n \lg n)$ expected running time of the algorithm.

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


def randomized_partition(a, p, r):
    x = random.randint(p, r - 1)
    a[x], a[r - 1] = a[r - 1], a[x]
    return partition(a, p, r)


def quicksort(a, p, r):
    while p < r - 1:
        q, t = randomized_partition(a, p, r)
        if q - p < r - t:
            quicksort(a, p, q)
            p = t + 1
        else:
            quicksort(a, t + 1, r)
            r = q
```

### 7-5 Median-of-3 partition

> One way to improve the RANDOMIZED-QUICKSORT procedure is to partition
around a pivot that is chosen more carefully than by picking a random element from the subarray. One common approach is the median-of-3 method: choose the pivot as the median (middle element) of a set of 3 elements randomly selected from the subarray. (See Exercise 7.4-6.) For this problem, let us assume that the elements in the input array $A[1 \dots n]$ are distinct and that $n \ge 3$. We denote the sorted output array by $A'[1 \dots n]$. Using the median-of-3 method to choose the pivot element $x$, define $p_i = \text{Pr} \{ x = A'[i] \}$.

> __*a*__. Give an extract formula for $p_i$ as a function of $n$ and $i$ for $i=2,3, \dots, n-1$. (Note that $p_1 = p_n = 0$.)


$$
p_i = \binom{3}{1} \frac{1}{n} \cdot \binom{2}{1} \frac{i-1}{n-1} \cdot \frac{n-i}{n-2} = \frac{6(i-1)(n-i)}{n(n-1)(n-2)}
$$

> __*b*__. By what amount have we increased the likelihood of choosing the pivot as $x = A'[\left \lfloor (n+1)/2 \right \rfloor]$, the median of $A[1 \dots n]$, compared with the ordinary implementaiton? Assume that $n \rightarrow \infty$, and give the limiting ratio of these probabilities.

$$
p_{\left \lfloor (n+1)/2 \right \rfloor} \approx \frac{6(\frac{n+1}{2}-1)(n-\frac{n+1}{2})}{n(n-1)(n-2)}=\frac{3(n-1)}{2n(n-2)}
$$

$$
\lim_{n \rightarrow \infty}\frac{\frac{3(n-1)}{2n(n-2)}}{\frac{1}{n}} = \lim_{n \rightarrow \infty} \frac{3(n-1)}{2(n-2)} = \frac{3}{2}
$$


> __*c*__. If we define a "good" split to mean choosing the pivot as $x=A'[i]$, where $n/3 \le i \le 2n / 3$, by what amount have we increased the likelihood of getting a good split compared with the ordinary implementation?

$$
\begin{array}{rll}
\displaystyle \lim_{n \rightarrow \infty} \sum_{i=n/3}^{2n/3} \frac{6(i-1)(n-i)}{n(n-1)(n-2)} &=& \displaystyle \lim_{n \rightarrow \infty} \frac{6}{n(n-1)(n-2)} \sum_{i=n/3}^{2n/3} (i-1)(n-i) \\
&\approx& \displaystyle \lim_{n \rightarrow \infty} \frac{6}{n(n-1)(n-2)} \int_{n/3}^{2n/3} (x-1)(n-x) dx \\
&=& \displaystyle \lim_{n \rightarrow \infty} \frac{6}{n(n-1)(n-2)} \left (-\frac{1}{3}x^3+\frac{1}{2}(n+1)x^2-nx \right ) \Bigr|_{n/3}^{2n/3} \\
&=& \displaystyle \lim_{n \rightarrow \infty} \frac{6}{n(n-1)(n-2)} \left ( -\frac{7}{81}n^3+\frac{1}{6}n^3 - \frac{1}{6}n^2 \right ) \\
&=& \displaystyle \lim_{n \rightarrow \infty} \frac{1}{n(n-1)(n-2)} \left ( -\frac{14}{27}n^3+n^3 - n^2 \right ) \\
&=& \displaystyle \lim_{n \rightarrow \infty} \frac{\frac{13}{27}n^3 - n^2}{n(n-1)(n-2)} \\
&=& \frac{13}{27}
\end{array}
$$

> __*d*__. Argue that in the $\Omega(n \lg n)$ running time of quicksort, the median-of-3 method affects only the constant factor.

Even if median-of-3 choose the median of $A[p \dots r]$, the running time is still $T(n)=2T(n/2)+\Theta(n)$, which is $\Omega(n \lg n)$.

### 7-6 Fuzzy sorting of intervals

> Consider a sorting problem in which we do not know the numbers exactly. Instead, for each number, we know an interval on the real line to which it belongs. That is, we are given $n$ closed intervals of the form $[a_i, b_i]$, where $a_i \le b_i$. We wish to __*fuzzy-sort*__ these intervals, i.e., to produce a permutation $\left \langle i_1, i_2, \dots, i_n \right \rangle$ of the intervals such that for $j=1,2,\dots,n$, there exist $c_j \in [a_{ij}, b_{ij}]$ satisfying $c_1 \le c_2 \le \dots \le c_n$.

> __*a*__. Design a randomized algorithm for fuzzy-sorting $n$ intervals. Your algorithm should have the general structure of an algorithm that quicksorts the left endpoints (the $a_i$ values), but it should take advantage of overlapping intervals to improve the running time. (As the intervals overlap more and more, the problem of fuzzy-sorting the intervals becomes progressively easier. Your algorithm should take advantage of such overlapping, to the extent that it exists.)

Find the intervals that all have a common overlapping with the pivot, these intervals could be seen as equal since there is a $c$ in the common overlapping. The following is the same as 7.2.

```python
class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __lt__(self, other):
        return self.r < other.l

    def __str__(self):
        return '(' + str(self.l) + ', ' + str(self.r) + ')'

    def get_intersect(self, interval):
        return Interval(max(self.l, interval.l), min(self.r, interval.r))


def partition(a, p, r):
    x = a[r - 1]
    for k in range(p, r - 1):
        next_x = x.get_intersect(a[k])
        if next_x.l <= next_x.r:
            x = next_x
    i = p - 1
    for k in range(p, r - 1):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    j = i
    inter = a[i]
    for k in range(i + 1, r):
        next_x = x.get_intersect(a[k])
        if next_x.l <= next_x.r:
            j += 1
            a[j], a[k] = a[k], a[j]
        k -= 1
    return i, j


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

> __*b*__. Argue that your algorithm runs in expected time $\Theta(n \lg n)$ in general, but runs in expected time $\Theta(n)$ when all of the intervals overlap (i.e., when there exists a value $x$ such that $x \in [a_i, b_i]$ for all $i$ ). Your algorithm should not be checking
for this case explicitly; rather, its performance should naturally improve as the amount of overlap increases.

The algorithm is based on quick-sort, therefore it is $\Theta(n \lg n)$.

If all of the intervals overlap, the partition returns $(1, n)$ immediately, there is no need for further recursion. Thus the expected time is the expected time of partition, which is $\Theta(n)$.
