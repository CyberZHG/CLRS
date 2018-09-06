## Problems

### 17-1 Bit-reversed binary counter

> Chapter 30 examines an important algorithm called the fast Fourier transform, or FFT. The first step of the FFT algorithm performs a __*bit-reversal permutation*__ on an input array $A[0 \dots n-1]$ whose length is $n = 2^k$ for some nonnegative integer $k$. This permutation swaps elements whose indices have binary representations that are the reverse of each other.

> We can express each index $a$ as a $k$-bit sequence $\langle a_{k-1}, a_{k-2}, \dots, a_0 \rangle$, where $a = \sum_{i=0}^{k-1} a_i 2^i$. We define

> $\text{rev}_k(\langle a_{k-1}, a_{k-2}, \dots, a_0 \rangle) = \langle a_0, a_1, \dots, a_{k-1} \rangle$;

> thus,

> $\displaystyle \text{rev}_k(a) = \sum_{i=0}^{k-1} a_{k-i-1} 2^i$.

> For example, if $n = 16$ (or, equivalently, $k = 4$), then $\text{rev}_k(3) = 12$, since the $4$-bit representation of $3$ is $0011$, which when reversed gives $1100$, the $4$-bit representation of $12$.

> __*a*__. Given a function $\text{rev}_k$ that runs in $\Theta(k)$ time, write an algorithm to perform the bit-reversal permutation on an array of length $n = 2^k$ in $O(nk)$ time.

```python
def rev_k(k, a):
    x = 0
    for _ in xrange(k):
        x <<= 1
        x += a & 1
        a >>= 1
    return x
```

> We can use an algorithm based on an amortized analysis to improve the running time of the bit-reversal permutation. We maintain a "bit-reversed counter" and a procedure BIT-REVERSED-INCREMENT that, when given a bit-reversed-counter value $a$, produces $\text{rev}_k(\text{rev}_k(a) + 1)$. If $k = 4$, for example, and the bit-reversed counter starts at $0$, then successive calls to BIT-REVERSED-INCREMENT produce the sequence

> $0000, 1000, 0100, 1100, 0010, 1010, \dots = 0, 8, 4, 12, 2, 10, \dots$.

> __*b*__. Assume that the words in your computer store $k$-bit values and that in unit time, your computer can manipulate the binary values with operations such as shifting left or right by arbitrary amounts, bitwise-AND, bitwise-OR, etc. Describe an implementation of the BIT-REVERSED-INCREMENT procedure that allows the bit-reversal permutation on an $n$-element array to be performed in a total of $O(n)$ time.

```python
class BitReversedCounter:
    def __init__(self, k):
        self.k = k
        self.c = 0

    def increment(self):
        for i in xrange(self.k - 1, -1, -1):
            self.c ^= 1 << i
            if self.c & (1 << i) > 0:
                break
        return self.c
```

> __*c*__. Suppose that you can shift a word left or right by only one bit in unit time. Is it still possible to implement an $O(n)$-time bit-reversal permutation?

```python
class BitReversedCounter:
    def __init__(self, k):
        self.k = k
        self.c = 0
        self.n = 1 << (self.k - 1)

    def increment(self):
        i = self.n
        for _ in xrange(self.k - 1, -1, -1):
            self.c ^= i
            if self.c & i > 0:
                break
            i >>= 1
        return self.c
```

### 17-2 Making binary search dynamic

> Binary search of a sorted array takes logarithmic search time, but the time to insert a new element is linear in the size of the array. We can improve the time for insertion by keeping several sorted arrays.

> Specifically, suppose that we wish to support SEARCH and INSERT on a set of $n$ elements. Let $k = \lceil \lg(n + 1) \rceil$, and let the binary representation of $n$ be $\langle n_{k-1}, n_{k-2}, \dots, n_0 \rangle$. We have $k$ sorted arrays $A_0, A_1, \dots, A_{k-1}$, where for $i = 0, 1, \dots, k - 1$, the length of array $A_i$ is $2^i$. Each array is either full or empty, depending on whether $n_i = 1$ or $n_i = 0$, respectively. The total number of elements held in all $k$ arrays is therefore $\sum_{i=0}^{k-1} n_i 2^i = n$. Although each individual array is sorted, elements in different arrays bear no particular relationship to each other.

