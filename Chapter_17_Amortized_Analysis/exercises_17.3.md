## 17.3 The potential method

### 17.3-1

> Suppose we have a potential function $$\Phi$$ such that $$\Phi(D_i) \ge \Phi(D_0)$$ for all $$i$$, but $$\Phi(D_0) \ne 0$$. Show that there exists a potential fuction $$\Phi'$$ such that $$\Phi'(D_0) = 0$$, $$\Phi'(D_i) \ge 0$$ for all $$i \ge 1$$, and the amortized costs using $$\Phi'$$ are the same as the amortized costs using $$\Phi$$.

$$\Phi'(D_i) = \Phi(D_i) - \Phi(D_0)$$

### 17.3-2

> Redo Exercise 17.1-3 using a potential method of analysis.

### 17.3-3

> Consider an ordinary binary min-heap data structure with $$n$$ elements supporting the instructions INSERT and EXTRACT-MIN in $$O(\lg n)$$ worst-case time. Give a potential function $$\Phi$$ such that the amortized cost of INSERT is $$O(\lg n)$$ and the amortized cost of EXTRACT-MIN is $$O(1)$$, and show that it works.

$$\Phi(D_i)=$$ number of elements in the heap$$\times \lg n$$.

INSERT: $$\Phi(D_i) = O(\lg n) + \lg n = O(\lg n)$$.

EXTRACT-MIN: $$\Phi(D_i) = O(\lg n) - \lg n = O(1)$$.

### 17.3-4

> What is the total cost of executing $$n$$ of the stack operations PUSH, POP, and MULTIPOP, assuming that the stack begins with $$s_0$$ objects and finishes with $$s_n$$ objects?

$$
\begin{array}{rll}
\displaystyle \sum_{i=1}^n c_i 
&=& \displaystyle \sum_{i=1}^n \hat{c_i} - \Phi(D_n) + \Phi(D_0) \\
&=& n - s_n + s_0
\end{array}
$$
### 17.3-5

> Suppose that a counter begins at a number with $$b$$ 1s in its binary representation, rather than at 0. Show that the cost of performing $$n$$ INCREMENT operations is $$O(n)$$ if $$n = \Omega(b)$$. (Do not assume that $$b$$ is constant.)

$$
\begin{array}{rll}
\displaystyle \sum_{i=1}^n c_i 
&=& \displaystyle \sum_{i=1}^n \hat{c_i} - \Phi(D_n) + \Phi(D_0) \\
&=& n - x + b \\
&\le& n - x + n \\
&=& O(n)
\end{array}
$$
### 17.3-6

> Show how to implement a queue with two ordinary stacks (Exercise 10.1-6) so that the amortized cost of each ENQUEUE and each DEQUEUE operation is $$O(1)$$.

$$\Phi(D_i) = $$ number of elements in the first stack.

### 17.3-7

> Design a data structure to support the following two operations for a dynamic multiset $$S$$ of integers, which allows duplicate values:

> INSERT$$(S, x)$$ inserts $$x$$ into $$S$$.

> DELETE-LARGER-HALF$$(S)$$ deletes the largest $$\lceil |S| / 2 \rceil$$ elements from $$S$$.

> Explain how to implement this data structure so that any sequence of $$m$$ INSERT and DELETE-LARGER-HALF operations runs in $$O(m)$$ time. Your implementation should also include a way to output the elements of $$S$$ in $$O(|S|)$$ time.

An array of elements.

INSERT: push the element to the back of the array.

DELETE-LARGER-HALF: find the median in $$O(n)$$ and delete the first $$\lceil |S| / 2 \rceil$$ elements that are larger or equal to the median.
