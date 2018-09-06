### 17-4 The cost of restructuring red-black trees

> There are four basic operations on red-black trees that perform __*structural modifications*__: node insertions, node deletions, rotations, and color changes. We have seen that RB-INSERT and RB-DELETE use only $O(1)$ rotations, node insertions, and node deletions to maintain the red-black properties, but they may make many more color changes.

> __*a*__. Describe a legal red-black tree with $n$ nodes such that calling RB-INSERT to add the $(n + 1)$st node causes $\Omega(\lg n)$ color changes. Then describe a legal red-black tree with $n$ nodes for which calling RB-DELETE on a particular node causes $\Omega(\lg n)$ color changes.

Insert: a complete red-black tree in which all nodes have different color with their parents.

Delete: a complete red-black tree in which all nodes are black.

> Although the worst-case number of color changes per operation can be logarithmic, we shall prove that any sequence of $m$ RB-INSERT and RB-DELETE operations on an initially empty red-black tree causes $O(m)$ structural modifications in the worst case. Note that we count each color change as a structural modification.

> __*b*__. Some of the cases handled by the main loop of the code of both RB-INSERT-FIXUP and RB-DELETE-FIXUP are terminating: once encountered, they cause the loop to terminate after a constant number of additional operations. For each of the cases of RB-INSERT-FIXUP and RB-DELETE-FIXUP, specify which are terminating and which are not.

RB-INSERT-FIXUP: all cases except for case 1.

RB-DELETE-FIXUP: case 2.

> We shall first analyze the structural modifications when only insertions are performed. Let $T$ be a red-black tree, and define $\Phi(T)$ to be the number of red nodes in $T$. Assume that 1 unit of potential can pay for the structural modifications performed by any of the three cases of RB-INSERT-FIXUP.

> __*c*__. Let $T'$ be the result of applying Case 1 of RB-INSERT-FIXUP to $T$. Argue that $\Phi(T') = \Phi(T) - 1$.

Parent and uncle: red to black.

Grandparent: black to red.

> __*d*__. When we insert a node into a red-black tree using RB-INSERT, we can break the operation into three parts. List the structural modifications and potential changes resulting from lines 1–16 of RB-INSERT, from nonterminating cases of RB-INSERT-FIXUP, and from terminating cases of RB-INSERT-FIXUP.

Case 1: decrease by 1.

Case 2 & 3: no effect.

> __*e*__. Using part (d), argue that the amortized number of structural modifications performed by any call of RB-INSERT is $O(1)$.

$O(1)$

> We now wish to prove that there are $O(m)$ structural modifications when there are both insertions and deletions. Let us define, for each node $x$,

