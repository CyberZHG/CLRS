## 16.2 Elements of the greedy strategy

### 16.2-1

> Prove that the fractional knapsack problem has the greedy-choice property.

Obviously

### 16.2-2

> Give a dynamic-programming solution to the 0-1 knapsack problem that runs in $$O(nW)$$ time, where $$n$$ is the number of items and $$W$$ is the maximum weight of items that the thief can put in his knapsack.

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

