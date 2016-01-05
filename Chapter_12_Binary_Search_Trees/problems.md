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

### 12-2 Radix trees

> Given two strings $$a = a_0a_1 \dots a_p$$ and $$b = b_0b_1 \dots b_q$$, where each $$a_i$$ and each $$b_j$$ is in some ordered set of characters, we say that string $$a$$ is lexicographically less
than string $$b$$ if either
1. there exists an integer $$j$$, where $$0 \le j \le \min(p, q)$$, such that $$a_i = b_i$$ for all $$i = 0, 1, \dots j - 1$$ and $$a_j < b_j$$, or
2. $$p < q$$ and $$a_i = b_i$$ for all $$i = 0, 1, \dots, p$$.

> The radix tree data structure shown in Figure 12.5 stores the bit strings 1011, 10, 011, 100, and 0. When searching for a key $$a = a_0a_1 \dots a_p$$, we go left at a node of depth $$i$$ if $$a_i = 0$$ and right if $$a_i = 1$$. Let $$S$$ be a set of distinct bit strings whose lengths sum to $$n$$. Show how to use a radix tree to sort $$S$$ lexicographically in $$\Theta(n)$$ time. For the example in Figure 12.5, the output of the sort should be the sequence 0, 011, 10, 100, 1011.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RadixTree:
    def __init__(self):
        self.root = None

    def insert(self, a):
        self.root = self.insert_rec(self.root, a, 0)

    def insert_rec(self, root, a, idx):
        if idx == len(a):
            if root is None:
                return TreeNode(a)
            root.val = a
            return root
        if root is None:
            root = TreeNode(None)
        if a[idx] == '0':
            root.left = self.insert_rec(root.left, a, idx+1)
        else:
            root.right = self.insert_rec(root.right, a, idx+1)
        return root

    def sorted(self):
        self.sorted_list = []
        self.sorted_rec(self.root)
        return self.sorted_list

    def sorted_rec(self, root):
        if root is None:
            return
        if root.val is not None:
            self.sorted_list.append(root.val)
        self.sorted_rec(root.left)
        self.sorted_rec(root.right)


def sort_strings(strs):
    radix_tree = RadixTree()
    for s in strs:
        radix_tree.insert(s)
    return radix_tree.sorted()
```


