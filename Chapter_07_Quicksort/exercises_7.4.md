## 7.4 Analysis of quicksort

### 7.4-1

> Show that in the recurrence 

> $\displaystyle T(n) = \max\_{0 \le q \le n-1}(T(q)+T(n-q-1)) + \Theta(n)$,

> $T(n) = \Omega(n^2)$.

Suppose $T(n) \ge cn^2$,

$$
\begin{array}{rlll}
T(n) &\ge& \displaystyle \max\_{0 \le q \le n-1}(cq^2+c(n-q-1)^2) + dn \\\\
&\ge&  c(n-1)^2+dn & \displaystyle \left ( q=\frac{n-1}{2} \right ) \\\\
&=& cn^2 +(d-2c)n+c & \displaystyle \left (d>2c\right ) \\\\
&\ge& cn^2\\\\
&=& \Omega(n^2)
\end{array}
$$

### 7.4-2

> Show that quicksort’s best-case running time is $\Omega(n \lg n)$.

$T(n)=2T(n/2)+\Theta(n)$, therefore it is $\Omega(n \lg n)$.

### 7.4-3

> Show that the expression $q^2+(n-q-1)^2$ achieves a maximum over $q=0,1, \dots, n-1$ when $q=0$ or $q=n-1$.

Based on the first order derivation on $q$, we know the minimum is achieved when $\displaystyle q=\frac{n-1}{2}$, and the function increases with the same speed when $q$ is away from $\displaystyle \frac{n-1}{2}$ in two directions. Thus the maximum is on the bound of the the variable, $q=0$ and $q=n-1$.

### 7.4-4

> Show that RANDOMIZED-QUICKSORT’s expected running time is $\Omega(n \lg n)$.

$$
\begin{array}{rll}
\text{E}[X] &=& \displaystyle \sum\_{i=1}^{n-1} \sum\_{j=i+1}^n \frac{2}{j-i+1} \\\\
&=& \displaystyle \sum\_{i=1}^{n-1} \sum\_{k=1}^{n-i} \frac{2}{k+1} \\\\
&>& \displaystyle \sum\_{i=1}^{n-1} \sum\_{k=1}^n \frac{1}{k} \\\\
&=& \displaystyle \sum\_{i=1}^{n-1} \Omega(\lg n) \\\\
&=& n\Omega \lg n
\end{array}
$$

### 7.4-5

> We can improve the running time of quicksort in practice by taking advantage of the fast running time of insertion sort when its input is "nearly" sorted. Upon calling quicksort on a subarray with fewer than $k$ elements, let it simply return without sorting the subarray. After the top-level call to quicksort returns, run insertion sort on the entire array to finish the sorting process. Argue that this sorting algorithm runs in $O(nk + n \lg(n/k))$ expected time. How should we pick $k$, both in theory and in practice?

QUICK-SORT: layer number is $O(\lg (n/k))$, therefore it is $O(n \lg (n/k))$.

INSERTION-SORT: each subarray is $O(k^2)$, the number of subarrays is $O(n/k)$, therefore it is $O(nk)$.

Therefore this sorting algorithm runs in $O(nk + n \lg(n/k))$.

In practice we should use profiling.

### 7.4-6 $\star$

> Consider modifying the PARTITION procedure by randomly picking three elements from array $A$ and partitioning about their median (the middle value of the three elements). Approximate the probability of getting at worst an $\alpha$-to-$(1-\alpha)$ split, as a function of $\alpha$ in the range $0 < \alpha < 1$.

The worst case happens when at least two of the chose elements are in the $\alpha n$ smallest or largest set, thus the probability of a worse case is 

$$
2 \left (\alpha^3 + \binom{3}{1}\alpha^2(1-\alpha)\right )=6\alpha^2-4\alpha^3
$$

The complementary is $1-6\alpha^2+4\alpha^3$.
