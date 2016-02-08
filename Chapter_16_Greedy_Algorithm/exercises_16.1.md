## 16.1 An activity-selection problem

### 16.1-1

> Give a dynamic-programming algorithm for the activity-selection problem, based on recurrence (16.2). Have your algorithm compute the sizes $$c[i, j]$$ as defined above and also produce the maximum-size subset of mutually compatible activities.
>
> Assume that the inputs have been sorted as in equation (16.1). Compare the running time of your solution to the running time of GREEDY-ACTIVITY-SELECTOR.

$$O(n^3)$$

### 16.1-2

> Suppose that instead of always selecting the first activity to finish, we instead select the last activity to start that is compatible with all previously selected activities. Describe how this approach is a greedy algorithm, and prove that it yields an optimal solution.

The same.

### 16.1-3

> Not just any greedy approach to the activity-selection problem produces a maximum-size set of mutually compatible activities. Give an example to show that the approach of selecting the activity of least duration from among those that are compatible with previously selected activities does not work. Do the same for the approaches of always selecting the compatible activity that overlaps the fewest other remaining activities and always selecting the compatible remaining activity with the earliest start time.

Least duration: [1, 5], [4, 7], [6, 10]

Overlap fewest: [1, 4], [5, 7], [8, 10], [1, 2], [3, 5], [6, 8], [9, 10], ...

Earliest start: [1, 6], [5, 10], [2, 4]

### 16.1-4

> Suppose that we have a set of activities to schedule among a large number of lecture halls, where any activity can take place in any lecture hall. We wish to schedule all the activities using as few lecture halls as possible. Give an efficient greedy algorithm to determine which activity should use which lecture hall.

> (This problem is also known as the __*interval-graph coloring problem*__. We can create an interval graph whose vertices are the given activities and whose edges connect incompatible activities. The smallest number of colors required to color every vertex so that no two adjacent vertices have the same color corresponds to finding the fewest lecture halls needed to schedule all of the given activities.)

Sort the intervals by start time, if the start time of one interval is the same as the finish time of the other interval, we should assume the finish time is less than the start time. From left to right, add 1 when there is a start time and subtract 1 when there is a finish time, the number of halls needed is the maximum number of the count.