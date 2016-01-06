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

