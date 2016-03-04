## Problems

### 20-1 Space requirements for van Emde Boas trees

> This problem explores the space requirements for van Emde Boas trees and suggests a way to modify the data structure to make its space requirement depend on the number $$n$$ of elements actually stored in the tree, rather than on the universe size $$u$$. For simplicity, assume that $$\sqrt{u}$$ is always an integer.

> __*a*__. Explain why the following recurrence characterizes the space requirement $$P(u)$$ of a van Emde Boas tree with universe size u:

> $$P(u) = (\sqrt{u} + 1) P(\sqrt{u}) + \Theta(\sqrt{u})$$

$$\sqrt{u}$$: number of clusters.

$$1$$: number of summary.

$$P(\sqrt{u})$$: space of cluster/summary.

$$\Theta(\sqrt{u})$$: pointers of clusters.

> __*b*__. Prove that recurrence (20.5) has the solution $$P(u) = O(u)$$.

Suppose $$P(u) \le cu - d$$,

$$
\begin{array}{rlll}
P(u) &=& (\sqrt{u} + 1) P(\sqrt{u}) + \Theta(\sqrt{u}) \\
&\le& (\sqrt{u} + 1) \cdot c \cdot (\sqrt{u} - d) + \Theta(\sqrt{u}) \\
&=& cu + c(1-d)\sqrt{u} - cd + \Theta(\sqrt{u}) & (d > 1)\\
&\le& cu
\end{array}
$$
