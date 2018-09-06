## Problems

### 16-1 Coin changing

> Consider the problem of making change for $n$ cents using the fewest number of coins. Assume that each coin's value is an integer.

> __*a*__. Describe a greedy algorithm to make change consisting of quarters, dimes, nickels, and pennies. Prove that your algorithm yields an optimal solution.

Use the coin as large as possible.

> __*b*__. Suppose that the available coins are in the denominations that are powers of $c$, i.e., the denominations are $c^0, c^1, \dots, c^k$ for some integers $c > 1$ and $k \ge 1$. Show that the greedy algorithm always yields an optimal solution.

Same.

> __*c*__. Give a set of coin denominations for which the greedy algorithm does not yield an optimal solution. Your set should include a penny so that there is a solution for every value of $n$.

$\langle 10, 9, 1 \rangle$

For 18, the greedy algorithm yields 9 coins, the optimal solution is $\langle 9,9 \rangle$, which contains 2 coins.

> __*d*__. Give an $O(nk)$-time algorithm that makes change for any set of $k$ different coin denominations, assuming that one of the coins is a penny.

Let $dp[i]$ be the minimal number of coins of amount $i$, $dp[i] = 1 + \min\_j dp[i - c\_j]$.

### 16-2 Scheduling to minimize average completion time

> Suppose you are given a set $S = \\{a\_1, a\_2, \dots, a\_n\\}$ of tasks, where task $a\_i$ requires $p\_i$ units of processing time to complete, once it has started. You have one computer on which to run these tasks, and the computer can run only one task at a time. Let $c\_i$ be the __*completion time*__ of task $a\_i$ , that is, the time at which task $a\_i$ completes processing. Your goal is to minimize the average completion time, that is, to minimize $(1/n) \sum\_{i=1}^n c\_i$. For example, suppose there are two tasks, $a\_1$ and $a\_2$, with $p\_1 = 3$ and $p\_2 = 5$, and consider the schedule in which $a\_2$ runs first, followed by $a\_1$. Then $c\_2 = 5$, $c\_1 = 8$, and the average completion time is $(5 + 8)/2 = 6.5$. If task $a\_1$ runs first, however, then $c\_1 = 3$, $c\_2 = 8$, and the average completion time is $(3 + 8)/2 = 5.5$.

> __*a*__. Give an algorithm that schedules the tasks so as to minimize the average completion time. Each task must run non-preemptively, that is, once task $a\_i$ starts, it must run continuously for $p\_i$ units of time. Prove that your algorithm minimizes the average completion time, and state the running time of your algorithm.

Suppose a permutation of $S$ is $\langle r\_1, r\_2, \dots, r\_n \rangle$, the total completion time is $\displaystyle \sum\_{i=1}^n (n - i + 1) \cdot p\_{r\_i}$.
The optimal solution is to sort $p\_i$ into increasing order.

> __*b*__. Suppose now that the tasks are not all available at once. That is, each task cannot start until its __*release time*__ $r\_i$ . Suppose also that we allow __*preemption*__, so that a task can be suspended and restarted at a later time. For example, a task $a\_i$ with processing time $p\_i = 6$ and release time $r\_i = 1$ might start running at time $1$ and be preempted at time $4$. It might then resume at time $10$ but be preempted at time $11$, and it might finally resume at time $13$ and complete at time $15$. Task $a\_i$ has run for a total of $6$ time units, but its running time has been divided into three pieces. In this scenario, $a\_i$'s completion time is $15$. Give an algorithm that schedules the tasks so as to minimize the average completion time in this new scenario. Prove that your algorithm minimizes the average completion time, and state the running time of your algorithm.

Preemption will not yield a better solution if there is no new task.
Each time there is a new task, assume that the current running task is preempted, let the current condition be a new scheduling task without preemption.

### 16-3 Acyclic subgraphs

> __*a*__. The __*incidence matrix*__ for an undirected graph $G = (V, E)$ is a $|V| \times |E|$ matrix $M$ such that $M\_{ve} = 1$ if edge $e$ is incident on vertex $v$, and $M\_{ve} = 0$ otherwise. Argue that a set of columns of $M$ is linearly independent over the field of integers modulo 2 if and only if the corresponding set of edges is acyclic. Then, use the result of Exercise 16.4-2 to provide an alternate proof that $(E, I)$ of part (a) is a matroid.

> __*b*__. Suppose that we associate a nonnegative weight $w(e)$ with each edge in an undirected graph $G = (V, E)$. Give an efficient algorithm to find an acyclic subset of $E$ of maximum total weight.

Maximum spanning tree.

> __*c*__. Let $G(V, E)$ be an arbitrary directed graph, and let $(E, I)$ be defined so that $A \in I$ if and only if $A$ does not contain any directed cycles. Give an example of a directed graph $G$ such that the associated system $(E, I)$ is not a matroid. Specify which defining condition for a matroid fails to hold.

> __*d*__. The __*incidence matrix*__ for a directed graph $G = (V, E)$ with no self-loops is a $|V| \times |E|$ matrix $M$ such that $M\_{ve} = -1$ if edge $e$ leaves vertex $v$, $M\_{ve} = 1$ if edge $e$ enters vertex $v$, and $M\_{ve} = 0$ otherwise. Argue that if a set of columns of $M$ is linearly independent, then the corresponding set of edges does not contain a directed cycle.

> __*e*__. Exercise 16.4-2 tells us that the set of linearly independent sets of columns of any matrix $M$ forms a matroid. Explain carefully why the results of parts (d) and (e) are not contradictory. How can there fail to be a perfect correspondence between the notion of a set of edges being acyclic and the notion of the associated set of columns of the incidence matrix being linearly independent?

### 16-4 Scheduling variations

> Consider the following algorithm for the problem from Section 16.5 of scheduling unit-time tasks with deadlines and penalties. Let all $n$ time slots be initially empty, where time slot $i$ is the unit-length slot of time that finishes at time $i$. We consider the tasks in order of monotonically decreasing penalty. When considering task $a\_j$, if there exists a time slot at or before $a\_j$'s deadline $d\_j$ that is still empty, assign $a\_j$ to the latest such slot, filling it. If there is no such slot, assign task $a\_j$ to the latest of the as yet unfilled slots.

> __*a*__. Argue that this algorithm always gives an optimal answer.

> __*b*__. Use the fast disjoint-set forest presented in Section 21.3 to implement the algorithm efficiently. Assume that the set of input tasks has already been sorted into monotonically decreasing order by penalty. Analyze the running time of your implementation.

### 16-5 Off-line caching

> __*a*__. Write pseudocode for a cache manager that uses the furthest-in-future strategy. The input should be a sequence $\langle r\_1, r2, \dots, r\_n \rangle$ of requests and a cache size $k$, and the output should be a sequence of decisions about which data element (if any) to evict upon each request. What is the running time of your algorithm?

> __*b*__. Show that the off-line caching problem exhibits optimal substructure.

> __*c*__. Prove that furthest-in-future produces the minimum possible number of cache misses.
