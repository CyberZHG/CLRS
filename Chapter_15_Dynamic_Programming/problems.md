## Problems

### 15-1 Longest simple path in a directed acyclic graph

> Suppose that we are given a directed acyclic graph $$G = (V, E)$$ with real-valued edge weights and two distinguished vertices $$s$$ and $$t$$ . Describe a dynamic-programming approach for finding a longest weighted simple path from $$s$$ to $$t$$ . What does the subproblem graph look like? What is the efficiency of your algorithm?

Topological sort.

### 15-2 Longest palindrome subsequence

> A __*palindrome*__ is a nonempty string over some alphabet that reads the same forward and backward. Examples of palindromes are all strings of length 1, civic, racecar, and aibohphobia (fear of palindromes). 
> Give an efficient algorithm to find the longest palindrome that is a subsequence of a given input string. For example, given the input character, your algorithm should return carac. What is the running time of your algorithm?

LCS of the original string and the reversed string.
