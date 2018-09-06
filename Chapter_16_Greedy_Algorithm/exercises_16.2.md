## 16.2 Elements of the greedy strategy

### 16.2-1

> Prove that the fractional knapsack problem has the greedy-choice property.

Obviously

### 16.2-2

> Give a dynamic-programming solution to the 0-1 knapsack problem that runs in $O(nW)$ time, where $n$ is the number of items and $W$ is the maximum weight of items that the thief can put in his knapsack.

```python
def zero_one_knapsack(v, w, W):
    n = len(v)
    dp = [0] * (W + 1)
    for i in range(n):
        for j in range(W, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[W]
```

### 16.2-3

> Suppose that in a 0-1 knapsack problem, the order of the items when sorted by increasing weight is the same as their order when sorted by decreasing value. Give an efficient algorithm to find an optimal solution to this variant of the knapsack problem, and argue that your algorithm is correct.

Suppose in an optimal solution we take an item with $v\_1$, $w\_1$, and drop an item with $v\_2$, $w\_2$, and $w\_1 > w\_2$, $v\_1 < v\_2$, we can substitude $1$ with $2$ and get a better solution. Therefore we should always choose the items with the greatest values.

### 16.2-4

> Professor Gekko has always dreamed of inline skating across North Dakota. He plans to cross the state on highway U.S. 2, which runs from Grand Forks, on the eastern border with Minnesota, to Williston, near the western border withMontana. The professor can carry two liters of water, and he can skate $m$ miles before running out of water. (Because North Dakota is relatively flat, the professor does not have to worry about drinking water at a greater rate on uphill sections than on flat or downhill sections.) The professor will start in Grand Forks with two full liters of water. His official North Dakota state map shows all the places along U.S. 2 at which he can refill his water and the distances between these locations.

> The professor's goal is to minimize the number of water stops along his route across the state. Give an efficient method by which he can determine which water stops he should make. Prove that your strategy yields an optimal solution, and give its running time.

Go to the furthest stop within $m$ miles in each iteration.

### 16.2-5

> Describe an efficient algorithm that, given a set $\\{ x\_1, x\_2, \dots, x\_n \\}$ of points on the real line, determines the smallest set of unit-length closed intervals that contains all of the given points. Argue that your algorithm is correct.

Place the left side of the unit-interval to the first left-most uncovered point in each iteration.

### 16.2-6 $\star$

> Show how to solve the fractional knapsack problem in $O(n)$ time.

Choose the median of $v\_i / w\_i$ in $O(n)$, partition the sequence with the median in $O(n)$, if the sum of weights in the more valuable side is less or equal to $W$, we take all the items in this side and repeat the steps in the other side; otherwise we repeat the steps in the more valuable side. The algorithm runs in $T(n) = T(n/2) + O(n)$, which is $O(n)$.

### 16.2-7

> Suppose you are given two sets $A$ and $B$, each containing $n$ positive integers. You can choose to reorder each set however you like. After reordering, let $a\_i$ be the $i$th element of set $A$, and let $b\_i$ be the $i$ th element of set $B$. You then receive a payoff of $\prod\_{i=1}^n a\_i^{b\_i}$ . Give an algorithm that will maximize your payoff. Prove that your algorithm maximizes the payoff, and state its running time.

Sort $A$ and $B$ into monotonically increasing/decreasing order.
