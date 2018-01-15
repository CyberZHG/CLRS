## Problems

### 8-1 Probabilistic lower bounds on comparison sorting

> In this problem, we prove a probabilistic $$\Omega(n \lg n)$$ lower bound on the running time of any deterministic or randomized comparison sort on $$n$$ distinct input elements. We begin by examining a deterministic comparison sort $$A$$ with decision tree $$T_A$$. We assume that every permutation of $$A$$'s inputs is equally likely.

> __*a*__. Suppose that each leaf of $$T_A$$ is labeled with the probability that it is reached given a random input. Prove that exactly $$n!$$ leaves are labeled $$1/n!$$ and that the rest are labeled 0.

There should be only $$n!$$ leaves.

> __*b*__. Let $$D(T)$$ denote the external path length of a decision tree $$T$$ ; that is, $$D(T)$$ is the sum of the depths of all the leaves of $$T$$. Let $$T$$ be a decision tree with $$k > 1$$ leaves, and let $$LT$$ and $$RT$$ be the left and right subtrees of $$T$$. Show that $$D(T)=D(LT)+D(RT)+k$$.

Add $$T$$ means all the $$k$$ depths of leaves increase by 1.

> __*c*__. Let $$d(k)$$ be the minimum value of $$D(T)$$ over all decision trees $$T$$ with $$k > 1$$ leaves. Show that $$d(k)=\min _{1 \le i \le k - 1}\{d(i)+d(k-i)+k\}$$.

$$D(T)=D(LT)+D(RT)+k$$, $$d(k)=\min _{1 \le i \le k - 1}\{d(i)+d(k-i)+k\}$$ iterates all the possibilities.

> __*d*__. Prove that for a given value of $$k > 1$$ and $$i$$ in the range $$1 \le i \le k - 1$$, the function $$i \lg i + (k - i) \lg(k - i)$$ is minimized at $$i = k/2$$. Conclude that $$d(k) = \Omega(k \lg k)$$.

$$
\begin{array}{rll}
f(i) &=& i \lg i + (k - i) \lg (k - i) \\
f'(i) &=& \lg i - \lg (k - i) \\
0 &=& \displaystyle \lg \frac{i}{k-i} \\
1 &=& \displaystyle \frac{i}{k-i} \\
i &=& k / 2 \\
\end{array}
$$

> __*e*__. Prove that $$D(T_A)=\Omega(n!\lg (n!))$$, and conclude that the average-case time to sort $$n$$ elements is $$\Omega(n \lg n)$$.

$$d(T_A) = d(n!) = \Omega(n! \lg n!)$$

Average:
$$
\frac{\Omega(n! \lg n!)}{n!} = \Omega(\lg n!) = \Omega(n \lg n)
$$


> Now, consider a _randomized_ comparison sort $$B$$. We can extend the decision-tree model to handle randomization by incorporating two kinds of nodes: ordinary comparison nodes and "randomization" nodes. A randomization node models a random choice of the form RANDOM$$(1, r)$$ made by algorithm $$B$$; the node has $$r$$ children, each of which is equally likely to be chosen during an execution of the algorithm.

> __*f*__. Show that for any randomized comparison sort $$B$$, there exists a deterministic comparison sort $$A$$ whose expected number of comparisons is no more than those made by $$B$$.

$$\dots$$

### 8-2 Sorting in place in linear time

> Suppose that we have an array of $$n$$ data records to sort and that the key of each record has the value 0 or 1. An algorithm for sorting such a set of records might possess some subset of the following three desirable characteristics:
1. The algorithm runs in $$O(n)$$ time.
2. The algorithm is stable.
3. The algorithm sorts in place, using no more than a constant amount of storage space in addition to the original array.

> __*a*__. Give an algorithm that satisfies criteria 1 and 2 above.

Counting sort.

> __*b*__. Give an algorithm that satisfies criteria 1 and 3 above.

Partition.

> __*c*__. Give an algorithm that satisfies criteria 2 and 3 above.

Insertion sort.

> __*d*__. Can you use any of your sorting algorithms from parts (a)-(c) as the sorting method used in line 2 of RADIX-SORT, so that RADIX-SORT sorts n records with $$b$$-bit keys in $$O(bn)$$ time? Explain how or why not.

First, stable and quick.

> __*e*__. Suppose that the $$n$$ records have keys in the range from 1 to $$k$$. Show how to modify counting sort so that it sorts the records in place in $$O(n+k)$$ time. You may use $$O(k)$$ storage outside the input array. Is your algorithm stable?

Same as permutation group:

