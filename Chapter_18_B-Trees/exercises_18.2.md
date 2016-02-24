## 18.2 Basic operations on B-trees

### 18.2-1

> Show the results of inserting the keys 

> $$F, S, Q, K, C, L, H, T, V, W, M, R, N, P, A, B, X, Y, D, Z, E$$

> in order into an empty B-tree with minimum degree 2. Draw only the configurations of the tree just before some node must split, and also draw the final configuration.

![](./img/18.2-1_1.png)

![](./img/18.2-1_2.png)

![](./img/18.2-1_3.png)

![](./img/18.2-1_4.png)

![](./img/18.2-1_5.png)

![](./img/18.2-1_6.png)

![](./img/18.2-1_7.png)

![](./img/18.2-1_8.png)

![](./img/18.2-1_9.png)

![](./img/18.2-1_10.png)

![](./img/18.2-1_11.png)

![](./img/18.2-1_12.png)

![](./img/18.2-1_13.png)

![](./img/18.2-1_14.png)

![](./img/18.2-1_15.png)

![](./img/18.2-1_16.png)

![](./img/18.2-1_17.png)

![](./img/18.2-1_18.png)

![](./img/18.2-1_19.png)

![](./img/18.2-1_20.png)

![](./img/18.2-1_21.png)

### 18.2-2

> Explain under what circumstances, if any, redundant DISK-READ or DISK-WRITE operations occur during the course of executing a call to B-TREE-INSERT. (A redundant DISK-READ is a DISK-READ for a page that is already in memory. A redundant DISK-WRITE writes to disk a page of information that is identical to what is already stored there.)

No redundant.

### 18.2-3

> Explain how to find the minimum key stored in a B-tree and how to find the predecessor of a given key stored in a B-tree.



