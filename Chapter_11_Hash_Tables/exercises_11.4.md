## 11.4 Open addressing

### 11.4-1

> Consider inserting the keys $10, 22, 31, 4, 15, 28, 17, 88, 59$ into a hash table of length $m = 11$ using open addressing with the auxiliary hash function $h'(k) = k$. Illustrate the result of inserting these keys using linear probing, using quadratic probing with $c\_1 = 1$ and $c\_2 = 3$, and using double hashing with $h\_1(k) = k$ and $h\_2(k) = 1 + (k \~\text{mod}\~ (m - 1))$.

```python
m = 11


class LinearProbing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        while True:
            pos = (key + i) % m
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key


class QuadraticProbing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        while True:
            pos = (key + i + 3 * i * i) % m
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key


class DoubleHashing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        h2 = 1 + (key % (m - 1))
        while True:
            pos = (key + i * h2) % m
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key
```

Linear: [22, 88, None, None, 4, 15, 28, 17, 59, 31, 10]

Quadratic: [22, None, 88, 17, 4, None, 28, 59, 15, 31, 10]

Double: [22, None, 59, 17, 4, 15, 28, 88, None, 31, 10]


### 11.4-2

> Write pseudocode for HASH-DELETE as outlined in the text, and modify HASHINSERT to handle the special value DELETED.

```python
m = 5


class LinearProbing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        while True:
            pos = (key + i) % m
            if self.slots[pos] is None or self.slots[pos] == '[Deleted]':
                break
            i += 1
        self.slots[pos] = key

    def delete(self, key):
        global m
        i = 0
        while True:
            pos = (key + i) % m
            if self.slots[pos] is None:
                break
            if self.slots[pos] == key:
                self.slots[pos] = '[Deleted]'
                break
            i += 1
```

### 11.4-3

> Consider an open-address hash table with uniform hashing. Give upper bounds on the expected number of probes in an unsuccessful search and on the expected number of probes in a successful search when the load factor is 3/4 and when it is 7/8.

$\alpha=3/4$, unsuccessful: $\displaystyle\frac{1}{1-\frac{3}{4}} = 4$ probes, successful: $\displaystyle \frac{1}{\frac{3}{4}} \ln \frac{1}{1-\frac{3}{4}} \approx 1.848$ probes.

$\alpha=7/8$, unsuccessful: $\displaystyle\frac{1}{1-\frac{7}{8}} = 8$ probes, successful: $\displaystyle \frac{1}{\frac{7}{8}} \ln \frac{1}{1-\frac{7}{8}} \approx 2.377$ probes.

### 11.4-4 $\star$

> Suppose that we use double hashing to resolve collisions—that is, we use the hash function $h(k, i) = (h\_1(k) + ih\_2(k)) \~\text{mod}\~ m$. Show that if $m$ and $h\_2(k)$ have greatest common divisor $d \ge 1$ for some key $k$, then an unsuccessful search for key $k$ examines $(1/d)$th of the hash table before returning to slot $h\_1(k)$. Thus, when $d = 1$, so that $m$ and $h\_2(k)$ are relatively prime, the search may examine the entire hash table.

Suppose $d = \gcd(m, h\_2(k))$, the LCM $l = m \cdot h\_2(k) / d$.

Since $d | h\_2(k)$, then $m \cdot h\_2(k) / d \~\text{mod}\~ m = 0 \cdot (h\_2(k) / d \~\text{mod}\~ m) = 0$, therefore $(l + ih\_2(k)) \~\text{mod}\~ m = ih\_2(k) \~\text{mod}\~ m$, which means $ih\_2(k) \~\text{mod}\~ m$ has a period of $m/d$.

### 11.4-5 $\star$

> Consider an open-address hash table with a load factor $\alpha$. Find the nonzero value $\alpha$ for which the expected number of probes in an unsuccessful search equals twice the expected number of probes in a successful search. Use the upper bounds given by Theorems 11.6 and 11.8 for these expected numbers of probes.

$$
\frac{1}{1 - \alpha} = 2 \cdot \frac{1}{\alpha} \ln \frac{1}{1 - \alpha}
$$

$$
\alpha = 0.71533
$$
