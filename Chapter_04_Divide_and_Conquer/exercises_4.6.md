## 4.6 Proof of the master theorem

### 4.6-1 $\star$

> Give a simple and exact expression for $n_j$ in equation (4.27) for the case in which b is a positive integer instead of an arbitrary real number.

$$
n_j=\left \lceil \frac{n}{b^j} \right \rceil
$$

### 4.6-2 $\star$

> Show that if $f(n)=\Theta(n^{\log_ba}\lg^kn)$, where $k \ge 0$, then the master recurrence has solution $T(n)=\Theta(n^{\log_ba}\lg^{k+1}n)$. For simplicity, confine your analysis to extract powers of $b$.

$$
\dots
$$

### 4.6-3 $\star$

> Show that case 3 of the master theorem is overstated, in the sense that the regularity condition $af(n/b) \le cf(n)$ for some constant $c < 1$ implies that there exists a constant $\epsilon > 0$ such that $f(n)=\Omega(n^{\log_ba+\epsilon})$.

$$
\dots
$$
