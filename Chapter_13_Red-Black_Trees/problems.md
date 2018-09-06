## Problems

### 13-1 Persistent dynamic sets

> During the course of an algorithm, we sometimes find that we need to maintain past versions of a dynamic set as it is updated. We call such a set __*persistent*__. One way to implement a persistent set is to copy the entire set whenever it is modified, but this approach can slow down a program and also consume much space. Sometimes, we can do much better.

> __*a*__. For a general persistent binary search tree, identify the nodes that we need to change to insert a key $k$ or delete a node $y$.

Insert: the number of nodes in the simple path plus 1.

Delete: the ancestors of $y$.

> __*b*__. Write a procedure PERSISTENT-TREE-INSERT that, given a persistent tree $T$ and a key $k$ to insert, returns a new persistent tree $T'$ that is the result of inserting $k$ into $T$.

```python
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def insert(root, x):
    if root is None:
        return TreeNode(x)
    new_root = TreeNode(root.key)
    if root.key <= x:
        new_root.left = root.left
        new_root.right = insert(root.right, x)
    else:
        new_root.left = insert(root.left, x)
        new_root.right = root.right
    return new_root
```

> __*c*__. If the height of the persistent binary search tree $T$ is $h$, what are the time and space requirements of your implementation of PERSISTENT-TREE-INSERT?

$\Theta(h)$ and $\Theta(h)$.

> __*d*__. Suppose that we had included the parent attribute in each node. In this case, PERSISTENT-TREE-INSERT would need to perform additional copying. Prove that PERSISTENT-TREE-INSERT would then require $\Omega(n)$ time and space, where $n$ is the number of nodes in the tree.

$T(n)=2T(n/2)+\Theta(1)$

> __*e*__. Show how to use red-black trees to guarantee that the worst-case running time and space are $O(\lg n)$ per insertion or deletion.

Based on Exercise 13.3-6.

### 13-2 Join operation on red-black trees

> The __*join*__ operation takes two dynamic sets $S\_1$ and $S\_2$ and an element $x$ such that for any $x\_1 \in S\_1$ and $x\_2 \in S\_2$, we have $x\_1.key \le x.key \le x\_2.key$. It returns a set $S = S\_1 \cup \\{x\\} \cup S\_2$. In this problem, we investigate how to implement the join operation on red-black trees.

> __*a*__. Given a red-black tree $T$, let us store its black-height as the new attribute $T.bh$. Argue that RB-INSERT and RB-DELETE can maintain the $bh$ attribute without requiring extra storage in the nodes of the tree and without increasing the asymptotic running times. Show that while descending through $T$, we can determine the black-height of each node we visit in $O(1)$ time per node visited.

Initialize: $bh = 0$.

RB-INSERT: if in the last step the root is red, we increase $bh$ by 1.

RB-DELETE: if $x$ is root, we decrease $bh$ by 1.

Each node: in the simple path, decrease $bh$ by 1 each time we find a black node.

> We wish to implement the operation RB-JOIN$(T\_1, x, T\_2)$, which destroys $T\_1$ and $T\_2$ and returns a red-black tree $T=T\_1 \cup \\{x\\} \cup T\_2$. Let $n$ be the total number of nodes in $T\_1$ and $T\_2$.

> __*b*__. Assume that $T\_1.bh \ge T\_2.bh$. Describe an $O(\lg n)$-time algorithm that finds a black node $y$ in $T\_1$ with the largest key from among those nodes whose black-height is $T2.bh$.

Move to the right child if the node has a right child, otherwise move to the left child. If the node is black, we decease $bh$ by 1. Repeat the step until $bh = T2.bh$.

> __*c*__. Let $T\_y$ be the subtree rooted at $y$. Describe how $T\_y \cup \\{ x \\} \cup T\_2$ can replace $T\_y$ in $O(1)$ time without destroying the binary-search-tree property.

$x$'s parent is $T\_y$'s parent, $x$'s left child is $T\_y$ and its right child is $T\_2$.

