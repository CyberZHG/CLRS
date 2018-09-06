## 7.2 Performance of quicksort

### 7.2-1

> Use the substitution method to prove that the recurrence $T(n) = T(n - 1) + \Theta(n)$has the solution $T(n)=\Theta(n^2)$, as claimed at the beginning of Section 7.2.

Suppose $T(n) \le cn^2-an$,

$$
\begin{array}{rlll}
T(n) &\le& c(n-1)^2-a(n-1) + dn \\\\
&=&  cn^2 + (d - 2c)n + c & \displaystyle (d < 2c, n \ge \frac{c}{2c-d}) \\\\
&\le& cn^2 \\\\
\end{array}
$$

### 7.2-2

> What is the running time of QUICKSORT when all elements of array A have the
same value?

$T(n)=T(n-1)+\Theta(n)$

$T(n)=\Theta(n^2)$

### 7.2-3

> Show that the running time of QUICKSORT is $\Theta(n^2)$ when the array $A$ contains distinct elements and is sorted in decreasing order.

$T(n)=T(n-1)+\Theta(n)$

$T(n)=\Theta(n^2)$

### 7.2-4

> Banks often record transactions on an account in order of the times of the transactions, but many people like to receive their bank statements with checks listed in order by check number. People usually write checks in order by check number, and merchants usually cash them with reasonable dispatch. The problem of converting time-of-transaction ordering to check-number ordering is therefore the problem of sorting almost-sorted input. Argue that the procedure INSERTION-SORT would tend to beat the procedure QUICKSORT on this problem.

INSERTION-SORT is $\Omega(n)$ while $QUCIKSORT$ is $\Omega(n^2)$

### 7.2-5

> Suppose that the splits at every level of quicksort are in the proportion $1-\alpha$ to $\alpha$, where $0 < \alpha \le 1/2$ is a constant. Show that the minimum depth of a leaf in the recursion tree is approximately $-\lg n / \lg \alpha$ and the maximum depth is approximately $-\lg n/\lg(1-\alpha)$. (Don't worry about integer round-off.)

Let $x$ be the minimum depth,

$$
\begin{array}{rll}
n\alpha^x &\le& 1 \\\\
\alpha^x &\le& n^{-1} \\\\
x &\ge& \log\_\alpha{n^{-1}} \\\\
x &\ge& -\lg n / \lg \alpha \\\\
\end{array}
$$

Let $y$ be the maximum depth,

$$
\begin{array}{rll}
n(1-\alpha)^y &\le& 1 \\\\
(1-\alpha)^y &\le& n^{-1} \\\\
y &\ge& \log\_{(1-\alpha)}{n^{-1}} \\\\
y &\ge& -\lg n / \lg (1-\alpha) \\\\
\end{array}
$$

### 7.2-6 $\star$

> Argue that for any constant $0 < \alpha \le 1/2$, the probability is approximately $1 - 2\alpha$, that on a random input array, PARTITION produces a split more balanced than $1-\alpha$ to $\alpha$.

In order to make a partition which is less balanced, the pivot should belong to either the largest $\alpha n$ elements or the smallest $\alpha n$ elements. Thus a better partition is approximately $\displaystyle \frac{n-2\alpha n}{n} = 1 - 2\alpha$.
