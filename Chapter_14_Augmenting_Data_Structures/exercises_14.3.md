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