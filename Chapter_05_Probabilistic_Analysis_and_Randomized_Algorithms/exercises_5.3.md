## 5.3 Randomized algorithms

### 5.3-1

> Professor Marceau objects to the loop invariant used in the proof of Lemma 5.5. He questions whether it is true prior to the first iteration. He reasons that we could just as easily declare that an empty subarray contains no 0-permutations. Therefore, the probability that an empty subarray contains a 0-permutation should be 0, thus
invalidating the loop invariant prior to the first iteration. Rewrite the procedure RANDOMIZE-IN-PLACE so that its associated loop invariant applies to a nonempty subarray prior to the first iteration, and modify the proof of Lemma 5.5 for your procedure.

$\dots$

### 5.3-2

> Professor Kelp decides to write a procedure that produces at random any permutation besides the identity permutation. He proposes the following procedure:

> ```
PERMUTE-WITHOUT-IDENTITY(A)
1 n = A.length
2 for i = 1 to n - 1
3     swap A[i] with A[RANDOM(i + 1, n)]
```

> Does this code do what Professor Kelp intends?

It's not uniform.

### 5.3-3

> Suppose that instead of swapping element $A[i]$ with a random element from the subarray $A[i \dots n]$, we swapped it with a random element from anywhere in the array:

> ```
PERMUTE-WITH-ALL(A)
1 n = A.length
2 for i = 1 to n
3     swap A[i] with A[RANDOM(1, n)]
```

> Does this code produce a uniform random permutation? Why or why not?

No. $n! \nmid n^n$.

### 5.3-4

> Professor Armstrong suggests the following procedure for generating a uniform random permutation:

> ```
PERMUTE-BY-CYCLIC(A)
1 n = A.length
2 let B[1..n] be a new array
3 offset = RANDOM(1, n)
4 for i = 1 to n
5     dest = i + offset
6     if dest > n
7         dest = dest - n
8     B[dest] = A[i]
9 return B
```

> Show that each element $A[i]$ has a $1/n$ probability of winding up in any particular position in $B$. Then show that Professor Armstrong is mistaken by showing that the resulting permutation is not uniformly random.

$n! \nmid n$

### 5.3-5 $\star$

> Prove that in the array $P$ in procedure PERMUTE-BY-SORTING, the probability that all elements are unique is at least $1 - 1/n$.

$$
\begin{array}{rll}
P &=& 1 \cdot (1 - \frac{1}{n^3}) \cdot (1 - \frac{2}{n^3}) \cdots (1 - \frac{n}{n^3}) \\
&\ge& 1 \cdot (1 - \frac{n}{n^3}) \cdot (1 - \frac{n}{n^3}) \cdots (1 - \frac{n}{n^3}) \\
&\ge& (1 - \frac{1}{n^2})^n \\
&\ge& 1 - n \cdot \frac{1}{n^2} \\
&=& 1 - 1/n \\
\end{array}
$$

### 5.3-6 

> Explain how to implement the algorithm PERMUTE-BY-SORTING to handle the case in which two or more priorities are identical. That is, your algorithm should produce a uniform random permutation, even if two or more priorities are identical.

Regenerate.

### 5.3-7

> Suppose we want to create a __*random sample*__ of the set $\{1,2,3,\dots,n\}$, that is, an $m$-element subset $S$, where $0 \le m \le n$, such that each $m$-subset is equally likely to be created. One way would be to set $A[i] = i$ for $i = 1, 2, 3, \dots, n$, call RANDOMIZE-IN-PLACE($A$), and then take just the first $m$ array elements. This method would make $n$ calls to the RANDOM procedure. If $n$ is much larger than $m$, we can create a random sample with fewer calls to RANDOM. Show that the following recursive procedure returns a random $m$-subset $S$ of $\{1,2,3,\dots,n\}$, in which each $m$-subset is equally likely, while making only $m$ calls to RANDOM:

> ```
RANDOM-SAMPLE(m, n)
1 if m == 0
2     return \varnothing;
3 else S = RANDOM-SAMPLE(m - 1, n - 1)
4     i = RANDOM(1, n)
5     if i \in S
6         S = S \cup {n}
7     else S = S \cup {i}
8     return S
```

For $m=1$, the subset is uniformly sampled with probability $1/n$;

Suppose RANDOM-SAMPLE$(m - 1, n - 1)$ creates an uniform subset,

for RANDOM-SAMPLE$(m, n)$, the probability of choosing $n$ is:

$$
\underbrace{\frac{n-1}{n}}_{i \in [1, n-1]} \underbrace{\cdot \frac{m-1}{n-1}}_{i \in S_{m-1}} + \underbrace{\frac{1}{n}}_{i=n} = \frac{m}{n}  
$$

the probability of $k$ $(k < n)$ is choosed is:

$$
\underbrace{\frac{1}{n}}_{i = k} \cdot \underbrace{\frac{(n-1)-(m-1)}{n-1}}_{k \notin S_{m-1}}+\underbrace{\frac{m-1}{n-1}}_{k \in S_{m-1}} = \frac{m}{n} 
$$
