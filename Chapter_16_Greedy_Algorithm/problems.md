## Problems

### 16-1 Coin changing

> Consider the problem of making change for $$n$$ cents using the fewest number of coins. Assume that each coin's value is an integer.

> __*a*__. Describe a greedy algorithm to make change consisting of quarters, dimes, nickels, and pennies. Prove that your algorithm yields an optimal solution.

Use the coin as large as possible.

> __*b*__. Suppose that the available coins are in the denominations that are powers of $$c$$, i.e., the denominations are $$c^0, c^1, \dots, c^k$$ for some integers $$c > 1$$ and $$k \ge 1$$. Show that the greedy algorithm always yields an optimal solution.

Same.

> __*c*__. Give a set of coin denominations for which the greedy algorithm does not yield an optimal solution. Your set should include a penny so that there is a solution for every value of $$n$$.

$$\langle 10, 9, 1 \rangle$$

For 18, the greedy algorithm yields 9 coins, the optimal solution is $$\langle 9,9 \rangle$$, which contains 2 coins.

> __*d*__. Give an $$O(nk)$$-time algorithm that makes change for any set of $$k$$ different coin denominations, assuming that one of the coins is a penny.

Sort the denominations into decreasing order, for $$i=k$$ to $$1$$, choose $$n / c_i$$ coins, remaining $$n~\text{mod}~c_i$$.

