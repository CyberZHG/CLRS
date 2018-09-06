## 10.2 Linked lists

### 10.2-1

> Can you implement the dynamic-set operation INSERT on a singly linked list
in $O(1)$ time? How about DELETE?

INSERT: $O(1)$.

DELETE: $O(n)$.

```python
class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def to_str(head):
    values = []
    head = head.next
    while head is not None:
        values.append(head.value)
        head = head.next
    return ' '.join(map(str, values))


def insert(head, x):
    new_node = LinkListNode(x)
    new_node.next = head.next
    head.next = new_node


def delete(head, x):
    while head is not None:
        if head.next is not None and head.next.value == x:
            head.next = head.next.next
        else:
            head = head.next
```

### 10.2-2

> Implement a stack using a singly linked list $L$. The operations PUSH and POP should still take $O(1)$ time.

```python
class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def push(head, x):
    new_node = LinkListNode(x)
    new_node.next = head.next
    head.next = new_node


def pop(head):
    if head.next is None:
        return None
    x = head.next.value
    head.next = head.next.next
    return x
```

### 10.2-3

> Implement a queue by a singly linked list $L$. The operations ENQUEUE and DEQUEUE should still take $O(1)$ time.

```python
class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = LinkListNode(None)

    def enqueue(self, x):
        new_node = LinkListNode(x)
        if self.tail.next is None:
            self.head = new_node
            self.tail.next = self.head
        else:
            self.head.next = new_node
            self.head = new_node

    def dequeue(self):
        if self.tail.next is None:
            return None
        x = self.tail.next.value
        self.tail = self.tail.next
        return x
```

### 10.2-4

> As written, each loop iteration in the LIST-SEARCH' procedure requires two tests: one for $x \ne L.nil$ and one for $x.key \ne k$. Show how to eliminate the test for $x \ne L.nil$ in each iteration.

```python
class LinkListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.nil = LinkListNode(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, x):
        x = LinkListNode(x)
        x.next = self.nil.next
        x.prev = self.nil
        x.next.prev = x
        x.prev.next = x

    def search(self, k):
        self.nil.key = k
        x = self.nil.next
        while x.key != k:
            x = x.next
        if x == self.nil:
            return None
        return x
```

### 10.2-5

> Implement the dictionary operations INSERT, DELETE, and SEARCH using singly linked, circular lists. What are the running times of your procedures?

INSERT $\Theta(n)$, DELETE $\Theta(n)$, SEARCH $\Theta(n)$.

```python
class LinkListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class Dict:
    def __init__(self):
        self.nil = LinkListNode(None, None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, key, value):
        x = self.search_node(key)
        if x is None:
            x = LinkListNode(key, value)
            x.next = self.nil.next
            x.prev = self.nil
            x.next.prev = x
            x.prev.next = x
        else:
            x.value = value

    def delete(self, key):
        x = self.search_node(key)
        if x is not None:
            x.next.prev = x.prev
            x.prev.next = x.next

    def search_node(self, key):
        self.nil.key = key
        x = self.nil.next
        while x.key != key:
            x = x.next
        if x == self.nil:
            return None
        return x

    def search(self, key):
        x = self.search_node(key)
        if x is None:
            return None
        return x.value
```

### 10.2-6

> The dynamic-set operation UNION takes two disjoint sets $S\_1$ and $S\_2$ as input, and it returns a set $S = S1 \cup S2$ consisting of all the elements of $S\_1$ and $S\_2$. The sets $S\_1$ and $S\_2$ are usually destroyed by the operation. Show how to support UNION in $O(1)$ time using a suitable list data structure.

```python
class LinkListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.nil = LinkListNode(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, key):
        x = LinkListNode(key)
        x.next = self.nil.next
        x.prev = self.nil
        x.next.prev = x
        x.prev.next = x

    def values(self):
        values = []
        x = self.nil.next
        while x != self.nil:
            values.append(x.key)
            x = x.next
        return values


def union(list_1, list_2):
    list_1.nil.next.prev = list_2.nil.prev
    list_2.nil.prev.next = list_1.nil.next
    list_1.nil.next = list_2.nil.next
    list_2.nil.next.prev = list_1.nil
    return list_1
```

### 10.2-7

> Give a $\Theta(n)$-time nonrecursive procedure that reverses a singly linked list of $n$ elements. The procedure should use no more than constant storage beyond that needed for the list itself.

```python
class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def to_list(head):
    values = []
    head = head.next
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


def insert(head, x):
    new_node = LinkListNode(x)
    new_node.next = head.next
    head.next = new_node


def reverse(head):
    prev = None
    node = head.next
    while node is not None:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
    head.next = prev
```

### 10.2-8 $\star$

> Explain how to implement doubly linked lists using only one pointer value $x.np$ per item instead of the usual two ($next$ and $prev$). Assume all pointer values can be interpreted as $k$-bit integers, and define $x.np$ to be $x.np = x.next$ XOR $x.prev$, the $k$-bit "exclusive-or" of $x.next$ and $x.prev$. (The value NIL is represented by 0.) Be sure to describe what information you need to access the head of the list. Show how to implement the SEARCH, INSERT, and DELETE operations on such a list. Also show how to reverse such a list in $O(1)$ time.

$head.np = next$

$tail.np = prev$

$next = x.np$ XOR $prev$

$prev = x.np$ XOR $next$

Reverse:

$head.np.np = (head$ XOR $head.np.np)$ XOR $tail$

$tail.np.np = (tail$ XOR $tail.np.np)$ XOR $head$

$head.np, tail.np = tail.np, head.np$
