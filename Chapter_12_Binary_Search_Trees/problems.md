## Problems

### 12-1 Binary search trees with equal keys

> Equal keys pose a problem for the implementation of binary search trees.

> __*a*__. What is the asymptotic performance of TREE-INSERT when used to insert $n$ items with identical keys into an initially empty binary search tree?

$\Theta(n)$

> __*b*__. Keep a boolean flag $x.b$ at node $x$, and set $x$ to either $x.left$ or $x.right$ based on the value of $x.b$, which alternates between FALSE and TRUE each time we visit $x$ while inserting a node with the same key as $x$.

$\Theta(n \lg n)$

> __*c*__. Keep a list of nodes with equal keys at $x$, and insert $z$ into the list.

If linked list is used, it could be $\Theta(1)$.

> __*d*__. Randomly set $x$ to either $x.left$ or $x.right$. (Give the worst-case performance and informally derive the expected running time.)

Worst: $\Theta(n)$.

Expected: $\Theta(n \lg n)$.

### 12-2 Radix trees

> Given two strings $a = a_0a_1 \dots a_p$ and $b = b_0b_1 \dots b_q$, where each $a_i$ and each $b_j$ is in some ordered set of characters, we say that string $a$ is lexicographically less
than string $b$ if either
1. there exists an integer $j$, where $0 \le j \le \min(p, q)$, such that $a_i = b_i$ for all $i = 0, 1, \dots j - 1$ and $a_j < b_j$, or
2. $p < q$ and $a_i = b_i$ for all $i = 0, 1, \dots, p$.

> The radix tree data structure shown in Figure 12.5 stores the bit strings 1011, 10, 011, 100, and 0. When searching for a key $a = a_0a_1 \dots a_p$, we go left at a node of depth $i$ if $a_i = 0$ and right if $a_i = 1$. Let $S$ be a set of distinct bit strings whose lengths sum to $n$. Show how to use a radix tree to sort $S$ lexicographically in $\Theta(n)$ time. For the example in Figure 12.5, the output of the sort should be the sequence 0, 011, 10, 100, 1011.

Insert all the bit strings into radix tree costs $\Theta(n)$, then use preorder tree walk to sort the strings costs $\Theta(n)$, the total cost is still $\Theta(n)$.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RadixTree:
    def __init__(self):
        self.root = None

    def insert(self, a):
        self.root = self.insert_rec(self.root, a, 0)

    def insert_rec(self, root, a, idx):
        if idx == len(a):
            if root is None:
                return TreeNode(a)
            root.val = a
            return root
        if root is None:
            root = TreeNode(None)
        if a[idx] == '0':
            root.left = self.insert_rec(root.left, a, idx+1)
        else:
            root.right = self.insert_rec(root.right, a, idx+1)
        return root

    def sorted(self):
        self.sorted_list = []
        self.sorted_rec(self.root)
        return self.sorted_list

    def sorted_rec(self, root):
        if root is None:
            return
        if root.val is not None:
            self.sorted_list.append(root.val)
        self.sorted_rec(root.left)
        self.sorted_rec(root.right)


def sort_strings(strs):
    radix_tree = RadixTree()
    for s in strs:
        radix_tree.insert(s)
    return radix_tree.sorted()
