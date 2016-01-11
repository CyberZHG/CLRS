## 15.1 Rod cutting

### 15.1-1

> Show that equation (15.4) follows from equation (15.3) and the initial condition $$T(0) = 1$$.

For $$n=0$$, $$T(0) = 2^0 = 1$$.

Suppose $$T(i) = 2^i$$ for $$i$$ in $$[0, n - 1]$$, then
$$
T(n) = 1 + \sum_{j=0}^{n-1} T(j) = 1 + 1 + 2 + 2^2 + \cdots + 2^{n-1} = 2^n - 1 + 1 = 2^n
$$

