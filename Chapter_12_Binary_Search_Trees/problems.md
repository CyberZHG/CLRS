## Problems

### 12-1 Binary search trees with equal keys

> Equal keys pose a problem for the implementation of binary search trees.

> __*a*__. What is the asymptotic performance of TREE-INSERT when used to insert $$n$$ items with identical keys into an initially empty binary search tree?

$$\Theta(n)$$

> __*b*__. Keep a boolean flag $$x.b$$ at node $$x$$, and set $$x$$ to either $$x.left$$ or $$x.right$$ based on the value of $$x.b$$, which alternates between FALSE and TRUE each time we visit $$x$$ while inserting a node with the same key as $$x$$.

$$\Theta(n \lg n)$$

> __*c*__. Keep a list of nodes with equal keys at $$x$$, and insert $$z$$ into the list.

If linked list is used, it could be $$\Theta(1)$$.

> __*d*__. Randomly set $$x$$ to either $$x.left$$ or $$x.right$$. (Give the worst-case performance and informally derive the expected running time.)

Worst: $$\Theta(n)$$.

Expected: $$\Theta(n \lg n)$$.

