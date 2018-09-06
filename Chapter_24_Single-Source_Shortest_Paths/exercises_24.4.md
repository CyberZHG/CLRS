## 24.4 Difference constraints and shortest paths

### 24.4-1

> Find a feasible solution or determine that no feasible solution exists for the following system of difference constraints:

### 24.4-2

> Find a feasible solution or determine that no feasible solution exists for the following system of difference constraints:

No solution.

### 24.4-3

> Can any shortest-path weight from the new vertex $v\_0$ in a constraint graph be positive? Explain.

### 24.4-4

> Express the single-pair shortest-path problem as a linear program.

### 24.4-5

> Show how to modify the Bellman-Ford algorithm slightly so that when we use it to solve a system of difference constraints with m inequalities on n unknowns, the running time is $O(nm)$.

### 24.4-6

> Suppose that in addition to a system of difference constraints, we want to handle __equality constraints__ of the form $x\_i = x\_j + b\_k$. Show how to adapt the Bellman-Ford algorithm to solve this variety of constraint system.

### 24.4-7

> Show how to solve a system of difference constraints by a Bellman-Ford-like algorithm that runs on a constraint graph without the extra vertex $v\_0$.

### 24.4-8 $\star$

> Let $Ax \le b$ be a system of $m$ difference constraints in $n$ unknowns. Show that the Bellman-Ford algorithm, when run on the corresponding constraint graph, maximizes $\sum\_{i=1}^n x\_i$ subject to $Ax \le b$ and $x\_i \le 0$ for all $x\_i$.

### 24.4-9 $\star$

> Show that the Bellman-Ford algorithm, when run on the constraint graph for a system $Ax \le b$ of difference constraints, minimizes the quantity $(\max\\{x\_i\\} - \min\\{x\_i\\})$ subject to $Ax \le b$. Explain how this fact might come in handy if the algorithm is used to schedule construction jobs.

### 24.4-10

> Suppose that every row in the matrix $A$ of a linear program $Ax \le b$ corresponds to a difference constraint, a single-variable constraint of the form $x\_i \le b\_k$, or a singlevariable constraint of the form $-x\_i \le b\_k$. Show how to adapt the Bellman-Ford algorithm to solve this variety of constraint system.

### 24.4-11

> Give an efficient algorithm to solve a system $Ax \le b$ of difference constraints when all of the elements of b are real-valued and all of the unknowns $x\_i$ must be integers.

### 24.4-12 $\star$

> Give an efficient algorithm to solve a system $Ax \le b$ of difference constraints when all of the elements of b are real-valued and a specified subset of some, but not necessarily all, of the unknowns $x\_i$ must be integers.