```

### 12-3 Average node depth in a randomly built binary search tree

> In this problem, we prove that the average depth of a node in a randomly built binary search tree with n nodes is $O(\lg n)$. Although this result is weaker than that of Theorem 12.4, the technique we shall use reveals a surprising similarity between the building of a binary search tree and the execution of RANDOMIZED-QUICKSORT from Section 7.3.

> We define the __*total path length*__ $P(T)$ of a binary tree $T$ as the sum, over all nodes $x$ in $T$ , of the depth of node $x$, which we denote by $d(x, T)$.

> __*a*__. Argue that the average depth of a node in $T$ is

> $\displaystyle \frac{1}{n} \sum_{x \in T} d(x, T) = \frac{1}{n} P(T)$.

Obviously.

> Thus, we wish to show that the expected value of $P(T)$ is $O(n \lg n)$.

> __*b*__. Let $T_L$ and $T_R$ denote the left and right subtrees of tree $T$, respectively. Argue that if $T$ has $n$ nodes, then

> $P(T) = P(T_L) + P(T_R) + n - 1$.

There are $n-1$ nodes in $P(T_L)$ and $P(T_R)$, each increase by 1.

> __*c*__. Let $P(n)$ denote the average total path length of a randomly built binary search tree with n nodes. Show that

> $\displaystyle P(n) = \frac{1}{n} \sum_{i=0}^{n-1} (P(i) + P(n-i-1) + n - 1)$.

The root is equally likely to be the rank in $[1, n]$.

> __*d*__. Show how to rewrite $P(n)$ as

> $\displaystyle P(n) = \frac{2}{n} \sum_{k=1}^{n-1} P(k) + \Theta(n)$.

Each item $P(1), P(2), \dots, P(n)$ appears twice in the summation, and

$$
\frac{1}{n} \sum_{i=0}^{n-1} n - 1 = \frac{(n-3)n}{2n} = \Theta(n)
$$

> __*e*__. Recalling the alternative analysis of the randomized version of quicksort given in Problem 7-3, conclude that $P(n) = O(n \lg n)$.

Based on Problem 7-3,  $P(n) = O(n \lg n)$.

> __*f*__. Describe an implementation of quicksort in which the comparisons to sort a set of elements are exactly the same as the comparisons to insert the elements into a binary search tree.

Choose the pivot that it has the lowest index in the original list.

### 12-4 Number of different binary trees

> Let $b_n$ denote the number of different binary trees with $n$ nodes. In this problem, you will find a formula for $b_n$, as well as an asymptotic estimate.

> __*a*__. Show that $b_0 = 1$ and that, for $n \ge 1$,

> $\displaystyle b_n = \sum_{k=0}^{n-1} b_k b_{n-1-k}$.

A root with two subtree.

> __*b*__. Referring to Problem 4-4 for the definition of a generating function, let $B(x)$ be the generating function

> $\displaystyle B(x) = \sum_{n=0}^\infty b_n x^n$.

$$
\begin{array}{rll}
B(x)^2 &=& (b_0 x^0 + b_1 x^1 + b_2 x^2 + \dots) ^ 2 \\
&=& b_0^2 x^0 + (b_0 b_1 + b_1 b_0) x^1 + (b_0 b_2 + b_1 b_1 + b_2 b_0) x^2 + \dots \\
&=& \displaystyle \sum_{k=0}^0 b_k b_{0-k} x^0 + \sum_{k=0}^1 b_k b_{1-k} x^1 + \sum_{k=0}^2 b_k b_{2-k} x^2 + \dots \\
\end{array}
$$

$$
\begin{array}{rll}
xB(x)^2 + 1 &=& \displaystyle 1 + \sum_{k=0}^0 b_k b_{1-1-k} x^1 + \sum_{k=0}^2 b_k b_{2-1-k} x^3 + \sum_{k=0}^2 b_k b_{3-1-k} x^2 + \dots \\
&=& 1 + b_1 x^1 + b_2 x^2 + b_3 x^3 + \dots \\
&=& b_0 x^0 + b_1 x^1 + b_2 x^2 + b_3 x^3 + \dots \\
&=& \displaystyle \sum_{n=0}^\infty b_n x^n \\
&=& B(x)
\end{array}
$$

> Show that $B(x) = x B(x)^2 + 1$, and hence one way to express $B(x)$ in closed form is

> $\displaystyle B(x) = \frac{1}{2x} (1 - \sqrt{1 - 4x})$.

$$
\begin{array}{rll}
x B(x)^2 + 1 &=& \displaystyle x \cdot \frac{1}{4x^2} (1 + 1 - 4x - 2\sqrt{1 - 4x}) + 1 \\
&=& \displaystyle \frac{1}{4x} (2 - 2\sqrt{1 - 4x}) - 1 + 1 \\
&=& \displaystyle \frac{1}{2x} (1 - \sqrt{1 - 4x}) \\
&=& B(x)
\end{array}
$$

> The __*Taylor expansion*__ of $f(x)$ around the point $x=a$ is given by

> $\displaystyle f(x) = \sum_{k=0}^\infty \frac{f^{(k)}(a)}{k!} (x - a)^k$,

> where $f^{(k)}(a)$ is the $k$th derivative of $f$ evaluated at $x$.

> __*c*__. Show that

> $\displaystyle b_n = \frac{1}{n+1} \binom{2n}{n}$

> (the $n$th Catalan number) by using the Taylor expansion of $\sqrt{1-4x}$ around $x=0$. 

Let $f(x) = \sqrt{1-4x}$,

The numerator of the derivative is 

$\begin{array}{rll}
2 \cdot (1 \cdot 2) \cdot (3 \cdot 2) \cdot (5 \cdot 2)\cdots &=&
\displaystyle 2^k \cdot \prod_{i=0}^{k - 2}(2k+1) \\
&=& 2^k \cdot \frac{\displaystyle (2(k-1))!}{\displaystyle 2^{k-1}(k-1)!} \\
&=& \frac{\displaystyle 2(2(k-1))!}{\displaystyle (k-1)!} \\
\end{array}
$$

$\displaystyle f(x) = 1 - 2x - 2x^2 - 4 x^3 - 10x^4 - 28x^5 - \dots$

The coefficient is $\frac{\displaystyle 2(2(k-1))!}{\displaystyle k!(k-1)!}$.

$\begin{array}{rll}
B(x) &=& \displaystyle \frac{1}{2x}(1-f(x)) \\
&=& 1 + x + 2x^2 + 5x^3 + 14x^4 + \dots \\
&=& \displaystyle \sum_{n=0}^\infty \frac{\displaystyle (2n)!}{\displaystyle (n+1)!n!} x \\
&=& \displaystyle \sum_{n=0}^\infty \frac{1}{n+1} \frac{\displaystyle (2n)!}{\displaystyle n!n!} x \\
&=& \displaystyle \sum_{n=0}^\infty \frac{1}{n+1} \binom{2n}{n} x
\end{array}
$$

Therefore $\displaystyle b_n = \frac{1}{n+1} \binom{2n}{n}$.

> __*d*__. Show that

> $\displaystyle b_n = \frac{4^n}{\sqrt{\pi}n^{3/2}} (1 + O(1/n))$.

Based on Stirling's approximation $\displaystyle n! \approx \sqrt{2 \pi n} \left ( \frac{n}{e} \right )^n$,

$$
\begin{array}{rll}
b_n &=& \displaystyle \frac{1}{n+1} \frac{\displaystyle (2n)!}{\displaystyle n!n!} \\
&\approx& \displaystyle \frac{1}{n+1} \frac{\sqrt{4 \pi n}(2n / e)^{2n}}{2 \pi n (n/e)^{2n}} \\
&=& \displaystyle \frac{1}{n+1} \frac{4^n}{\sqrt{\pi n} } \\
&=& \displaystyle \left ( \frac{1}{n} + \left ( \frac{1}{n+1} - \frac{1}{n} \right ) \right ) \frac{4^n}{\sqrt{\pi n} } \\
&=& \displaystyle \left ( \frac{1}{n} - \frac{1}{n^2+n} \right ) \frac{4^n}{\sqrt{\pi n} } \\
&=& \displaystyle \frac{1}{n} \left (1  - \frac{1}{n+1} \right ) \frac{4^n}{\sqrt{\pi n} } \\
&=& \displaystyle \frac{4^n}{\sqrt{\pi}n^{3/2}} (1 + O(1/n))
\end{array}
$$
