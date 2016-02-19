## Problems

### 17-1 Bit-reversed binary counter

> Chapter 30 examines an important algorithm called the fast Fourier transform, or FFT. The first step of the FFT algorithm performs a __*bit-reversal permutation*__ on an input array $$A[0 \dots n-1]$$ whose length is $$n = 2^k$$ for some nonnegative integer $$k$$. This permutation swaps elements whose indices have binary representations that are the reverse of each other.

> We can express each index $$a$$ as a $$k$$-bit sequence $$\langle a_{k-1}, a_{k-2}, \dots, a_0 \rangle$$, where $$a = \sum_{i=0}^{k-1} a_i 2^i$$. We define

> $$\text{rev}_k(\langle a_{k-1}, a_{k-2}, \dots, a_0 \rangle) = \langle a_0, a_1, \dots, a_{k-1} \rangle$$;

> thus,

> $$\displaystyle \text{rev}_k(a) = \sum_{i=0}^{k-1} a_{k-i-1} 2^i$$.

> For example, if $$n = 16$$ (or, equivalently, $$k = 4$$), then $$\text{rev}_k(3) = 12$$, since the $$4$$-bit representation of $$3$$ is $$0011$$, which when reversed gives $$1100$$, the $$4$$-bit representation of $$12$$.

> __*a*__. Given a function $$\text{rev}_k$$ that runs in $$\Theta(k)$$ time, write an algorithm to perform the bit-reversal permutation on an array of length $$n = 2^k$$ in $$O(nk)$$ time.

```python
def rev_k(k, a):
    x = 0
    for _ in xrange(k):
        x <<= 1
        x += a & 1
        a >>= 1
    return x
```

> We can use an algorithm based on an amortized analysis to improve the running time of the bit-reversal permutation. We maintain a "bit-reversed counter" and a procedure BIT-REVERSED-INCREMENT that, when given a bit-reversed-counter value $$a$$, produces $$\text{rev}_k(\text{rev}_k(a) + 1)$$. If $$k = 4$$, for example, and the bit-reversed counter starts at $$0$$, then successive calls to BIT-REVERSED-INCREMENT produce the sequence

> $$0000, 1000, 0100, 1100, 0010, 1010, \dots = 0, 8, 4, 12, 2, 10, \dots$$.

> __*b*__. Assume that the words in your computer store $$k$$-bit values and that in unit time, your computer can manipulate the binary values with operations such as shifting left or right by arbitrary amounts, bitwise-AND, bitwise-OR, etc. Describe an implementation of the BIT-REVERSED-INCREMENT procedure that allows the bit-reversal permutation on an $$n$$-element array to be performed in a total of $$O(n)$$ time.

```python
class BitReversedCounter:
    def __init__(self, k):
        self.k = k
        self.c = 0

    def increment(self):
        for i in xrange(self.k - 1, -1, -1):
            self.c ^= 1 << i
            if self.c & (1 << i) > 0:
                break
        return self.c
```

> __*c*__. Suppose that you can shift a word left or right by only one bit in unit time. Is it still possible to implement an $$O(n)$$-time bit-reversal permutation?

```python
class BitReversedCounter:
    def __init__(self, k):
        self.k = k
        self.c = 0
        self.n = 1 << (self.k - 1)

    def increment(self):
        i = self.n
        for _ in xrange(self.k - 1, -1, -1):
            self.c ^= i
            if self.c & i > 0:
                break
            i >>= 1
        return self.c
```

### 17-2 Making binary search dynamic

> Binary search of a sorted array takes logarithmic search time, but the time to insert a new element is linear in the size of the array. We can improve the time for insertion by keeping several sorted arrays.

