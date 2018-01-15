## 20.1 Preliminary approaches

### 20.1-1

> Modify the data structures in this section to support duplicate keys.

Bit vector => integer vector.

### 20.1-2

> Modify the data structures in this section to support keys that have associated satellite data.

Satellite area.

### 20.1-3

> Observe that, using the structures in this section, the way we find the successor and predecessor of a value $$x$$ does not depend on whether $$x$$ is in the set at the time. Show how to find the successor of $$x$$ in a binary search tree when $$x$$ is not stored in the tree.

For each node, if $$x <= node.key$$, then $$node.key$$ is a candidate and descend to the node's left child; otherwise do nothing and descend to the node's right child. There are at most $$\lg n$$ candidates, the successor is the minimal candidate, and the method runs in $$\Theta(\lg n)$$.

### 20.1-4

> Suppose that instead of superimposing a tree of degree $$\sqrt{u}$$, we were to superimpose a tree of degree $$u^{1/k}$$, where $$k > 1$$ is a constant. What would be the height of such a tree, and how long would each of the operations take?

Height: $$k$$

How long: $$O(k\sqrt{u})$$