> __*d*__. What color should we make $x$ so that red-black properties 1, 3, and 5 are maintained? Describe how to enforce properties 2 and 4 in $O(\lg n)$ time.

Red. RB-INSERT-FIXUP(T, x).

> __*e*__. Argue that no generality is lost by making the assumption in part (b). Describe the symmetric situation that arises when $T\_1.bh \le T\_2.bh$.

Symmetric.

> __*f*__. Argue that the running time of RB-JOIN is $O(\lg n)$.

$O(1) + O(\lg n) = O(\lg n)$

### 13-3 AVL trees

> An __*AVL tree*__ is a binary search tree that is __*height balanced*__: for each node $x$, the heights of the left and right subtrees of $x$ differ by at most 1. To implement an AVL tree, we maintain an extra attribute in each node: $x.h$ is the height of node $x$. As for any other binary search tree $T$, we assume that $T.root$ points to the root node.

> __*a*__. Prove that an AVL tree with $n$ nodes has height $O(\lg n)$.

$T(h) = T(h-1) + T(h-2)$.

> __*b*__. To insert into an AVL tree, we first place a node into the appropriate place in binary search tree order. Afterward, the tree might no longer be height balanced. Specifically, the heights of the left and right children of some node might differ by 2. Describe a procedure BALANCE$(x)$, which takes a subtree rooted at $x$ whose left and right children are height balanced and have heights that differ by at most 2, i.e., $|x.right.h - x.left.hj|\le 2$, and alters the subtree rooted at $x$ to be height balanced.

See __*c*__.

> __*c*__. Using part (b), describe a recursive procedure AVL-INSERT$(x, z)$ that takes a node $x$ within an AVL tree and a newly created node $z$ (whose key has already been filled in), and adds $z$ to the subtree rooted at $x$, maintaining the property that $x$ is the root of an AVL tree. As in TREE-INSERT from Section 12.3, assume that $z.key$ has already been filled in and that $z.left = NIL$ and $z.right = NIL$; also assume that $z.h = 0$. Thus, to insert the node $z$ into the AVL tree $T$, we call AVL-INSERT$(T.root, z)$.


```python
class AVLTreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.h = 0
        self.p = None
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.p = self
        if self.right is not None:
            self.right.p = self


class AVL:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def get_height(self, node):
        if node is None:
            return -1
        return node.h

    def update_height(self, node):
        if node is None:
            return
        node.h = max(self.get_height(node.left), self.get_height(node.right))+1

    def balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def avl_insert(self, x):
        self.root = self.avl_insert_rec(self.root, x)

    def avl_insert_rec(self, root, x):
        if root is None:
            return AVLTreeNode(x)
        if root.key > x:
            root.left = self.avl_insert_rec(root.left, x)
            root.left.p = root
        else:
            root.right = self.avl_insert_rec(root.right, x)
            root.right.p = root
        if self.balance_factor(root) == 2:
            if self.balance_factor(root.left) == -1:
                self.left_rotate(root.left)
            self.right_rotate(root)
            root = root.p
            self.update_height(root.left)
            self.update_height(root.right)
            self.update_height(root)
        elif self.balance_factor(root) == -2:
            if self.balance_factor(root.right) == 1:
                self.right_rotate(root.right)
            self.left_rotate(root)
            root = root.p
            self.update_height(root.left)
            self.update_height(root.right)
            self.update_height(root)
        else:
            self.update_height(root)
        return root
```

> __*d*__. Show that AVL-INSERT, run on an n-node AVL tree, takes $O(\lg n)$ time and performs $O(1)$ rotations.

$O(\lg n)$: the length of path from root to the inserted node.

$O(1)$: the height will decrease by 1 after the rotation, therefore the ancestors will not be affected.

### 13-4 Treaps

> If we insert a set of $n$ items into a binary search tree, the resulting tree may be horribly unbalanced, leading to long search times. As we saw in Section 12.4, however, randomly built binary search trees tend to be balanced. Therefore, one strategy that, on average, builds a balanced tree for a fixed set of items would be to randomly permute the items and then insert them in that order into the tree.

