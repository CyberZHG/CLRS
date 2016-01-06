## Problems

### 13-1 Persistent dynamic sets

> During the course of an algorithm, we sometimes find that we need to maintain past versions of a dynamic set as it is updated. We call such a set __*persistent*__. One way to implement a persistent set is to copy the entire set whenever it is modified, but this approach can slow down a program and also consume much space. Sometimes, we can do much better.

> __*a*__. For a general persistent binary search tree, identify the nodes that we need to change to insert a key $$k$$ or delete a node $$y$$.

Insert: the number of nodes in the simple path plus 1.

Delete: the ancestors of $$y$$.

> __*b*__. Write a procedure PERSISTENT-TREE-INSERT that, given a persistent tree $$T$$ and a key $$k$$ to insert, returns a new persistent tree $$T'$$ that is the result of inserting $$k$$ into $$T$$.

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

> __*c*__. If the height of the persistent binary search tree $$T$$ is $$h$$, what are the time and space requirements of your implementation of PERSISTENT-TREE-INSERT?

$$\Theta(h)$$ and $$\Theta(h)$$.

> __*d*__. Suppose that we had included the parent attribute in each node. In this case, PERSISTENT-TREE-INSERT would need to perform additional copying. Prove that PERSISTENT-TREE-INSERT would then require $$\Omega(n)$$ time and space, where $$n$$ is the number of nodes in the tree.

$$T(n)=2T(n/2)+\Theta(1)$$

> __*e*__. Show how to use red-black trees to guarantee that the worst-case running time and space are $$O(\lg n)$$ per insertion or deletion.

Based on Exercise 13.3-6.

### 13-2 Join operation on red-black trees

> The __*join*__ operation takes two dynamic sets $$S_1$$ and $$S_2$$ and an element $$x$$ such that for any $$x_1 \in S_1$$ and $$x_2 \in S_2$$, we have $$x_1.key \le x.key \le x_2.key$$. It returns a set $$S = S_1 \cup \{x\} \cup S_2$$. In this problem, we investigate how to implement the join operation on red-black trees.

> __*a*__. Given a red-black tree $$T$$, let us store its black-height as the new attribute $$T.bh$$. Argue that RB-INSERT and RB-DELETE can maintain the $$bh$$ attribute without requiring extra storage in the nodes of the tree and without increasing the asymptotic running times. Show that while descending through $$T$$, we can determine the black-height of each node we visit in $$O(1)$$ time per node visited.

Initialize: $$bh = 0$$.

RB-INSERT: if in the last step the root is red, we increase $$bh$$ by 1.

RB-DELETE: if $$x$$ is root, we decrease $$bh$$ by 1.

Each node: in the simple path, decrease $$bh$$ by 1 each time we find a black node.

> We wish to implement the operation RB-JOIN$$(T_1, x, T_2)$$, which destroys $$T_1$$ and $$T_2$$ and returns a red-black tree $$T=T_1 \cup \{x\} \cup T_2$$. Let $$n$$ be the total number of nodes in $$T_1$$ and $$T_2$$.

> __*b*__. Assume that $$T_1.bh \ge T_2.bh$$. Describe an $$O(\lg n)$$-time algorithm that finds a black node $$y$$ in $$T_1$$ with the largest key from among those nodes whose black-height is $$T2.bh$$.

Move to the right child if the node has a right child, otherwise move to the left child. If the node is black, we decease $$bh$$ by 1. Repeat the step until $$bh = T2.bh$$.

> __*c*__. Let $$T_y$$ be the subtree rooted at $$y$$. Describe how $$T_y \cup \{ x \} \cup T_2$$ can replace $$T_y$$ in $$O(1)$$ time without destroying the binary-search-tree property.

$$x$$'s parent is $$T_y$$'s parent, $$x$$'s left child is $$T_y$$ and its right child is $$T_2$$.

> __*d*__. What color should we make $$x$$ so that red-black properties 1, 3, and 5 are maintained? Describe how to enforce properties 2 and 4 in $$O(\lg n)$$ time.

Red. RB-INSERT-FIXUP(T, x).

> __*e*__. Argue that no generality is lost by making the assumption in part (b). Describe the symmetric situation that arises when $$T1.bh \le T2.bh$$.

Symmetric.

> __*f*__. Argue that the running time of RB-JOIN is $$O(\lg n)$$.

$$O(1) + O(\lg n) = O(\lg n)$$