> Specifically, suppose that we wish to support SEARCH and INSERT on a set of $$n$$ elements. Let $$k = \lceil \lg(n + 1) \rceil$$, and let the binary representation of $$n$$ be $$\langle n_{k-1}, n_{k-2}, \dots, n_0 \rangle$$. We have $$k$$ sorted arrays $$A_0, A_1, \dots, A_{k-1}$$, where for $$i = 0, 1, \dots, k - 1$$, the length of array $$A_i$$ is $$2^i$$. Each array is either full or empty, depending on whether $$n_i = 1$$ or $$n_i = 0$$, respectively. The total number of elements held in all $$k$$ arrays is therefore $$\sum_{i=0}^{k-1} n_i 2^i = n$$. Although each individual array is sorted, elements in different arrays bear no particular relationship to each other.

> __*a*__. Describe how to perform the SEARCH operation for this data structure. Analyze its worst-case running time.

$$O(\lg^2 n)$$

> __*b*__. Describe how to perform the INSERT operation. Analyze its worst-case and amortized running times.

Merge sort.

Worst: $$O(n)$$

Amortized: $$O(\lg n)$$

> __*c*__. Discuss how to implement DELETE.

### 17-3 Amortized weight-balanced trees

> Consider an ordinary binary search tree augmented by adding to each node $$x$$ the attribute $$x.size$$ giving the number of keys stored in the subtree rooted at $$x$$. Let $$\alpha$$ be a constant in the range $$1/2 \le \alpha < 1$$. We say that a given node $$x$$ is __*$$\alpha$$-balanced*__ if $$x.left.size \le \alpha \cdot x.size$$ and $$x.right.size \le \alpha \cdot x.size$$. The tree as a whole is __*$$\alpha$$-balanced*__ if every node in the tree is $$\alpha$$-balanced. The following amortized approach to maintaining weight-balanced trees was suggested by G. Varghese.

> __*a*__. A $$1/2$$-balanced tree is, in a sense, as balanced as it can be. Given a node $$x$$ in an arbitrary binary search tree, show how to rebuild the subtree rooted at $$x$$ so that it becomes $$1/2$$-balanced. Your algorithm should run in time $$\Theta(x.size)$$, and it can use $$O(x.size)$$ auxiliary storage.

Choose the middle node as the root.

> __*b*__. Show that performing a search in an $$n$$-node $$\alpha$$-balanced binary search tree takes $$O(\lg n)$$ worst-case time.

Let $$\beta = 1 / \alpha$$, $$\beta^k = n$$, $$k = \log_\beta n = O(\log n) = O(\lg n)$$.

> For the remainder of this problem, assume that the constant $$\alpha$$ is strictly greater than $$1/2$$. Suppose that we implement INSERT and DELETE as usual for an $$n$$-node binary search tree, except that after every such operation, if any node in the tree is no longer $$\alpha$$-balanced, then we "rebuild" the subtree rooted at the highest such node in the tree so that it becomes $$1/2$$-balanced.

> We shall analyze this rebuilding scheme using the potential method. For a node $$x$$ in a binary search tree $$T$$, we define

> $$\Delta(x) = | x.left.size - x.right.size |$$,

> and we define the potential of $$T$$ as

> $$\displaystyle \Phi(T) = c \sum_{x \in T: \Delta(x) \ge 2} \Delta(x)$$,

> where $$c$$ is a sufficiently large constant that depends on $$\alpha$$.

> __*c*__. Argue that any binary search tree has nonnegative potential and that a $$1/2$$-balanced tree has potential 0.

$$\Delta(x) \ge 0$$: nonnegative potential.

$$1/2$$-balanced: $$\Delta(x) \le 1$$, $$\Phi(T) = 0$$.

> __*d*__. Suppose that $$m$$ units of potential can pay for rebuilding an $$m$$-node subtree. How large must $$c$$ be in terms of $$\alpha$$ in order for it to take $$O(1)$$ amortized time to rebuild a subtree that is not $$\alpha$$-balanced?

$$
\begin{array}{rll}
\hat{c_i} &=& c_i + \Phi(D_i) - \Phi(D_{i-1}) \\
O(1) &=& m + \Phi(D_i) - \Phi(D_{i-1}) \\
\Phi(D_{i-1}) &=& m + \Phi(D_i) \\
\Phi(D_{i-1}) &\ge& m
\end{array}
$$

