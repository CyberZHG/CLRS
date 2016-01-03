## 11.4 Open addressing

### 11.4-1

> Consider inserting the keys $$10, 22, 31, 4, 15, 28, 17, 88, 59$$ into a hash table of length $$m = 11$$ using open addressing with the auxiliary hash function $$h'(k) = k$$. Illustrate the result of inserting these keys using linear probing, using quadratic probing with $$c_1 = 1$$ and $$c_2 = 3$$, and using double hashing with $$h_1(k) = k$$ and $$h_2(k) = 1 + (k ~\text{mod}~ (m - 1))$$.

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


