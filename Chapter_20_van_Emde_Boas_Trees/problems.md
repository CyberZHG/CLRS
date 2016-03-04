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

```python
    def get_cluster(self, x):
        if self.cluster[x] is None:
            self.cluster[x] = VanEmdeBoasTree(self.sqrt_l)
        return self.cluster[x]

    def get_summary(self):
        if self.summary is None:
            self.summary = VanEmdeBoasTree(self.sqrt_h)
        return self.summary
        
    def insert(self, x):
        if self.min is None:
            self.insert_empty(x)
        else:
            if x < self.min:
                x, self.min = self.min, x
            if not self.is_leaf():
                if self.get_cluster(self.high(x)).minimum() is None:
                    self.get_summary().insert(self.high(x))
                    self.get_cluster(self.high(x)).insert_empty(self.low(x))
                else:
                    self.get_cluster(self.high(x)).insert(self.low(x))
            if x > self.max:
                self.max = x
```

> __*d*__. Modify the VEB-TREE-SUCCESSOR procedure to produce pseudocode for the procedure RS-VEB-TREE-SUCCESSOR$$(V, x)$$, which returns the successor of $$x$$ in RS-vEB tree $$V$$, or NIL if $$x$$ has no successor in $$V$$.

```python
    def successor(self, x):
        if self.is_leaf():
            if x == 0 and self.max == 1:
                return 1
            return None
        if self.min is not None and x < self.min:
            return self.min
        max_low = self.get_cluster(self.high(x)).maximum()
        if max_low is not None and self.low(x) < max_low:
            offset = self.get_cluster(self.high(x)).successor(self.low(x))
            return self.index(self.high(x), offset)
        succ_cluster = self.get_summary().successor(self.high(x))
        if succ_cluster is None:
            return None
        offset = self.cluster[succ_cluster].minimum()
        return self.index(succ_cluster, offset)
```

> __*e*__. Prove that, under the assumption of simple uniform hashing, your RS-VEBTREE-INSERT and RS-VEB-TREE-SUCCESSOR procedures run in $$O(\lg \lg u)$$ expected time.

The hashing tasks about $$\Theta(1)$$ time, thus the procedures run in $$O(\lg \lg u)$$.

> __*f*__. Assuming that elements are never deleted from a vEB tree, prove that the space requirement for the RS-vEB tree structure is $$O(n)$$, where $$n$$ is the number of elements actually stored in the RS-vEB tree.

> __*g*__. RS-vEB trees have another advantage over vEB trees: they require less time to create. How long does it take to create an empty RS-vEB tree?

$$\Theta(\sqrt{u})$$ to create the hash table.

### 20-2 y-fast tries

> This problem investigates D. Willard's "y-fast tries" which, like van Emde Boas trees, perform each of the operations MEMBER, MINIMUM, MAXIMUM, PREDECESSOR, and SUCCESSOR on elements drawn from a universe with size $$u$$ in $$O(\lg\lg u)$$ worst-case time. The INSERT and DELETE operations take $$O(\lg\lg u)$$ amortized time. Like reduced-space van Emde Boas trees (see Problem 20-1), yfast tries use only $$O(n)$$ space to store $$n$$ elements. The design of y-fast tries relies on perfect hashing (see Section 11.5).

> As a preliminary structure, suppose that we create a perfect hash table containing not only every element in the dynamic set, but every prefix of the binary representation of every element in the set. For example, if $$u = 16$$, so that $$\lg u = 4$$, and $$x = 13$$ is in the set, then because the binary representation of $$13$$ is $$1101$$, the perfect hash table would contain the strings $$1$$, $$11$$, $$110$$, and $$1101$$. In addition to the hash table, we create a doubly linked list of the elements currently in the set, in increasing order.

> __*a*__. How much space does this structure require?

$$O(u)$$

> __*b*__. Show how to perform the MINIMUM and MAXIMUM operations in $$O(1)$$ time; the MEMBER, PREDECESSOR, and SUCCESSOR operations in $$O(\lg \lg u)$$ time; and the INSERT and DELETE operations in $$O(\lg u)$$ time.

> To reduce the space requirement to $$O(n)$$, we make the following changes to the data structure:

> * We cluster the $$n$$ elements into $$n / \lg u$$ groups of size $$\lg u$$. (Assume for now that $$\lg u$$ divides $$n$$.) The first group consists of the $$\lg u$$ smallest elements in the set, the second group consists of the next $$\lg u$$ smallest elements, and so on.

> * We designate a "representative" value for each group. The representative of the $$i$$th group is at least as large as the largest element in the $$i$$th group, and it is smaller than every element of the $$(i+1)$$st group. (The representative of the last group can be the maximum possible element $$u - 1$$.) Note that a representative might be a value not currently in the set.

> * We store the $$\lg u$$ elements of each group in a balanced binary search tree, such as a red-black tree. Each representative points to the balanced binary search tree for its group, and each balanced binary search tree points to its group's representative.

> * The perfect hash table stores only the representatives, which are also stored in a doubly linked list in increasing order.

> We call this structure a __*y-fast trie*__.

> __*c*__. Show that a y-fast trie requires only $$O(n)$$ space to store $$n$$ elements.
 
> __*d*__. Show how to perform the MINIMUM and MAXIMUM operations in $$O(\lg lg u)$$ time with a y-fast trie.

> __*e*__. Show how to perform the MEMBER operation in $$O(\lg \lg u)$$ time.

> __*f*__. Show how to perform the PREDECESSOR and SUCCESSOR operations in
$$O(\lg \lg u)$$ time.

> __*g*__. Explain why the INSERT and DELETE operations take $$\Omega(\lg \lg u)$$ time.

> __*h*__. Show how to relax the requirement that each group in a y-fast trie has exactly $$\lg u$$ elements to allow INSERT and DELETE to run in $$O(\lg \lg u)$$ amortized time without affecting the asymptotic running times of the other operations.
