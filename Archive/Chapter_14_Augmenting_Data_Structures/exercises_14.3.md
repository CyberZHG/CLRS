## 14.3 Interval trees

### 14.3-1

> Write pseudocode for LEFT-ROTATE that operates on nodes in an interval tree and updates the $$max$$ attributes in $$O(1)$$ time.

$$y.max = x.max$$

$$x.max = \max(x.int.high, x.left.max, x.right.max)$$

### 14.3-2

> Rewrite the code for INTERVAL-SEARCH so that it works properly when all intervals are open.

```
INTERVAL-SEARCH(T, i)
1 x = T.root
2 while x != T.nil and (i.high <= x.int.left or x.int.right <= i.low)
3     if x.left != T.nil and x.left.max > i.low
4         x = x.left
5     else x = x.right
6 return x
```

### 14.3-3

> Describe an efficient algorithm that, given an interval $$i$$ , returns an interval overlapping $$i$$ that has the minimum low endpoint, or $$T.nil$$ if no such interval exists.

```
MIN-INTERVAL-SEARCH(T, i)
 1 x = T.root
 2 ret = T.nil
 3 while x != T.nil:
 4     if not (i.high <= x.int.left or x.int.right <= i.low)
 5         if ret == T.nil or ret.right > x.int.right
 6             ret = x
 7     if x.left != T.nil and x.left.max > i.low
 8         x = x.left
 9     else x = x.right
10 return ret
```

### 14.3-4

> Given an interval tree $$T$$ and an interval $$i$$, describe how to list all intervals in $$T$$ that overlap $$i$$ in $$O(\min(n, k \lg n))$$ time, where $$k$$ is the number of intervals in the output list.

```
INTERVALS-SEARCH(T, x, i)
 1 lst = []
 2 if i overlaps x.int
 3     lst.append(x)
 4 if x.left != T.nil and x.left.max > i.low
 5     lst += INTERVALS-SEARCH(T, x.left, i)
 6 if x.right != T.nil and x.int.low <= i.high and x.right.max >= i.low
 7     lst += INTERVALS-SEARCH(T, x.right, i)
 8 return lst
```

### 14.3-5

> Suggest modifications to the interval-tree procedures to support the new operation INTERVAL-SEARCH-EXACTLY$$(T, i)$$, where $$T$$ is an interval tree and $$i$$ is an interval. The operation should return a pointer to a node $$x$$ in $$T$$ such that $$x.int.low = i.low$$ and $$x.int.high = i.high$$, or $$T.nil$$ if $$T$$ contains no such node. All operations, including INTERVAL-SEARCH-EXACTLY, should run in $$O(\lg n)$$ time on an $$n$$-node interval tree.

Search for nodes which has exactly the same low value.

### 14.3-6

> Show how to maintain a dynamic set $$Q$$ of numbers that supports the operation MIN-GAP, which gives the magnitude of the difference of the two closest numbers in $$Q$$. For example, if $$Q = \{1, 5, 9, 15, 18, 22\}$$, then MIN-GAP$$(Q)$$ returns $$18 - 15 = 3$$, since $$15$$ and $$18$$ are the two closest numbers in $$Q$$. Make the operations INSERT, DELETE, SEARCH, and MIN-GAP as efficient as possible, and analyze their running times.

Based on Exercise 14.2-1, we can maintain SUCCESSOR in $$O(1)$$ time, each time after updating the SUCCESSOR, we can update $$x.gap$$ to $$x.successor.key - x.key$$. And based on Exercise 14.2-1 we can also maintain the minimum $$gap$$ of the subtree in $$O(1)$$ time.

### 14.3-7 $$\star$$

> VLSI databases commonly represent an integrated circuit as a list of rectangles. Assume that each rectangle is rectilinearly oriented (sides parallel to the $$x$$- and $$y$$-axes), so that we represent a rectangle by its minimum and maximum $$x$$ and $$y$$-coordinates. Give an $$O(n \lg n)$$-time algorithm to decide whether or not a set of $$n$$ rectangles so represented contains two rectangles that overlap. Your algorithm need not report all intersecting pairs, but it must report that an overlap exists if one rectangle entirely covers another, even if the boundary lines do not intersect.

Suppose we represent a rectangle by $$(x_{min}, x_{max}, y_{min}, y_{max})$$.

Sort the $$x_{min}$$s and $$x_{max}$$s in ascending order. From left to right, if we meet a $$x_{min}$$, before we add $$(y_{min}, y_{max})$$ to the interval tree, if the interval $$(y_{min}, y_{max})$$ is overlapped with some node in the interval tree, then there is an overlap of rectangles. And when we meet a $$x_{max}$$, we remove $$(y_{min}, y_{max})$$ from the interval tree.
