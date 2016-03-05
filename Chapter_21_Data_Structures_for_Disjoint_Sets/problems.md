## Problems

### 21-1 Off-line minimum

> The __*off-line minimum problem*__ asks us to maintain a dynamic set $$T$$ of elements from the domain $$\{1, 2, \dots, n\}$$ under the operations INSERT and EXTRACT-MIN. We are given a sequence $$S$$ of $$n$$ INSERT and $$m$$ EXTRACT-MIN calls, where each key in $$\{1, 2, \dots, n\}$$ is inserted exactly once. We wish to determine which key is returned by each EXTRACT-MIN call. Specifically, we wish to fill in an array $$extracted[1 \dots m]$$, where for $$i = 1, 2, \dots, m$$, $$extracted[i]$$ is the key returned by the $$i$$th EXTRACT-MIN call. The problem is "off-line" in the sense that we are allowed to process the entire sequence $$S$$ before determining any of the returned keys.

> __*a*__. In the following instance of the off-line minimum problem, each operation INSERT$$(i)$$ is represented by the value of $$i$$ and each EXTRACT-MIN is represented by the letter E:

> 4, 8, E, 3, E, 9, 2, 6, E, E, E, 1, 7, E, 5.

> Fill in the correct values in the _extracted_ array.

4, 3, 2, 6, 8, 1.

> To develop an algorithm for this problem, we break the sequence $$S$$ into homogeneous subsequences. That is, we represent $$S$$ by

> $$I_1, E, I_2, E, I_3, \dots, I_m, E, I_{m+1}$$

> where each $$E$$ represents a single EXTRACT-MIN call and each $$\text{I}_j$$ represents a (possibly empty) sequence of INSERT calls. For each subsequence $$\text{I}_j$$ , we initially place the keys inserted by these operations into a set $$K_j$$ , which is empty if $$\text{I}_j$$ is empty. We then do the following:

> ```
OFF-LINE-MINIMUM(m, n)
1  for i = 1 to n
2       determine j such that i \in K_j
3       if j \ne m + 1
4            extracted[j] = i
5            let l be the smallest value greater than j
                   for which set K_l exists
6            K_l = K_j \cup K_l , destroying K_j
7  return extracted 
```

> __*b*__. Argue that the array extracted returned by OFF-LINE-MINIMUM is correct.

Greedy.

> __*c*__. Describe how to implement OFF-LINE-MINIMUM efficiently with a disjoint-set data structure. Give a tight bound on the worst-case running time of your implementation.

Disjoint-set forest.


