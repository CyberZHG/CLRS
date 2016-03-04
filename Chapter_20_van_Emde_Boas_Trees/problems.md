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
> In order to reduce the space requirements, let us define a __*reduced-space van Emde Boas tree*__, or __*RS-vEB tree*__, as a __*vEB tree*__ $$V$$ but with the following changes:

> * The attribute $$V.cluster$$, rather than being stored as a simple array of pointers to vEB trees with universe size $$\sqrt{u}$$, is a hash table (see Chapter 11) stored as a dynamic table (see Section 17.4). Corresponding to the array version of $$V.cluster$$, the hash table stores pointers to RS-vEB trees with universe size $$\sqrt{u}$$. To find the $$i$$th cluster, we look up the key $$i$$ in the hash table, so that we can find the $$i$$th cluster by a single search in the hash table.
> * The hash table stores only pointers to nonempty clusters. A search in the hash table for an empty cluster returns NIL, indicating that the cluster is empty.
> * The attribute $$V.summary$$ is NIL if all clusters are empty. Otherwise, $$V.summary$$ points to an RS-vEB tree with universe size $$\sqrt{u}$$.

> Because the hash table is implemented with a dynamic table, the space it requires is proportional to the number of nonempty clusters.

> When we need to insert an element into an empty RS-vEB tree, we create the RS-vEB tree by calling the following procedure, where the parameter u is the universe size of the RS-vEB tree:

> ```
CREATE-NEW-RS-VEB-TREE(u)
1  allocate a new vEB tree V
2  V.u = u
3  V.min = NIL
4  V.max = NIL
5  V.summary = NIL
6  create V.cluster as an empty dynamic hash table
7  return V
```

> __*c*__. Modify the VEB-TREE-INSERT procedure to produce pseudocode for the procedure RS-VEB-TREE-INSERT$$(V, x)$$, which inserts $$x$$ into the RS-vEB tree $$V$$, calling CREATE-NEW-RS-VEB-TREE as appropriate.

> __*d*__. Modify the VEB-TREE-SUCCESSOR procedure to produce pseudocode for the procedure RS-VEB-TREE-SUCCESSOR$$(V, x)$$, which returns the successor of $$x$$ in RS-vEB tree $$V$$ , or NIL if $$x$$ has no successor in $$V$$.

> __*e*__. Prove that, under the assumption of simple uniform hashing, your RS-VEBTREE-INSERT and RS-VEB-TREE-SUCCESSOR procedures run in $$O(\lg \lg u)$$ expected time.

> __*f*__. Assuming that elements are never deleted from a vEB tree, prove that the space requirement for the RS-vEB tree structure is $$O(n)$$, where $$n$$ is the number of elements actually stored in the RS-vEB tree.

> __*g*__. RS-vEB trees have another advantage over vEB trees: they require less time to create. How long does it take to create an empty RS-vEB tree?

