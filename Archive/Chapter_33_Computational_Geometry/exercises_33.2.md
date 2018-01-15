## 33.2 Determining whether any pair of segments intersects

### 33.2-1

> Show that a set of $$n$$ line segments may contain $$\Theta(n ^ 2)$$ intersections.

Star.

### 33.2-2

> Given two segments $$a$$ and $$b$$ that are comparable at $$x$$, show how to determine in $$O(1)$$ time which of $$a \succeq_x b$$ or $$b \succeq_x a$$ holds. Assume that neither segment is vertical. 

Suppose $$a = \overline{(x_1, y_1)(x_2, y_2)}$$ and $$b = \overline{(x_3, y_3)(x_4, y_4)}$$,

$$
\frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1}
$$

$$
y = (x - x_1) \cdot \frac{y_2 - y_1}{x_2 - x_1} + y_1
$$

$$
y' = (x - x_3) \cdot \frac{y_4 - y_3}{x_4 - x_3} + y_3
$$

Compare $$y$$ and $$y'$$. To avoid division, compare $$(x_2 - x_1) \cdot y$$ and $$(x_4 - x_3) \cdot y'$$.

### 33.2-3

> Professor Mason suggests that we modify ANY-SEGMENTS-INTERSECT so that instead of returning upon finding an intersection, it prints the segments that intersect and continues on to the next iteration of the __for__ loop. The professor calls the resulting procedure PRINT-INTERSECTING-SEGMENTS and claims that it prints all intersections, from left to right, as they occur in the set of line segments. Professor Dixon disagrees, claiming that Professor Mason's idea is incorrect. Which professor is right? Will PRINT-INTERSECTING-SEGMENTS always find the leftmost intersection first? Will it always find all the intersections?

No.

No.

### 33.2-4

> Give an $$O(n \lg n)$$-time algorithm to determine whether an n-vertex polygon is simple.

Same as ANY-SEGMENTS-INTERSECT.

### 33.2-5

> Give an $$O(n \lg n)$$-time algorithm to determine whether two simple polygons with a total of $$n$$ vertices intersect.

Same as ANY-SEGMENTS-INTERSECT.

### 33.2-6

> A __*disk*__ consists of a circle plus its interior and is represented by its center point and radius. Two disks intersect if they have any point in common. Give an $$O(n \lg n)$$- time algorithm to determine whether any two disks in a set of $$n$$ intersect.

Same as ANY-SEGMENTS-INTERSECT.

### 33.2-7

> Given a set of $$n$$ line segments containing a total of $$k$$ intersections, show how to output all $$k$$ intersections in $$O((n + k) \lg)$$ time.

Treat the intersection points as event points.

### 33.2-8

> Argue that ANY-SEGMENTS-INTERSECT works correctly even if three or more segments intersect at the same point.

### 33.2-9

> Show that ANY-SEGMENTS-INTERSECT works correctly in the presence of vertical segments if we treat the bottom endpoint of a vertical segment as if it were a left endpoint and the top endpoint as if it were a right endpoint. How does your answer to Exercise 33.2-2 change if we allow vertical segments?