> __*a*__. Describe how to perform the SEARCH operation for this data structure. Analyze its worst-case running time.

$O(\lg^2 n)$

> __*b*__. Describe how to perform the INSERT operation. Analyze its worst-case and amortized running times.

Merge sort.

Worst: $O(n)$

Amortized: $O(\lg n)$

> __*c*__. Discuss how to implement DELETE.

### 17-3 Amortized weight-balanced trees

> Consider an ordinary binary search tree augmented by adding to each node $x$ the attribute $x.size$ giving the number of keys stored in the subtree rooted at $x$. Let $\alpha$ be a constant in the range $1/2 \le \alpha < 1$. We say that a given node $x$ is __*$\alpha$-balanced*__ if $x.left.size \le \alpha \cdot x.size$ and $x.right.size \le \alpha \cdot x.size$. The tree as a whole is __*$\alpha$-balanced*__ if every node in the tree is $\alpha$-balanced. The following amortized approach to maintaining weight-balanced trees was suggested by G. Varghese.

> __*a*__. A $1/2$-balanced tree is, in a sense, as balanced as it can be. Given a node $x$ in an arbitrary binary search tree, show how to rebuild the subtree rooted at $x$ so that it becomes $1/2$-balanced. Your algorithm should run in time $\Theta(x.size)$, and it can use $O(x.size)$ auxiliary storage.

Choose the middle node as the root.

> __*b*__. Show that performing a search in an $n$-node $\alpha$-balanced binary search tree takes $O(\lg n)$ worst-case time.

Let $\beta = 1 / \alpha$, $\beta^k = n$, $k = \log_\beta n = O(\log n) = O(\lg n)$.

> For the remainder of this problem, assume that the constant $\alpha$ is strictly greater than $1/2$. Suppose that we implement INSERT and DELETE as usual for an $n$-node binary search tree, except that after every such operation, if any node in the tree is no longer $\alpha$-balanced, then we "rebuild" the subtree rooted at the highest such node in the tree so that it becomes $1/2$-balanced.

> We shall analyze this rebuilding scheme using the potential method. For a node $x$ in a binary search tree $T$, we define

> $\Delta(x) = | x.left.size - x.right.size |$,

> and we define the potential of $T$ as

> $\displaystyle \Phi(T) = c \sum_{x \in T: \Delta(x) \ge 2} \Delta(x)$,

> where $c$ is a sufficiently large constant that depends on $\alpha$.

> __*c*__. Argue that any binary search tree has nonnegative potential and that a $1/2$-balanced tree has potential 0.

$\Delta(x) \ge 0$: nonnegative potential.

$1/2$-balanced: $\Delta(x) \le 1$, $\Phi(T) = 0$.

> __*d*__. Suppose that $m$ units of potential can pay for rebuilding an $m$-node subtree. How large must $c$ be in terms of $\alpha$ in order for it to take $O(1)$ amortized time to rebuild a subtree that is not $\alpha$-balanced?

$$
\begin{array}{rll}
\hat{c_i} &=& c_i + \Phi(D_i) - \Phi(D_{i-1}) \\
O(1) &=& m + \Phi(D_i) - \Phi(D_{i-1}) \\
\Phi(D_{i-1}) &=& m + \Phi(D_i) \\
\Phi(D_{i-1}) &\ge& m
\end{array}
$$

$$
\begin{array}{rll}
\Delta(x) &=& x.left.size - x.right.size \\
&\ge& \alpha \cdot m - ((1 - \alpha) m - 1) \\
&=& (2\alpha - 1)m + 1
\end{array}
$$

$$
\begin{array}{rll}
m &\le& c((2\alpha - 1)m + 1) \\
c &\ge& \displaystyle \frac{m}{(2\alpha - 1)m + 1} \\
&\ge& \displaystyle \frac{1}{2\alpha}
\end{array}
$$

> __*e*__. Show that inserting a node into or deleting a node from an $n$-node $\alpha$-balanced tree costs $O(\lg n)$ amortized time.
