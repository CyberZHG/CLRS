## 15.5 Optimal binary search trees

### 15.5-1

> Write pseudocode for the procedure CONSTRUCT-OPTIMAL-BST$(root)$ which, given the table root, outputs the structure of an optimal binary search tree. For the example in Figure 15.10, your procedure should print out the structure corresponding to the optimal binary search tree shown in Figure 15.9(b).

```
CONSTRUCT-OPTIMAL-BST(root, i, j, last=0)
 1 if i L j
 2     return
 3 if last == 0
 4     print root[i, j] + "is the root"
 5 elseif j < last:
 6     print root[i, j] + "is the left child of" + last
 7 else
 8     print root[i, j] + "is the right child of" + last
 9 CONSTRUCT-OPTIMAL-BST(root, i, root[i, j] - 1, root[i, j])
10 CONSTRUCT-OPTIMAL-BST(root, root[i, j] + 1, j, root[i, j])
```

### 15.5-2

> Determine the cost and structure of an optimal binary search tree for a set of $n = 7$ keys with the following probabilities

$k_4$ is the root
$k_2$ is the left child of $k_4$
$k_1$ is the left child of $k_2$
$d_0$ is the right child of $k_1$
$d_1$ is the right child of $k_1$
$k_3$ is the right child of $k_2$
$d_2$ is the left child of $k_3$
$d_3$ is the right child of $k_3$
$k_5$ is the right child of $k_4$
$d_4$ is the left child of $k_5$
$d_5$ is the right child of $k_5$

### 15.5-3

> Suppose that instead of maintaining the table $w[i, j]$, we computed the value of $w(i, j)$ directly from equation (15.12) in line 9 of OPTIMAL-BST and used this computed value in line 11. How would this change affect the asymptotic running time of OPTIMAL-BST?

$O(n^3)$

### 15.5-4 $\star$

> Knuth [212] has shown that there are always roots of optimal subtrees such that $root[i, j - 1] \le root[i, j] \le root[i + 1, j]$ for all $1 \le i < j \le n$. Use this fact to modify the OPTIMAL-BST procedure to run in $O(n^2)$ time.

```
 10 for r = root[i, j-1] to root[i + 1, j]
```