```python
def counting_in_place(a):
    k = max(a)
    c = [0 for _ in range(k + 1)]
    for v in a:
        c[v] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    r = c[:]
    for i in range(len(a)):
        while True:
            if a[i] == 0:
                if i < r[0]:
                    break
            else:
                if r[a[i] - 1] <= i < r[a[i]]:
                    break
            c[a[i]] -= 1
            pos = c[a[i]]
            a[i], a[pos] = a[pos], a[i]
```

Not stable.

### 8-3 Sorting variable-length items

> __*a*__. You are given an array of integers, where different integers may have different numbers of digits, but the total number of digits over all the integers in the array is $$n$$. Show how to sort the array in $$O(n)$$ time.

Suppose the number of integers which have $$b_i$$ digits is $$n_i$$, divide the integers into different buckets using counting sort, the integers in the same bucket have the same $$b_i$$, then use radix sort in each bucket:

$$
\sum_{i} b_i n_i = n
$$

therefore the algorithm is $$O(n)$$.

```python
def counting_sort(a, m):
    b = [0 for _ in range(len(a))]
    k = 10
    c = [0 for _ in range(k)]
    for s in a:
        c[ord(s[m]) - ord('0')] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        c[ord(a[i][m]) - ord('0')] -= 1
        b[c[ord(a[i][m]) - ord('0')]] = a[i]
    return b


def radix_sort(a):
    for m in range(len(a[0]) - 1, -1, -1):
        a = counting_sort(a, m)
    return a


def count_and_divide(a):
    a = map(str, a)
    b = [0 for _ in range(len(a))]
    k = 0
    for s in a:
        k = max(k, len(s))
    c = [0 for _ in range(k + 1)]
    for s in a:
        c[len(s)] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    r = c[:]
    for i in range(len(a) - 1, -1, -1):
        c[len(a[i])] -= 1
        b[c[len(a[i])]] = a[i]
    for i in range(k + 1):
        if c[i] < r[i]:
            b[c[i]:r[i]] = radix_sort(b[c[i]:r[i]])
    return map(int, b)
```

> __*b*__. You are given an array of strings, where different strings may have different numbers of characters, but the total number of characters over all the strings is $$n$$. Show how to sort the strings in $$O(n)$$ time. (Note that the desired order here is the standard alphabetical order; for example, $$a < ab < b$$.)

Sort the strings by their first characters with counting-sort, then divide the strings by their first characters, repeat the process in each new group. Since each character is used only once for sorting, the amortized running time is $$O(n)$$.

```python
def get_key(s, i):
    if i >= len(s):
        return 0
    return ord(s[i]) - ord('a') + 1


def counting_sort(a, p=0):
    k = 27
    b = ['' for _ in range(len(a))]
    c = [0 for _ in range(k)]
    for s in a:
        c[get_key(s, p)] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    r = c[:]
    for i in range(len(a) - 1, -1, -1):
        c[get_key(a[i], p)] -= 1
        b[c[get_key(a[i], p)]] = a[i]
    for i in range(1, k):
        if c[i] < r[i]:
            b[c[i]:r[i]] = counting_sort(b[c[i]:r[i]], p+1)
    return b
```

### 8-4 Water jugs

> Suppose that you are given $$n$$ red and $$n$$ blue water jugs, all of different shapes and sizes. All red jugs hold different amounts of water, as do the blue ones. Moreover, for every red jug, there is a blue jug that holds the same amount of water, and vice versa.

> Your task is to find a grouping of the jugs into pairs of red and blue jugs that hold the same amount of water. To do so, you may perform the following operation: pick a pair of jugs in which one is red and one is blue, fill the red jug with water, and then pour the water into the blue jug. This operation will tell you whether the red or the blue jug can hold more water, or that they have the same volume. Assume that such a comparison takes one time unit. Your goal is to find an algorithm that makes a minimum number of comparisons to determine the grouping. Remember that you may not directly compare two red jugs or two blue jugs.

> __*a*__. Describe a deterministic algorithm that uses $$\Theta(n^2)$$ comparisons to group the jugs into pairs.

Compare each red jug with each blue jug.

> __*b*__. Prove a lower bound of $$\Omega(n \lg n)$$ for the number of comparisons that an algorithm solving this problem must make.

$$
\begin{array}{rll}
n! &\le& 3^h \\
h &=& \Omega(n \lg n)
\end{array}
$$

> __*c*__. Give a randomized algorithm whose expected number of comparisons is $$O(n \lg n)$$, and prove that this bound is correct. What is the worst-case number of comparisons for your algorithm?

Random choose a red jug as pivot and partition blue rugs, and use the blue rug which is equal to the red rug as pivot and partition red rugs.

Worst case is $$O(n^2)$$.

