## 6.1 Heaps

### 6.1-1

> What are the minimum and maximum numbers of elements in a heap of height $$h$$?

Minimum: $$1 + 2 + 2^2 + \dots + 2^{h-1} + 1=2^h$$

Maximum: $$1 + 2 + 2^2 + \dots + 2^h = 2^{h+1} - 1$$

### 6.1-2

> Show that an $$n$$-element heap has height $$\left \lfloor \lg n \right \rfloor$$.

$$
\begin{array}{rrcll}
2^h & \le & n & \le & 2^{h+1} - 1 \\
2^h & \le & n & < & 2^{h+1} \\
h & \le & \lg n & < & h + 1
\end{array}
$$

### 6.1-3

> Show that in any subtree of a max-heap, the root of the subtree contains the largest value occurring anywhere in that subtree.

Transitivity of $$A[i] \ge A[\text{LEFT}(i)], A[i] \ge A[\text{RIGHT}(i)]$$

### 6.1-4

> Where in a max-heap might the smallest element reside, assuming that all elements are distinct?

The leaves.

### 6.1-5

> Is an array that is in sorted order a min-heap?

Yes, since $$\text{PARENT}(i) < i$$, $$A[\text{PARENT}(i)] \le A[i]$$.

### 6.1-6

> Is the array with values $$\left \langle 23, 17, 14, 6, 13, 10, 1, 5, 7, 12 \right \rangle$$ a max-heap?

No, $$6 < 7$$.

### 6.1-7

> Show that, with the array representation for storing an $$n$$-element heap, the leaves are the nodes indexed by $$\left \lfloor n/2 \right \rfloor + 1, \left \lfloor n/2 \right \rfloor + 2, \dots, n$$.

$$
\begin{array}{rll}
\text{LEFT}(i) &>& n \\
2i &>& n \\
i &>& n / 2 \\
i &>& \left \lfloor n/2 \right \rfloor + 1 \\
\end{array}
$$