$$
\begin{array}{rll}
\Delta(x) &=& x.left.size - x.right.size \\
&\ge& \alpha \cdot m - ((1 - \alpha) m - 1) \\
&=& (2\alpha - 1)m + 1
\end{array}
$$

$$
\begin{array}{rll}
m &\le& c((2\alpha - 1)m + 1) \\
c &\ge& \displaystyle \frac{m}{(2\alpha - 1)m + 1} \\
&\ge& \displaystyle \frac{1}{2\alpha}
\end{array}
$$

> __*e*__. Show that inserting a node into or deleting a node from an $$n$$-node $$\alpha$$-balanced tree costs $$O(\lg n)$$ amortized time.

### 17-4 The cost of restructuring red-black trees

> There are four basic operations on red-black trees that perform __*structural modifications*__: node insertions, node deletions, rotations, and color changes. We have seen that RB-INSERT and RB-DELETE use only $$O(1)$$ rotations, node insertions, and node deletions to maintain the red-black properties, but they may make many more color changes.

> __*a*__. Describe a legal red-black tree with $$n$$ nodes such that calling RB-INSERT to add the $$(n + 1)$$st node causes $$\Omega(\lg n)$$ color changes. Then describe a legal red-black tree with $$n$$ nodes for which calling RB-DELETE on a particular node causes $$\Omega(\lg n)$$ color changes.

Insert: a complete red-black tree in which all nodes have different color with their parents.

Delete: a complete red-black tree in which all nodes are black.

> Although the worst-case number of color changes per operation can be logarithmic, we shall prove that any sequence of $$m$$ RB-INSERT and RB-DELETE operations on an initially empty red-black tree causes $$O(m)$$ structural modifications in the worst case. Note that we count each color change as a structural modification.

> __*b*__. Some of the cases handled by the main loop of the code of both RB-INSERT-FIXUP and RB-DELETE-FIXUP are terminating: once encountered, they cause the loop to terminate after a constant number of additional operations. For each of the cases of RB-INSERT-FIXUP and RB-DELETE-FIXUP, specify which are terminating and which are not.

RB-INSERT-FIXUP: all cases except for case 1.

RB-DELETE-FIXUP: case 2.

> We shall first analyze the structural modifications when only insertions are performed. Let $$T$$ be a red-black tree, and define $$\Phi(T)$$ to be the number of red nodes in $$T$$. Assume that 1 unit of potential can pay for the structural modifications performed by any of the three cases of RB-INSERT-FIXUP.

> __*c*__. Let $$T'$$ be the result of applying Case 1 of RB-INSERT-FIXUP to $$T$$. Argue that $$\Phi(T') = \Phi(T) - 1$$.

Parent and uncle: red to black.

Grandparent: black to red.

> __*d*__. When we insert a node into a red-black tree using RB-INSERT, we can break the operation into three parts. List the structural modifications and potential changes resulting from lines 1–16 of RB-INSERT, from nonterminating cases of RB-INSERT-FIXUP, and from terminating cases of RB-INSERT-FIXUP.

Case 1: decrease by 1.

Case 2 & 3: no effect.

> __*e*__. Using part (d), argue that the amortized number of structural modifications performed by any call of RB-INSERT is $$O(1)$$.

$$O(1)$$

> We now wish to prove that there are $$O(m)$$ structural modifications when there are both insertions and deletions. Let us define, for each node $$x$$,