```python
def partition(a, b, p, r):
    pos = random.randint(p, r - 1)
    i = p - 1
    for j in range(p, r):
        if b[j] <= a[pos]:
            i += 1
            b[i], b[j] = b[j], b[i]
            if b[i] == a[pos]:
                k = i
    b[i], b[k] = b[k], b[i]
    pos = i
    i = p - 1
    for j in range(p, r):
        if a[j] <= b[pos]:
            i += 1
            a[i], a[j] = a[j], a[i]
            if a[i] == b[pos]:
                k = i
    a[i], a[k] = a[k], a[i]
    return pos


def quick_sort(a, b, p, r):
    if p + 1 < r:
        q = partition(a, b, p, r)
        quick_sort(a, b, p, q)
        quick_sort(a, b, q + 1, r)
```

### 8-5 Average sorting

> Suppose that, instead of sorting an array, we just require that the elements increase on average. More precisely, we call an $$n$$-element array $$A$$ __*k-sorted*__ if, for all $$i=1,2, \dots,n-k$$, the following holds:

> $$
\frac{\sum_{j=i}^{i+k-1}A[j]}{k} \le \frac{\sum_{j=i+1}^{i+k}A[j]}{k}
$$

> __*a*__. What does it mean for an array to be 1-sorted?

Sorted.

> __*b*__. Give a permutation of the numbers $$1,2,\dots,10$$ that is 2-sorted, but not sorted.

1, 2, 1, 2, 1, 2

> __*c*__. Prove that an $$n$$-element array is $$k$$-sorted if and only if $$A[i] \le A[i + k]$$ for all $$i=1,2,\dots,n-k$$.

$$
\begin{array}{rll}
\displaystyle \frac{\sum_{j=i}^{i+k-1}A[j]}{k} &\le& \displaystyle \frac{\sum_{j=i+1}^{i+k}A[j]}{k} \\
\displaystyle \sum_{j=i}^{i+k-1}A[j] &\le& \displaystyle \sum_{j=i+1}^{i+k}A[j] \\
A[i] &\le& A[i + k]
\end{array}
$$

> __*d*__. Give an algorithm that $$k$$-sorts an $$n$$-element array in $$O(n \lg (n / k))$$ time.

We need to sort $$k$$ groups, each group has the same $$(i \mod k)$$. We can sort one group in $$O(n/k\lg (n/k))$$, to sort $$k$$ groups, it is $$O(n \lg (n/k)$$.

```python
def k_sort(a, k):
    for i in range(k):
        a[i:len(a):k] = sorted(a[i:len(a):k])
```

> We can also show a lower bound on the time to produce a $$k$$-sorted array, when $$k$$ is a constant.

> __*e*__. Show that we can sort a $$k$$-sorted array of length $$n$$ in $$O(n\lg k)$$ time.

Same as Exercise 6.5-9.

> __*f*__. Show that when $$k$$ is a constant, $$k$$-sorting an $$n$$-element array requires $$\Omega(n \lg n)$$ time.

$$
\Omega(n \lg n/k) = \Omega(n \lg n) 
$$

### 8-6 Lower bound on merging sorted lists

> The problem of merging two sorted lists arises frequently. We have seen a procedure for it as the subroutine MERGE in Section 2.3.1. In this problem, we will prove a lower bound of $$2n - 1$$ on the worst-case number of comparisons required to merge two sorted lists, each containing $$n$$ items.
First we will show a lower bound of $$2n - o(n)$$ comparisons by using a decision tree.

> __*a*__. Given $$2n$$ numbers, compute the number of possible ways to divide them into two sorted lists, each with $$n$$ numbers.

$$
\displaystyle \binom{2n}{n}
$$

> __*b*__. Using a decision tree and your answer to part (a), show that any algorithm that correctly merges two sorted lists must perform at least $$2n - o(n)$$ comparisons.

Based on Exercise C.1.13, 

$$
\begin{array}{rll}
\displaystyle \binom{2n}{n} &\le& \displaystyle 2^h \\
h &\ge& \displaystyle \lg\frac{(2n)!}{(n!)^2} \\
&=& \displaystyle \lg (2n!) - 2\lg (n!) \\
&=& \displaystyle \Theta(2n\lg 2n) - 2\Theta(n \lg n) \\
&=& \displaystyle \Theta(2n) \\
\end{array}
$$

> Now we will show a slightly tighter $$2n - 1$$ bound.

> __*c*__. Show that if two elements are consecutive in the sorted order and from different lists, then they must be compared.

We have to know the order of the two consecutive elements.

> __*d*__. Use your answer to the previous part to show a lower bound of $$2n - 1$$ comparisons for merging two sorted lists.

There are $$2n-1$$ pairs of consecutive elements.

### 8-7 The 0-1 sorting lemma and columnsort

$$\dots$$