## 14.1 Dynamic order statistics

### 14.1-1

> Show how OS-SELECT$$(T.root, 10)$$ operates on the red-black tree $$T$$ of Figure 14.1.

* 26: r = 13, i = 10, go left
* 17: r = 8, i = 10, go right
* 21: r = 3, i = 2, go left
* 19: r = 1, i = 2, go right
* 20: r = 1, i = 1, choose 20

### 14.1-2

> Show how OS-RANK$$(T, x)$$ operates on the red-black tree $$T$$ of Figure 14.1 and the node $$x$$ with $$x.key = 35$$.

* 35: r = 1
* 38: r = 1
* 30: r = r + 2 = 3
* 41: r = 3
* 26: r = r + 13 = 16

### 14.1-3

> Write a nonrecursive version of OS-SELECT.

```python
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.size = 1
        self.left = left
        self.right = right
        if left is not None:
            self.size += left.size
        if right is not None:
            self.size += right.size


def os_select(x, i):
    while True:
        if x.left is None:
            r = 1
        else:
            r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            x = x.left
        else:
            x = x.right
            i -= r
```

### 14.1-4

> Write a recursive procedure OS-KEY-RANK$$(T, k)$$ that takes as input an order-statistic tree $$T$$ and a key $$k$$ and returns the rank of $$k$$ in the dynamic set represented by $$T$$. Assume that the keys of $$T$$ are distinct.

```python
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.size = 1
        self.left = left
        self.right = right
        if left is not None:
            self.size += left.size
        if right is not None:
            self.size += right.size


def os_key_rank(x, k, i=0):
    r = 1
    if x.left is not None:
        r += x.left.size
    if k == x.key:
        return i + r
    if k < x.key:
        return os_key_rank(x.left, k, i)
    if k > x.key:
        return os_key_rank(x.right, k, i + r)
```

### 14.1-5

> Given an element $$x$$ in an $$n$$-node order-statistic tree and a natural number $$i$$, how can we determine the $$i$$th successor of $$x$$ in the linear order of the tree in $$O(\lg n)$$ time?

OS-SELECT(T, OS-RANK(T, x) + i)

### 14.1-6

> Observe that whenever we reference the size attribute of a node in either OS-SELECT or OS-RANK, we use it only to compute a rank. Accordingly, suppose
we store in each node its rank in the subtree of which it is the root. Show how to maintain this information during insertion and deletion. (Remember that these two operations can cause rotations.)

Tree walk and change the rank by comparing the key of the node with that of the inserted node. $$O(n)$$

### 14.1-7

> Show how to use an order-statistic tree to count the number of inversions (see Problem 2-4) in an array of size $$n$$ in time $$O(n \lg n)$$.

After the insertion of a node, the number of tree nodes subtract the rank of the inserted node is the number of inversions of the current node.

### 14.1-8 $$\star$$

> Consider $$n$$ chords on a circle, each defined by its endpoints. Describe an $$O(n \lg n)$$- time algorithm to determine the number of pairs of chords that intersect inside the circle. (For example, if the $$n$$ chords are all diameters that meet at the center, then the correct answer is $$\binom{n}{2}$$. Assume that no two chords share an endpoint.

Sort the vertices in clock-wise order, and assign a unique value to each vertex. For each chord its two vertices are $$u_i$$, $$v_i$$ and $$u_i < v_i$$. Add the vertices one by one in clock-wise order, if we meet a $$u_i$$, we add it to the order-statistic tree, if we meet a $$v_i$$, we calculate how many nodes are larger than $$u_i$$ (which is the number of intersects with chord $$i$$), and remove $$u_i$$.
