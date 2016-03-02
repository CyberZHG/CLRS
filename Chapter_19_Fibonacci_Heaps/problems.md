## Problems

### 19-1 Alternative implementation of deletion

> Professor Pisano has proposed the following variant of the FIB-HEAP-DELETE procedure, claiming that it runs faster when the node being deleted is not the node pointed to by $$H.min$$.

> ```
PISANO-DELETE(H, x)
1 if x == H.min
2      FIB-HEAP-EXTRACT-MIN(H)
3 else y = x.p
4      if y != NIL
5           CUT(H, x, y)
6           CASCADING-CUT(H, y)
7      add x's child list to the root list of H
8      remove x from the root list of H
```

> __*a*__. The professor’s claim that this procedure runs faster is based partly on the assumption that line 7 can be performed in $$O(1)$$ actual time. What is wrong with this assumption?

The largest degree is $$D(n) = O(\lg n)$$.

> __*b*__. Give a good upper bound on the actual time of PISANO-DELETE when $$x$$ is not $$H.min$$. Your bound should be in terms of $$x.degree$$ and the number $$c$$ of calls to the CASCADING-CUT procedure.

$$O(x.degree + c)$$.

> __*c*__. Suppose that we call PISANO-DELETE$$(H, x)$$, and let $$H'$$ be the Fibonacci heap that results. Assuming that node $$x$$ is not a root, bound the potential of $$H'$$ in terms of $$x.degree$$, $$c$$, $$t(H)$$, and $$m(H)$$.

$$\Phi(H') = [t(H) + x.degree + c] + 2 [m(H) - c + 2]$$.

> __*d*__. Conclude that the amortized time for PISANO-DELETE is asymptotically no better than for FIB-HEAP-DELETE, evenwhen $$x \ne H.min$$.

$$O(x.degree + c) + x.degree + 4 - c = O(x.degree + c) = O(\lg n)$$ is worse than $$O(1)$$.

### 19-2 Binomial trees and binomial heaps

> The __*binomial tree*__ $$B_k$$ is an ordered tree (see Section B.5.2) defined recursively. As shown in Figure 19.6(a), the binomial tree $$B_0$$ consists of a single node. The binomial tree $$B_k$$ consists of two binomial trees $$B_{k-1}$$ that are linked together so that the root of one is the leftmost child of the root of the other. Figure 19.6(b) shows the binomial trees $$B_0$$ through $$B_4$$.

> __*a*__. Show that for the binomial tree $$B_k$$,

> 1. there are $$2^k$$ nodes,
> 2. the height of the tree is $$k$$,
> 3. there are exactly $$\binom{k}{i}$$ nodes at depth $$i$$ for $$i = 0, 1, \dots, k$$, and
> 4. the root has degree $$k$$, which is greater than that of any other node; moreover, as Figure 19.6(c) shows, if we number the children of the root from left to right by $$k-1, k-2, \dots, 0$$, then child $$i$$ is the root of a subtree $$B_i$$.

1. $$B_k$$ consists of two binomial trees $$B_{k-1}$$.
2. The height of one $$B_{k-1}$$ is increased by 1.
3. For $$i=0$$, $$\binom{k}{0}=1$$ and only root is at depth $$0$$. Suppose in $$B_{k-1}$$, the number of nodes at depth $$i$$ is $$\binom{k-1}{i}$$, in $$B_k$$, the number of nodes at depth $$i$$ is $$\binom{k-1}{i} + \binom{k-1}{i-1} = \binom{k}{i}$$.
4. The degree of the root increase by 1.





