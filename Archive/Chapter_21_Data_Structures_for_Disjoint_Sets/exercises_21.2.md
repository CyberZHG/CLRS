## 20.2 Linked-list representation of disjoint sets

### 21.2-1

> Write pseudocode for MAKE-SET, FIND-SET, and UNION using the linked-list representation and the weighted-union heuristic. Make sure to specify the attributes that you assume for set objects and list objects.

UNION: if > swap & size +=

### 21.2-2

> Show the data structure that results and the answers returned by the FIND-SET operations in the following program. Use the linked-list representation with the weighted-union heuristic.

> ```
1   for i = 1 to 16
2        MAKE-SET(x_{i})
3   for i = 1 to 15 by 2
4        UNION(x_{i}, x_{i+1})
5   for i = 1 to 13 by 4
6        UNION(x_{i}, x_{i+2})
7   UNION(x_{1}, x_{5})
8   UNION(x_{11}, x_{13})
9   UNION(x_{1}, x_{10})
10  FIND-SET(x_{2})
11  FIND-SET(x_{9})
```
All same set.

### 21.2-3

> Adapt the aggregate proof of Theorem 21.1 to obtain amortized time bounds of $$O(1)$$ for MAKE-SET and FIND-SET and $$O(\lg n)$$ for UNION using the linked-list representation and the weighted-union heuristic.

$$O(n\lg n) / n = O(\lg n)$$

### 21.2-4

> Give a tight asymptotic bound on the running time of the sequence of operations in Figure 21.3 assuming the linked-list representation and the weighted-union heuristic.

$$\Theta(n) + \Theta(n) = \Theta(n)$$

### 21.2-5

> Professor Gompers suspects that it might be possible to keep just one pointer in each set object, rather than two (head and tail), while keeping the number of pointers in each list element at two. Show that the professor's suspicion is well founded by describing how to represent each set by a linked list such that each operation has the same running time as the operations described in this section. Describe also how the operations work. Your scheme should allow for the weighted-union heuristic, with the same effect as described in this section. (Hint: Use the tail of a linked list as its set's representative.)

If each node has a pointer points to the first node and we use the tail as the representative, then we can find the head (first node) with the tail's pointer in $$\Theta(1)$$.

### 21.2-6 

> Suggest a simple change to the UNION procedure for the linked-list representation that removes the need to keep the tail pointer to the last object in each list. Whether or not the weighted-union heuristic is used, your change should not change the asymptotic running time of the UNION procedure. (Hint: Rather than appending one list to another, splice them together.)

We can splice/zip two lists. Suppose one list is $$1 \rightarrow 3 \rightarrow 5 \rightarrow \dots \rightarrow 101$$, the other is $$2 \rightarrow 4 \rightarrow 6$$, then the spliced/zipped list is $$1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 7 \rightarrow \dots \rightarrow 101$$. When the shorter one is used up, we can concatenate the remaining part of the longer list directly to the tail of merged list, thus it is identical to the weighted-union heuristic.