> __*a*__. Show that given a set of nodes $x\_1, x\_2, \dots, x\_n$, with associated keys and priorities, all distinct, the treap associated with these nodes is unique.

The root is the node with smallest priority, the root divides the sets into two subsets based on the key. In each subset, the node with smallest priority is selected as the root, thus we can uniquely determine a treap with a specific input.

> __*b*__. Show that the expected height of a treap is $\Theta(\lg n)$, and hence the expected time to search for a value in the treap is $\Theta(\lg n)$.

Same as randomly built BST.

> __*c*__. Explain how TREAP-INSERT works. Explain the idea in English and give pseudocode.

```python
class TreapNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.priority = random.random()
        self.p = None
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.p = self
        if self.right is not None:
            self.right.p = self


class Treap:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def insert(self, x):
        self.root = self.insert_rec(self.root, x)

    def insert_rec(self, root, x):
        if root is None:
            return TreapNode(x)
        if root.key > x:
            root.left = self.insert_rec(root.left, x)
            root.left.p = root
            if root.left.priority < root.priority:
                self.right_rotate(root)
                root = root.p
        else:
            root.right = self.insert_rec(root.right, x)
            root.right.p = root
            if root.right.priority < root.priority:
                self.left_rotate(root)
                root = root.p
        return root
```

> __*d*__. Show that the expected running time of TREAP-INSERT is $\Theta(\lg n)$.

Rotation is $\Theta(1)$, at most $h$ rotations, therefore the expected running time is $\Theta(\lg n)$.

> __*e*__. Consider the treap $T$ immediately after TREAP-INSERT has inserted node $x$. Let $C$ be the length of the right spine of the left subtree of $x$. Let $D$ be the length of the left spine of the right subtree of $x$. Prove that the total number of rotations that were performed during the insertion of $x$ is equal to $C + D$.

Left rotation increase $C$ by 1, right rotation increase $D$ by 1.

> __*f*__. Show that $X\_{ik} = 1$ if and only if $y.priority > x.priority$, $y.key < x.key$, and, for every $z$ such that $y.key < z.key < x.key$, we have $y.priority < z.priority$.

The first two are obvious.

The min-heap property will not hold if $y.priority > z.priority$.

> __*g*__. Show that

> $\begin{array}{rll}
\text{Pr}\\{X\_{ik}=1\\} &=&
\displaystyle \frac{(k-i-1)!}{(k-i+1)!} \\\\
&=& \displaystyle \frac{1}{(k-i+1)(k-i)} \\\\
\end{array}
$$

Total number of permutations: $(k-i+1)!$

Permutations satisfy the condition: $(k-i-1)!$

> \_\_\*h\*\_\_. Show that

> $\begin{array}{rll}
\text{E}[C] &=&
\displaystyle \sum_{j=1}^{k-1} \frac{1}{j(j+1)} \\
&=& \displaystyle 1 - \frac{1}{k} \\
\end{array}
$$

$$
\begin{array}{rll}
\text{E}[C] 
&=& \displaystyle \sum_{j=1}^{k-1} \frac{1}{(k-i+1)(k-i)} \\
&=& \displaystyle \sum_{j=1}^{k-1} \left ( \frac{1}{k-i} - \frac{1}{k-i+1} \right ) \\
&=& \displaystyle 1 - \frac{1}{k} 
\end{array}
$$

> \_\_\*i\*\_\_. Use a symmetry argument to show that

> $\displaystyle \text{E}[D] = 1 - \frac{1}{n-k+1}$

$$
\begin{array}{rll}
\text{E}[D] 
&=& \displaystyle \sum_{j=1}^{n-k} \frac{1}{(k-i+1)(k-i)} \\
&=& \displaystyle 1 - \frac{1}{n-k+1}
\end{array}
$$

> \_\_\*j\*\_\_. Conclude that the expected number of rotations performed when inserting a node into a treap is less than 2.

$\text{E}[C] + \text{E}[D] \le 2$
