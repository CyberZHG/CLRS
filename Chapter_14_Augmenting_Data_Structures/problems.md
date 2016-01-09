## Problems

### 14-1 Point of maximum overlap

> Suppose that we wish to  keep track of a point of maximum overlap in a set of intervals - a point with the largest number of intervals in the set that overlap it.

> __*a*__. Show that there will always be a point of maximum overlap that is an endpoint of one of the segments.

> __*b*__. Design a data structure that efficiently supports the operations INTERVAL-INSERT, INTERVAL-DELETE, and FIND-POM, which returns a point of maximum overlap.

### 14-2 Josephus permutation

> We define the __*Josephus problem*__ as follows. Suppose that $$n$$ people form a circle and that we are given a positive integer $$m \ge n$$. Beginning with a designated first person, we proceed around the circle, removing every $$m$$th person. After each person is removed, counting continues around the circle that remains. This process continues until we have removed all $$n$$ people. The order in which the people are removed from the circle defines the __*$$(n,m)$$-Josephus permutation*__ of the integers $$1,2, \dots ,n$$. For example, the $$(7, 3)$$-Josephus permutation is $$\langle 3, 6, 2, 7, 5, 1, 4 \rangle$$.

> __*a*__. Suppose that $$m$$ is a constant. Describe an $$O(n)$$-time algorithm that, given an integer $$n$$, outputs the .$$(n,m)$$-Josephus permutation.

> __*b*__. Suppose that $$m$$ is not a constant. Describe an $$O(n \lg n)$$-time algorithm that, given integers $$n$$ and $$m$$, outputs the $$(n,m)$$-Josephus permutation.
