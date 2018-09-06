## Problems

### 10-1 Comparisons among lists

> For each of the four types of lists in the following table, what is the asymptotic worst-case running time for each dynamic-set operation listed?

| |unsorted, singly linked|sorted, singly linked|unsorted, doubly linked|sorted, doubly linked|
|:-:|:-:|:-:|:-:|:-:|
|SEARCH$$(L,k)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|
|INSERT$$(L,x)$$|$$\Theta(1)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(n)$$|
|DELETE$$(L,x)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(1)$$|
|SUCCESSOR$$(L,x)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(n)$$|$$\Theta(1)$$|
|PREDECESSOR$$(L,x)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(1)$$|
|MINIMUM$$(L)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(n)$$|$$\Theta(1)$$|
|MAXIMUM$$(L)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|

### 10-2 Mergeable heaps using linked lists

> A mergeable heap supports the following operations: MAKE-HEAP (which creates an empty mergeable heap), INSERT, MINIMUM, EXTRACT-MIN, and UNION. Show how to implement mergeable heaps using linked lists in each of the following cases. Try to make each operation as efficient as possible. Analyze the running time of each operation in terms of the size of the dynamic set(s) being operated on.

> __*a*__. Lists are sorted.

MAKE-HEAP $$\Theta(1)$$, INSERT $$\Theta(n)$$, MINIMUM $$\Theta(1)$$, EXTRACT-MIN $$\Theta(1)$$, UNION $$\Theta(n)$$.

```python
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MergeableHeap:
    def __init__(self):
        self.head = None

    def to_list(self):
        values = []
        x = self.head
        while x is not None:
            values.append(x.value)
            x = x.next
        return values

    def insert(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            if value < self.head.value:
                new_node.next = self.head
                self.head = new_node
            else:
                x = self.head
                while x.next is not None and x.next.value < value:
                    x = x.next
                if x.next is None or x.next < value:
                    new_node.next = x.next
                    x.next = new_node

    def minimum(self):
        if self.head is None:
            return None
        return self.head.value

    def extract_min(self):
        if self.head is None:
            return None
        x = self.head.value
        self.head = self.head.next
        return x

    def union(self, other):
        head = LinkedListNode(None)
        x = head
        while self.head is not None or other.head is not None:
            if other.head is None:
                x.next = self.head
                self.head = self.head.next
            elif self.head is None:
                x.next = other.head
                other.head = other.head.next
            elif self.head.value <= other.head.value:
                x.next = self.head
                self.head = self.head.next
            else:
                x.next = other.head
                other.head = other.head.next
            if x.next.value != x.value:
                x = x.next
        x.next = None
        self.head = head.next
```

> __*b*__. Lists are unsorted.

MAKE-HEAP $$\Theta(1)$$, INSERT $$\Theta(1)$$, MINIMUM $$\Theta(n)$$, EXTRACT-MIN $$\Theta(n)$$, UNION $$\Theta(n)$$.

```python
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MergeableHeap:
    def __init__(self):
        self.head = None

    def to_list(self):
        values = []
        x = self.head
        while x is not None:
            values.append(x.value)
            x = x.next
        return values

    def insert(self, value):
        x = LinkedListNode(value)
        if self.head is None:
            self.head = x
        else:
            x.next = self.head
            self.head = x

    def minimum(self):
        if self.head is None:
            return None
        min_val = self.head.value
        x = self.head.next
        while x is not None:
            min_val = min(min_val, x.value)
            x = x.next
        return min_val

    def delete(self, value):
        prev = None
        x = self.head
        while x is not None:
            if x.value == value:
                if x == self.head:
                    self.head = self.head.next
                prev.next = x.next
            prev = x
            x = x.next

    def extract_min(self):
        x = self.minimum()
        self.delete(x)
        return x

    def union(self, other):
        if self.head is None:
            self.head = other.head
        else:
            x = self.head
            while x.next is not None:
                x = x.next
            x.next = other.head
```

> __*c*__. Lists are unsorted, and dynamic sets to be merged are disjoint.

Same as __*b*__.

### 10-3 Searching a sorted compact list

> __*a*__. Suppose that COMPACT-LIST-SEARCH$$(L, n, k)$$ takes $$t$$ iterations of the while loop of lines 2–8. Argue that COMPACT-LIST-SEARCH'$$(L, n, k, t)$$ returns the same answer and that the total number of iterations of both the for and while loops within COMPACT-LIST-SEARCH' is at least $$t$$.

> __*b*__. Argue that the expected running time of COMPACT-LIST-SEARCH'$$(L, n, k, t)$$ is $$O(t+\text{E}[X_t])$$.

> __*c*__. Show that $$\text{E}[X_t] \le \sum_{r=1}^n (1-r/n)^t$$.

> __*d*__. Show that $$\sum_{r=0}^{n-1} r^t \le n^{t+1}/(t+1)$$.

> __*e*__. Prove that $$\text{E}[X_t] \le n/(t+1)$$.

> __*f*__. Show that COMPACT-LIST-SEARCH'$$(L, n, k, t)$$ runs in $$O(t+n/t)$$ expected time.

> __*g*__. Conclude that COMPACT-LIST-SEARCH runs in $$O(\sqrt{n})$$ expected time.

> __*h*__. Why do we assume that all keys are distinct in COMPACT-LIST-SEARCH? Argue that random skips do not necessarily help asymptotically when the list contains repeated key values.
