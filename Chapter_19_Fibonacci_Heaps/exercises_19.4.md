## 19.4 Bounding the maximum degree

### 19.4-1

> Professor Pinocchio claims that the height of an $n$-node Fibonacci heap is $O(\lg n)$. Show that the professor is mistaken by exhibiting, for any positive integer $n$, a sequence of Fibonacci-heap operations that creates a Fibonacci heap consisting of just one tree that is a linear chain of $n$ nodes.

Initialize: insert 3 numbers then extract-min.

Iteration: insert 3 numbers, in which at least two numbers are less than the root of chain, then extract-min. The smallest newly inserted number will be extracted and the remaining two numbers will form a heap whose degree of root is 1, and since the root of the heap is less than the old chain, the chain will be merged into the newly created heap. Finally we should delete the node which contains the largest number of the 3 inserted numbers.

### 19.4-2

> Suppose we generalize the cascading-cut rule to cut a node $x$ from its parent as soon as it loses its $k$th child, for some integer constant $k$. (The rule in Section 19.3 uses $k = 2$.) For what values of $k$ is $D(n) = O(\lg n)$?
