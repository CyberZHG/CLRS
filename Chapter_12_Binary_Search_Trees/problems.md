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

Insert all the bit strings into radix tree costs $$\Theta(n)$$, then use preorder tree walk to sort the strings costs $$\Theta(n)$$, the total cost is still $$\Theta(n)$$.

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

### 12-3 Average node depth in a randomly built binary search tree

> In this problem, we prove that the average depth of a node in a randomly built binary search tree with n nodes is $$O(\lg n)$$. Although this result is weaker than that of Theorem 12.4, the technique we shall use reveals a surprising similarity between the building of a binary search tree and the execution of RANDOMIZED-QUICKSORT from Section 7.3.

> We define the __*total path length*__ $$P(T)$$ of a binary tree $$T$$ as the sum, over all nodes $$x$$ in $$T$$ , of the depth of node $$x$$, which we denote by $$d(x, T)$$.

> __*a*__. Argue that the average depth of a node in $$T$$ is

> $$\displaystyle \frac{1}{n} \sum_{x \in T} d(x, T) = \frac{1}{n} P(T)$$.

Obviously.

> Thus, we wish to show that the expected value of $$P(T)$$ is $$O(n \lg n)$$.

> __*b*__. Let $$T_L$$ and $$T_R$$ denote the left and right subtrees of tree $$T$$, respectively. Argue that if $$T$$ has $$n$$ nodes, then

> $$P(T) = P(T_L) + P(T_R) + n - 1$$.

There are $$n-1$$ nodes in $$P(T_L)$$ and $$P(T_R)$$, each increase by 1.

> __*c*__. Let $$P(n)$$ denote the average total path length of a randomly built binary search tree with n nodes. Show that

> $$\displaystyle P(n) = \frac{1}{n} \sum_{i=0}^{n-1} (P(i) + P(n-i-1) + n - 1)$$.

The root is equally likely to be the rank in $$[1, n]$$.

> __*d*__. Show how to rewrite $$P(n)$$ as

> $$\displaystyle P(n) = \frac{2}{n} \sum_{k=1}^{n-1} P(k) + \Theta(n)$$.

Each item $$P(1), P(2), \dots, P(n)$$ appears twice in the summation, and

$$
\frac{1}{n} \sum_{i=0}^{n-1} n - 1 = \frac{(n-3)n}{2n} = \Theta(n)
$$

> __*e*__. Recalling the alternative analysis of the randomized version of quicksort given in Problem 7-3, conclude that $$P(n) = O(n \lg n)$$.

Based on Problem 7-3,  $$P(n) = O(n \lg n)$$.

> __*f*__. Describe an implementation of quicksort in which the comparisons to sort a set of elements are exactly the same as the comparisons to insert the elements into a binary search tree.

Choose the pivot that it has the lowest index in the original list.
