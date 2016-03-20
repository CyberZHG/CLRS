## 24.2 Single-source shortest paths in directed acyclic graphs

### 24.2-1

> Run DAG-SHORTEST-PATHS on the directed graph of Figure 24.5, using vertex $$r$$ as the source.

|\|$$r$$|$$s$$|$$t$$|$$x$$|$$y$$|$$z$$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|$$d$$|0|5|3|10|7|5|
|$$\pi$$|NIL|$$r$$|$$r$$|$$t$$|$$t$$|$$t$$|

### 24.2-2

> Suppose we change line 3 of DAG-SHORTEST-PATHS to read 
> 
> 3  __for__ the first $$|V| - 1$$ vertices, taken in topologically sorted order
> 
> Show that the procedure would remain correct.

The out-degree of the last vertex is 0.

### 24.2-3

> The PERT chart formulation given above is somewhat unnatural. In a more natural structure, vertices would represent jobs and edges would represent sequencing constraints; that is, edge $$(u, v)$$ would indicate that job $$u$$ must be performed before job $$v$$. We would then assign weights to vertices, not edges. Modify the DAG-SHORTEST- PATHS procedure so that it finds a longest path in a directed acyclic graph with weighted vertices in linear time.

$$s.d = s.w$$, $$w(u, v) = v.w$$.

### 24.2-4

> Give an efficient algorithm to count the total number of paths in a directed acyclic graph. Analyze your algorithm.

$$s.num = 1$$, $$v.num = \sum_{(u, v) \in E} u.num$$.

Time: $$\Theta(V + E)$$.
