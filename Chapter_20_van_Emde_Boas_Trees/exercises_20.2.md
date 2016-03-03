## 20.2 A recursive structure

### 20.2-1

> Write pseudocode for the procedures PROTO-VEB-MAXIMUM and PROTO-VEBPREDECESSOR.

```python
import math


class ProtoVEB:
    def __init__(self, u):
        self.u = u
        self.sqrt = int(math.sqrt(u))
        if self.is_leaf():
            self.a = [0, 0]
        else:
            self.summary = ProtoVEB(self.sqrt)
            self.cluster = []
            for _ in xrange(self.sqrt):
                self.cluster.append(ProtoVEB(self.sqrt))

    def is_leaf(self):
        return self.u == 2

    def high(self, x):
        return x / self.sqrt

    def low(self, x):
        return x % self.sqrt

    def index(self, x, y):
        return x * self.sqrt + y

    def member(self, x):
        if self.is_leaf():
            return self.a[x]
        return self.cluster[self.high(x)].member(self.low(x))

    def minimum(self):
        if self.is_leaf():
            if self.a[0]:
                return 0
            if self.a[1]:
                return 1
            return None
        min_idx = self.summary.minimum()
        if min_idx is None:
            return None
        offset = self.cluster[min_idx].minimum()
        return self.index(min_idx, offset)

    def maximum(self):
        if self.is_leaf():
            if self.a[1]:
                return 1
            if self.a[0]:
                return 0
            return None
        max_idx = self.summary.maximum()
        if max_idx is None:
            return None
        offset = self.cluster[max_idx].maximum()
        return self.index(max_idx, offset)

    def predecessor(self, x):
        if self.is_leaf():
            if self.a[0] == 1 and x == 1:
                return 0
            return None
        offset = self.cluster[self.high(x)].predecessor(self.low(x))
        if offset is not None:
            return self.index(self.high(x), offset)
        pred_idx = self.summary.predecessor(self.high(x))
        if pred_idx is None:
            return None
        offset = self.cluster[pred_idx].maximum()
        return self.index(pred_idx, offset)

    def successor(self, x):
        if self.is_leaf():
            if x == 0 and self.a[1] == 1:
                return 1
            return None
        offset = self.cluster[self.high(x)].successor(self.low(x))
        if offset is not None:
            return self.index(self.high(x), offset)
        succ_idx = self.summary.successor(self.high(x))
        if succ_idx is None:
            return None
        offset = self.cluster[succ_idx].minimum()
        return self.index(succ_idx, offset)

    def insert(self, x):
        if self.is_leaf():
            self.a[x] = 1
        else:
            self.summary.insert(self.high(x))
            self.cluster[self.high(x)].insert(self.low(x))

    def display(self, space=0, summary=False):
        if self.is_leaf():
            if summary:
                print(' ' * space + 'S ' + str(self.u) + ' ' + str(self.a))
            else:
                print(' ' * space + 'C ' + str(self.u) + ' ' + str(self.a))
        else:
            if summary:
                print(' ' * space + 'S ' + str(self.u))
            else:
                print(' ' * space + 'C ' + str(self.u))
            self.summary.display(space + 2, True)
            for c in self.cluster:
                c.display(space + 2)
```
### 20.2-2

> Write pseudocode for PROTO-VEB-DELETE. It should update the appropriate summary bit by scanning the related bits within the cluster. What is the worst-case running time of your procedure?

```python
    def delete(self, x):
        if self.is_leaf():
            self.a[x] = 0
        else:
            self.cluster[self.high(x)].delete(self.low(x))
            if self.cluster[self.high(x)].minimum() is None:
                self.summary.delete(self.high(x))
```

$$T(u) = 2T(\sqrt{u}) + \Theta(\lg \sqrt{u}) = \Theta(\lg u \lg \lg u)$$

### 20.2-3

> Add the attribute $$n$$ to each proto-vEB structure, giving the number of elements currently in the set it represents, and write pseudocode for PROTO-VEB-DELETE that uses the attribute $$n$$ to decide when to reset summary bits to 0. What is the worst-case running time of your procedure? What other procedures need to change because of the new attribute? Do these changes affect their running times?

```python
    def insert(self, x):
        if self.is_leaf():
            if self.a[x] == 0:
                self.a[x] = 1
                self.n += 1
                return True
            return False
        new_elem = self.cluster[self.high(x)].insert(self.low(x))
        if new_elem:
            self.n += 1
        self.summary.insert(self.high(x))
        return new_elem

    def delete(self, x):
        if self.is_leaf():
            if self.a[x] == 1:
                self.a[x] = 0
                self.n -= 1
                return True
            return False
        del_elem = self.cluster[self.high(x)].delete(self.low(x))
        if del_elem:
            self.n -= 1
        if self.cluster[self.high(x)].n == 0:
            self.summary.delete(self.high(x))
        return del_elem
```

Worst-case: $$T(u) = 2T(\sqrt{u}) + O(1) = \Theta(\lg n)$$



