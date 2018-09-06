## Problems

### 14-1 Point of maximum overlap

> Suppose that we wish to  keep track of a point of maximum overlap in a set of intervals - a point with the largest number of intervals in the set that overlap it.

> __*a*__. Show that there will always be a point of maximum overlap that is an endpoint of one of the segments.

> __*b*__. Design a data structure that efficiently supports the operations INTERVAL-INSERT, INTERVAL-DELETE, and FIND-POM, which returns a point of maximum overlap.

### 14-2 Josephus permutation

> We define the __*Josephus problem*__ as follows. Suppose that $n$ people form a circle and that we are given a positive integer $m \ge n$. Beginning with a designated first person, we proceed around the circle, removing every $m$th person. After each person is removed, counting continues around the circle that remains. This process continues until we have removed all $n$ people. The order in which the people are removed from the circle defines the __*$(n,m)$-Josephus permutation*__ of the integers $1,2, \dots ,n$. For example, the $(7, 3)$-Josephus permutation is $\langle 3, 6, 2, 7, 5, 1, 4 \rangle$.

> __*a*__. Suppose that $m$ is a constant. Describe an $O(n)$-time algorithm that, given an integer $n$, outputs the $(n,m)$-Josephus permutation.

Use doubly linked list, the time is $O(nm)$, since $m$ is a constant, $O(nm)$ = $O(n)$.

```python
class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        x = LinkedListNode(key)
        if self.head is None:
            self.head = x
            x.next = x
            x.prev = x
        else:
            x.prev = self.head.prev
            x.next = self.head
            x.prev.next = x
            x.next.prev = x

    def remove(self):
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next

    def forward(self, step):
        while step > 0:
            step -= 1
            self.head = self.head.next


def josephus_permutation(n, m):
    lst = LinkedList()
    for i in xrange(1, n + 1):
        lst.insert(i)
    perm = []
    while lst.head is not None:
        lst.forward(m - 1)
        perm.append(lst.head.key)
        lst.remove()
    return perm
```

> __*b*__. Suppose that $m$ is not a constant. Describe an $O(n \lg n)$-time algorithm that, given integers $n$ and $m$, outputs the $(n,m)$-Josephus permutation.

Build a balanced binary search tree in $O(n \lg n)$, maintain $size$ to support order-statistics. In each iteration, we select and delete the $(r + m - 1) \~\text{mod}\~ T.root.size + 1$th element.

```python
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.color = BLACK
        self.size = 1
        self.p = None
        self.left = left
        self.right = right
        if left is not None:
            left.p = self
            self.size += left.size
        if right is not None:
            right.p = self
            self.size += right.size


class BinarySearchTree:
    def __init__(self, a):
        self.root = self.build(a, 0, len(a))

    def build(self, a, l, r):
        if l >= r:
            return None
        mid = (l + r) // 2
        return TreeNode(a[mid], self.build(a, l, mid), self.build(a, mid+1, r))

    def get_size(self, x):
        if x is None:
            return 0
        return x.size

    def update_size(self, x):
        if x is not None:
            x.size = 1 + self.get_size(x.left) + self.get_size(x.right)

    def select(self, x, i):
        r = self.get_size(x.left) + 1
        if i == r:
            return x
        elif i < r:
            return self.select(x.left, i)
        else:
            return self.select(x.right, i - r)

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            p = y.p
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            while p != z and p != y:
                self.update_size(p)
                p = p.p
            self.update_size(y)
        while z.p is not None:
            z = z.p
            self.update_size(z)


def josephus_permutation(n, m):
    tree = BinarySearchTree(range(1, n + 1))
    perm = []
    rank = 0
    while n > 0:
        rank = (rank + m - 1) % n
        x = tree.select(tree.root, rank + 1)
        perm.append(x.key)
        tree.delete(x)
        n -= 1
    return perm
```
