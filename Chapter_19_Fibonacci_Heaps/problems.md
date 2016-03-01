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

