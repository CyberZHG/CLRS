## Problems

### 6-1 Building a heap using insertion

> We can build a heap by repeatedly calling MAX-HEAP-INSERT to insert the elements into the heap. Consider the following variation on the BUILD-MAX-HEAP procedure:

> ```
BUILD-MAX-HEAP'(A)
1 A.heap-size = 1
2 for i = 2 to A.length
3     MAX-HEAP-INSERT(A, A[i])
```

> __*a*__. Do the procedures BUILD-MAX-HEAP and BUILD-MAX-HEAP' always create the same heap when run on the same input array? Prove that they do, or provide a counterexample.

No. 

For $$\left \langle 1, 2, 3, 4, 5, 6\right \rangle$$, 

BUILD-MAX-HEAP: $$\left \langle 6,4,5,1,3,2 \right \rangle$$;

BUILD-MAX-HEAP': $$\left \langle 6,5,3,4,2,1 \right \rangle$$.

> __*b*__. Show that in the worst case, BUILD-MAX-HEAP' requires $$\Theta(n\lg n)$$ time to build an n-element heap.

MAX-HEAP-INSERT is $$\Theta(\lg n)$$, thus BUILD-MAX-HEAP' is $$\Theta(n \lg n)$$.

### 6-2 Analysis of $$d$$-ary heaps

> A $$d$$-ary heap is like a binary heap, but (with one possible exception) non-leaf nodes have $$d$$ children instead of $$2$$ children.

> __*a*__. How would you represent a $$d$$-ary heap in an array?

If the index of the array begins with 0, then the $$k$$th children of node $$i$$ is $$id+k$$. The parent of node $$i$$ is $$\displaystyle \left \lfloor \frac{i - 1}{d} \right \rfloor$$.

Thus if the index begins with 1, the $$k$$th children is $$(i-1)d+k+1$$, the parent is $$\displaystyle \left \lfloor \frac{i-2}{d} \right \rfloor + 1$$.

> __*b*__. What is the height of a $$d$$-ary heap of $$n$$ elements in terms of $$n$$ and $$d$$?

$$\log_dn$$

> __*c*__. Give an efficient implementation of EXTRACT-MAX in a $$d$$-ary max-heap. Analyze its running time in terms of $$d$$ and $$n$$.

$$\Theta(d \log_dn)$$

```python
def parent(d, i):
    return (i - 1) / d


def child(d, i, k):
    return (i * d) + k


def max_heapify(d, a, i):
    max_idx = i
    for k in range(1, d + 1):
        c = child(d, i, k)
        if c < len(a) and a[c] > a[max_idx]:
            max_idx = c
    if max_idx != i:
        a[i], a[max_idx] = a[max_idx], a[i]
        max_heapify(d, a, max_idx)


def extract_max(d, a):
    assert(len(a) > 0)
    val = a[0]
    a[0] = a[-1]
    del a[-1]
    max_heapify(d, a, 0)
    return val
```

> __*d*__. Give an efficient implementation of INSERT in a $$d$$-ary max-heap. Analyze its running time in terms of $$d$$ and $$n$$.

$$\Theta(\log_dn)$$

```python
def increase_key(d, a, i, key):
    assert(key >= a[i])
    while i > 0 and key > a[parent(d, i)]:
        a[i] = a[parent(d, i)]
        i = parent(d, i)
    a[i] = key


def insert(d, a, key):
    a.append(-1e100)
    increase_key(d, a, len(a) - 1, key)
```

> __*e*__. Give an efficient implementation of INCREASE-KEY$$(A, i, k)$$, which flags an error if $$k < A[i]$$, but otherwise sets $$A[i] = k$$ and then updates the $$d$$-ary maxheap structure appropriately. Analyze its running time in terms of $$d$$ and $$n$$.

$$\Theta(\log_dn)$$

```python
def increase_key(d, a, i, key):
    assert(key >= a[i])
    while i > 0 and key > a[parent(d, i)]:
        a[i] = a[parent(d, i)]
        i = parent(d, i)
    a[i] = key
```