> $$\displaystyle w(x) = \left \{
\begin{array}{ll}
0 & \text{if}~x~\text{is red,} \\
1 & \text{if}~x~\text{is black and has no red children,} \\
0 & \text{if}~x~\text{is black and has one red children,} \\
2 & \text{if}~x~\text{is black and has two red children,} \\
\end{array}
\right .
$$

> Now we redefine the potential of a red-black tree $$T$$ as

> $$\displaystyle \Phi(T) = \sum_{x \in T} w(x)$$,

> and let $$T'$$ be the tree that results from applying any nonterminating case of RB-INSERT-FIXUP or RB-DELETE-FIXUP to $$T$$.

> __*f*__. Show that $$\Phi(T') \le \Phi(T) - 1$$ for all nonterminating cases of RB-INSERT-FIXUP. Argue that the amortized number of structural modifications performed by any call of RB-INSERT-FIXUP is $$O(1)$$.

$$O(1)$$

> __*g*__. Show that $$\Phi(T') \le \Phi(T) - 1$$ for all nonterminating cases of RB-DELETE-FIXUP. Argue that the amortized number of structural modifications performed by any call of RB-DELETE-FIXUP is $$O(1)$$.

$$O(1)$$

> __*h*__. Complete the proof that in the worst case, any sequence of $$m$$ RB-INSERT and RB-DELETE operations performs $$O(m)$$ structural modifications.

$$O(m)$$

### 17-5 Competitive analysis of self-organizing lists with move-to-front

> A __*self-organizing*__ list is a linked list of $$n$$ elements, in which each element has a unique key. When we search for an element in the list, we are given a key, and we want to find an element with that key.

> A self-organizing list has two important properties:

> 1\. To find an element in the list, given its key, we must traverse the list from the beginning until we encounter the element with the given key. If that element is the $$k$$th element from the start of the list, then the cost to find the element is $$k$$.

> 2\. We may reorder the list elements after any operation, according to a given rule with a given cost. We may choose any heuristic we like to decide how to reorder the list.

> Assume that we start with a given list of $$n$$ elements, and we are given an access sequence $$\sigma = \langle \sigma_1, \sigma_2, \dots, \sigma_m \rangle$$ of keys to find, in order. The cost of the sequence is the sum of the costs of the individual accesses in the sequence.

> Out of the various possible ways to reorder the list after an operation, this problem focuses on transposing adjacent list elements-switching their positions in the list—with a unit cost for each transpose operation. You will show, by means of a potential function, that a particular heuristic for reordering the list, move-to-front, entails a total cost no worse than 4 times that of any other heuristic for maintaining the list order—even if the other heuristic knows the access sequence in advance! We call this type of analysis a __*competitive analysis*__.

> For a heuristic $$H$$ and a given initial ordering of the list, denote the access cost of
sequence $$\sigma$$ by $$C_H(\sigma)$$ Let $$m$$ be the number of accesses in $$\sigma$$.

> __*a*__. Argue that if heuristic $$H$$ does not know the access sequence in advance, then the worst-case cost for $$H$$ on an access sequence $$\sigma$$ is $$C_H(\sigma) = \Omega(mn)$$.

Always last.

> With the __*move-to-front*__ heuristic, immediately after searching for an element $$x$$, we move $$x$$ to the first position on the list (i.e., the front of the list).

> Let $$\text{rank}_L(x)$$ denote the rank of element $$x$$ in list $$L$$, that is, the position of $$x$$ in list $$L$$. For example, if $$x$$ is the fourth element in $$L$$, then $$\text{rank}_L(x) = 4$$. Let $$c_i$$ denote the cost of access $$\sigma_i$$ using the move-to-front heuristic, which includes the cost of finding the element in the list and the cost of moving it to the front of the list by a series of transpositions of adjacent list elements.

> __*b*__. Show that if $$\sigma_i$$ accesses element $$x$$ in list $$L$$ using the move-to-front heuristic, then $$c_i = 2 \cdot \text{rank}_L(x) - 1$$.

Access: $$\text{rank}_L(x)$$

Move: $$\text{rank}_L(x) - 1$$

> Now we compare move-to-front with any other heuristic $$\text{H}$$ that processes an access sequence according to the two properties above. Heuristic $$\text{H}$$ may transpose elements in the list in any way it wants, and it might even know the entire access sequence in advance.

> Let $$L_i$$ be the list after access $$\sigma_i$$ using move-to-front, and let $$L_i^*$$ be the list after access $$\sigma_i$$ using heuristic $$\text{H}$$. We denote the cost of access $$\sigma_i$$ by $$c_i$$ for move-to-front and by $$c_i^*$$ for heuristic $$\text{H}$$. Suppose that heuristic $$\text{H}$$ performs $$t_i^*$$ transpositions during access $$\sigma_i$$.

> __*c*__. In part (b), you showed that $$c_i = 2 \cdot \text{rank}_{L_{i-1}}(x) - 1$$. Now show that $$c_i^* = \text{rank}_{L_{i-1}^*}(x) + t_i^*$$.

Access: $$\text{rank}_{L_{i-1}^*}(x)$$

Move: $$t_i^*$$

> We define an __*inversion*__ in list $$L_i$$ as a pair of elements $$y$$ and $$z$$ such that $$y$$ precedes $$z$$ in $$L_i$$ and $$z$$ precedes $$y$$ in list $$L_i^*$$. Suppose that list $$L_i$$ has $$q_i$$ inversions after processing the access sequence $$\langle \sigma_1, \sigma_2, \dots, \sigma_i \rangle$$. Then, we define a potential function $$\Phi$$ that maps $$L_i$$ to a real number by $$\Phi(L_i) = 2q_i$$. For example, if $$L_i$$ has the elements $$\langle e, c, a, d, b \rangle$$ and $$L_i^*$$ has the elements $$\langle c, a, b, d, e \rangle$$, then $$L_i$$ has 5 inversions $$((e, c), (e, a), (e, d), (e, b), (d, b))$$, and so $$\Phi(L_i) = 10$$. Observe that $$\Phi(L_i) \ge 0$$ for all $$i$$ and that, if move-to-front and heuristic $$\text{H}$$ start with the same list $$L_0$$, then $$\Phi(L_0) = 0$$.

> __*d*__. Argue that a transposition either increases the potential by 2 or decreases the potential by 2.

Same before: decrese by 2.

Same after: increase by 2.

> Suppose that access $$\sigma_i$$ finds the element $$x$$. To understand how the potential changes due to $$\sigma_i$$, let us partition the elements other than $$x$$ into four sets, depending on where they are in the lists just before the $$i$$th access:

> * Set $$A$$ consists of elements that precede $$x$$ in both $$L_{i-1}$$ and $$L_{i-1}^*$$.
> * Set $$B$$ consists of elements that precede $$x$$ in $$L_{i-1}$$ and follow $$x$$ in $$L_{i-1}^*$$.
> * Set $$C$$ consists of elements that follow $$x$$ in $$L_{i-1}$$ and precede $$x$$ in $$L_{i-1}^*$$.
> * Set $$D$$ consists of elements that follow $$x$$ in both $$L_{i-1}$$ and $$L_{i-1}^*$$.

> __*e*__. Argue that $$\text{rank}_{L_{i-1}}(x) = |A| + |B| + 1$$ and $$\text{rank}_{L_{i-1}^*}(x) = |A| + |C| + 1$$.

Precede.

> __*f*__. Show that access $$\sigma_i$$ causes a change in potential of

> $$\Phi(L_i) - \Phi(L_{i-1}) \le 2(|A| - |B| + t_i^*)$$,

> where, as before, heuristic $$\text{H}$$ performs $$t_i^*$$ transpositions during access $$\sigma_i$$.

> Define the amortized cost $$\hat{c_i}$$ of access $$\sigma_i$$ by $$\hat{c_i} = c_i + \Phi(L_i) - \Phi(L_{i-1})$$.

> __*g*__. Show that the amortized cost $$\hat{c_i}$$ of access $$\sigma_i$$ is bounded from above by $$4c_i^*$$.

$$
\begin{array}{rll}
\hat{c_i} &\le& 2(|A| + |B| + 1) - 1 + 2(|A| - |B| + t_i^*) \\
&=& 4|A| + 1 + 2 t_i^* \\
&\le& 4(|A| + |C| + 1 + t_i^*) \\
&=& 4 c_i^*
\end{array}
$$

> __*h*__. Conclude that the cost $$C_{MTF}(\sigma)$$ of access sequence $$\sigma$$ with move-to-front is at most 4 times the cost $$C_H(\sigma)$$ of $$\sigma$$ withany other heuristic $$\text{H}$$, assuming that both heuristics start with the same list.