> $$\displaystyle w(x) = \left \\{
\begin{array}{ll}
0 & \text{if}\~x\~\text{is red,} \\\\
1 & \text{if}\~x\~\text{is black and has no red children,} \\\\
0 & \text{if}\~x\~\text{is black and has one red children,} \\\\
2 & \text{if}\~x\~\text{is black and has two red children,} \\\\
\end{array}
\right .
$$

> Now we redefine the potential of a red-black tree $T$ as

> $\displaystyle \Phi(T) = \sum\_{x \in T} w(x)$,

> and let $T'$ be the tree that results from applying any nonterminating case of RB-INSERT-FIXUP or RB-DELETE-FIXUP to $T$.

> __*f*__. Show that $\Phi(T') \le \Phi(T) - 1$ for all nonterminating cases of RB-INSERT-FIXUP. Argue that the amortized number of structural modifications performed by any call of RB-INSERT-FIXUP is $O(1)$.

$O(1)$

> __*g*__. Show that $\Phi(T') \le \Phi(T) - 1$ for all nonterminating cases of RB-DELETE-FIXUP. Argue that the amortized number of structural modifications performed by any call of RB-DELETE-FIXUP is $O(1)$.

$O(1)$

> __*h*__. Complete the proof that in the worst case, any sequence of $m$ RB-INSERT and RB-DELETE operations performs $O(m)$ structural modifications.

$O(m)$

### 17-5 Competitive analysis of self-organizing lists with move-to-front

> A __*self-organizing*__ list is a linked list of $n$ elements, in which each element has a unique key. When we search for an element in the list, we are given a key, and we want to find an element with that key.

> A self-organizing list has two important properties:

> 1\. To find an element in the list, given its key, we must traverse the list from the beginning until we encounter the element with the given key. If that element is the $k$th element from the start of the list, then the cost to find the element is $k$.

> 2\. We may reorder the list elements after any operation, according to a given rule with a given cost. We may choose any heuristic we like to decide how to reorder the list.

> Assume that we start with a given list of $n$ elements, and we are given an access sequence $\sigma = \langle \sigma\_1, \sigma\_2, \dots, \sigma\_m \rangle$ of keys to find, in order. The cost of the sequence is the sum of the costs of the individual accesses in the sequence.

> Out of the various possible ways to reorder the list after an operation, this problem focuses on transposing adjacent list elements-switching their positions in the list—with a unit cost for each transpose operation. You will show, by means of a potential function, that a particular heuristic for reordering the list, move-to-front, entails a total cost no worse than 4 times that of any other heuristic for maintaining the list order—even if the other heuristic knows the access sequence in advance! We call this type of analysis a __*competitive analysis*__.

> For a heuristic $H$ and a given initial ordering of the list, denote the access cost of
sequence $\sigma$ by $C\_H(\sigma)$ Let $m$ be the number of accesses in $\sigma$.

> __*a*__. Argue that if heuristic $H$ does not know the access sequence in advance, then the worst-case cost for $H$ on an access sequence $\sigma$ is $C\_H(\sigma) = \Omega(mn)$.

Always last.

> With the __*move-to-front*__ heuristic, immediately after searching for an element $x$, we move $x$ to the first position on the list (i.e., the front of the list).

> Let $\text{rank}\_L(x)$ denote the rank of element $x$ in list $L$, that is, the position of $x$ in list $L$. For example, if $x$ is the fourth element in $L$, then $\text{rank}\_L(x) = 4$. Let $c\_i$ denote the cost of access $\sigma\_i$ using the move-to-front heuristic, which includes the cost of finding the element in the list and the cost of moving it to the front of the list by a series of transpositions of adjacent list elements.

> __*b*__. Show that if $\sigma\_i$ accesses element $x$ in list $L$ using the move-to-front heuristic, then $c\_i = 2 \cdot \text{rank}\_L(x) - 1$.

Access: $\text{rank}\_L(x)$

Move: $\text{rank}\_L(x) - 1$

> Now we compare move-to-front with any other heuristic $\text{H}$ that processes an access sequence according to the two properties above. Heuristic $\text{H}$ may transpose elements in the list in any way it wants, and it might even know the entire access sequence in advance.

> Let $L\_i$ be the list after access $\sigma\_i$ using move-to-front, and let $L\_i^\*$ be the list after access $\sigma\_i$ using heuristic $\text{H}$. We denote the cost of access $\sigma\_i$ by $c\_i$ for move-to-front and by $c\_i^\*$ for heuristic $\text{H}$. Suppose that heuristic $\text{H}$ performs $t\_i^\*$ transpositions during access $\sigma\_i$.

> __*c*__. In part (b), you showed that $c\_i = 2 \cdot \text{rank}\_{L\_{i-1}}(x) - 1$. Now show that $c\_i^\* = \text{rank}\_{L\_{i-1}^\*}(x) + t\_i^\*$.

Access: $\text{rank}\_{L\_{i-1}^\*}(x)$

Move: $t\_i^\*$

> We define an __*inversion*__ in list $L\_i$ as a pair of elements $y$ and $z$ such that $y$ precedes $z$ in $L\_i$ and $z$ precedes $y$ in list $L\_i^\*$. Suppose that list $L\_i$ has $q\_i$ inversions after processing the access sequence $\langle \sigma\_1, \sigma\_2, \dots, \sigma\_i \rangle$. Then, we define a potential function $\Phi$ that maps $L\_i$ to a real number by $\Phi(L\_i) = 2q\_i$. For example, if $L\_i$ has the elements $\langle e, c, a, d, b \rangle$ and $L\_i^\*$ has the elements $\langle c, a, b, d, e \rangle$, then $L\_i$ has 5 inversions $((e, c), (e, a), (e, d), (e, b), (d, b))$, and so $\Phi(L\_i) = 10$. Observe that $\Phi(L\_i) \ge 0$ for all $i$ and that, if move-to-front and heuristic $\text{H}$ start with the same list $L\_0$, then $\Phi(L\_0) = 0$.

> __*d*__. Argue that a transposition either increases the potential by 2 or decreases the potential by 2.

Same before: decrese by 2.

Same after: increase by 2.

> Suppose that access $\sigma\_i$ finds the element $x$. To understand how the potential changes due to $\sigma\_i$, let us partition the elements other than $x$ into four sets, depending on where they are in the lists just before the $i$th access:

> * Set $A$ consists of elements that precede $x$ in both $L\_{i-1}$ and $L\_{i-1}^\*$.
> * Set $B$ consists of elements that precede $x$ in $L\_{i-1}$ and follow $x$ in $L\_{i-1}^\*$.
> * Set $C$ consists of elements that follow $x$ in $L\_{i-1}$ and precede $x$ in $L\_{i-1}^\*$.
> * Set $D$ consists of elements that follow $x$ in both $L\_{i-1}$ and $L\_{i-1}^\*$.

> __*e*__. Argue that $\text{rank}\_{L\_{i-1}}(x) = |A| + |B| + 1$ and $\text{rank}\_{L\_{i-1}^\*}(x) = |A| + |C| + 1$.

Precede.

> __*f*__. Show that access $\sigma\_i$ causes a change in potential of

> $\Phi(L\_i) - \Phi(L\_{i-1}) \le 2(|A| - |B| + t\_i^\*)$,

> where, as before, heuristic $\text{H}$ performs $t\_i^\*$ transpositions during access $\sigma\_i$.

> Define the amortized cost $\hat{c\_i}$ of access $\sigma\_i$ by $\hat{c\_i} = c\_i + \Phi(L\_i) - \Phi(L\_{i-1})$.

> __*g*__. Show that the amortized cost $\hat{c\_i}$ of access $\sigma\_i$ is bounded from above by $4c\_i^\*$.

$$
\begin{array}{rll}
\hat{c\_i} &\le& 2(|A| + |B| + 1) - 1 + 2(|A| - |B| + t\_i^\*) \\\\
&=& 4|A| + 1 + 2 t\_i^\* \\\\
&\le& 4(|A| + |C| + 1 + t\_i^\*) \\\\
&=& 4 c\_i^\*
\end{array}
$$

> __*h*__. Conclude that the cost $C\_{MTF}(\sigma)$ of access sequence $\sigma$ with move-to-front is at most 4 times the cost $C\_H(\sigma)$ of $\sigma$ with any other heuristic $\text{H}$, assuming that both heuristics start with the same list.
