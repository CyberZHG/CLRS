## 8.2 Counting sort

### 8.2-1

> Using Figure 8.2 as a model, illustrate the operation of COUNTING-SORT on the array $A = \left \langle6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2\right \rangle$.

![](/img/8.2-1_1.png)

![](/img/8.2-1_2.png)

![](/img/8.2-1_3.png)

![](/img/8.2-1_4.png)

![](/img/8.2-1_5.png)

![](/img/8.2-1_6.png)

![](/img/8.2-1_7.png)

![](/img/8.2-1_8.png)

![](/img/8.2-1_9.png)

![](/img/8.2-1_10.png)

![](/img/8.2-1_11.png)

![](/img/8.2-1_12.png)

![](/img/8.2-1_13.png)

![](/img/8.2-1_14.png)

![](/img/8.2-1_15.png)

### 8.2-2

> Prove that COUNTING-SORT is stable.

Value with larger index choose the largest index first.

### 8.2-3

> Suppose that we were to rewrite the for loop header in line 10 of the COUNTING-SORT as
```
10 for j = 1 to A.length
```
Show that the algorithm still works properly. Is the modified algorithm stable?

works properly but not stable.

### 8.2-4

> Describe an algorithm that, given n integers in the range $0$ to $k$, preprocesses its input and then answers any query about how many of the $n$ integers fall into a range $[a \dots b]$ in $O(1)$ time. Your algorithm should use $\Theta(n + k)$ preprocessing time.

Use `C` in the counting sort, the number of integers fall into a range $[a \dots b]$ is $C[b] - C[a-1]$.

```python
class CountInterval:
    def __init__(self, a):
        k = max(a)
        self.c = [0 for _ in range(k + 1)]
        for v in a:
            self.c[v] += 1
        for i in range(1, k + 1):
            self.c[i] += self.c[i - 1]

    def count(self, a, b):
        if a == 0:
            return self.c[b]
        return self.c[b] - self.c[a - 1]
```
