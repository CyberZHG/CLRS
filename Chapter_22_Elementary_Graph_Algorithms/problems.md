## Problems

### 22-1 Classifying edges by breadth-first search

> A depth-first forest classifies the edges of a graph into tree, back, forward, and cross edges. A breadth-first tree can also be used to classify the edges reachable from the source of the search into the same four categories.

> __*a*__. Prove that in a breadth-first search of an undirected graph, the following properties hold:
> 1. There are no back edges and no forward edges.
> 2. For each tree edge $(u, v)$, we have $v.d = u.d + 1$.
> 3. For each cross edge $(u, v)$, we have $v.d = u.d$ or $v.d = u.d + 1$. 

> __*b*__. Prove that in a breadth-first search of a directed graph, the following properties hold:
> 1. There are no forward edges.
> 2. For each tree edge $(u, v)$, we have $v.d = u.d + 1$.
> 3. For each cross edge $(u, v)$, we have $v.d \le u.d + 1$.
> 4. For each back edge $(u, v)$, we have $0 \le v.d \le u.d$.

### 22-2 Articulation points, bridges, and biconnected components

> Let $G = (V, E)$ be a connected, undirected graph. An articulation point of $G$ is a vertex whose removal disconnects $G$. A bridge of $G$ is an edge whose removal disconnects $G$. A biconnected component of $G$ is a maximal set of edges such that any two edges in the set lie on a common simple cycle. Figure 22.10 illustrates these definitions. We can determine articulation points, bridges, and biconnected components using depth-first search. Let $G\_\pi = (V, E\_\pi)$ be a depth-first tree of $G$.

> __*a*__. Prove that the root of $G\_\pi$ is an articulation point of $G$ if and only if it has at least two children in $G\_\pi$.

At least two children => at least two components that are not connected.

> __*b*__. Let $v$ be a nonroot vertex of $G\_\pi$. Prove that $v$ is an articulation point of $G$ if and only if $v$ has a child $s$ such that there is no back edge from $s$ or any descendant of $s$ to a proper ancestor of $v$.

Connect to ancestor => loop.

> __*c*__. Let
> 
> $v.low = \min \left \\{ 
\begin{array}{l}
v.d,\\\\
w.d: (u, w) \~\text{is a back edge for some descendant}\~u\~\text{of}\~v
\end{array}
\right .$.

> Show how to computer $v.low$ for all vertices $v \in V$ in $O(E)$ time.

In DFS, for each edge, $v.low = min(v.low, w.d)$.

> __*d*__. Show how to compute all articulation points in $O(E)$ time.

(1) Root and have at least two children.

(2) Nonroot $u$ and there exist an edge $(u, v) \in E$ that $v.low >= u.d$.

> __*e*__. Prove that an edge of $G$ is a bridge if and only if it does not lie on any simple cycle of $G$.

No cycle => two components that are connected only by one edge.

> __*f*__. Show how to compute all the bridges of $G$ in $O(E)$ time.

$v.low > u.d$.

> __*g*__. Prove that the biconnected components of $G$ partition the nonbridge edges of $G$.

> __*h*__. Give an $O(E)$-time algorithm to label each edge $e$ of $G$ with a positive integer $e.bcc$ such that $e.bcc = e'.bcc$ if and only if $e$ and $e'$ are in the same biconnected component.

Delete bridges then DFS/BFS.

### 22-3 Euler tour

> An Euler tour of a strongly connected, directed graph $G = (V, E)$ is a cycle that traverses each edge of $G$ exactly once, although it may visit a vertex more than once.

> __*a*__. Show that $G$ has an Euler tour if and only if in-degree$(v)=$out-degree$(v)$ for each vertex $v \in V$.

Part 1 : To prove Euler tour exists ⇒ in-degree(v)=out-degree(v)

Euler tour can be decomposed into a set of edge-disjoint simple cycles, that when combined form the tour.
First, for each sub-cycle,  since they are simple edge-disjoint cycles, each vertex v in the cycle has one edge coming into it and one edge leading out of it. Therefore, in-degree(v)=out-degree(v) for each of the cycles. 
Second, for the entire graph, since an Euler tour exists, each simple cycle must be connected together, where each cycle has an edge coming in and an edge going out. 
Therefore, for each vertex v in the graph, in-degree(v)= out-degree(v).

Part 2: To prove in-degree(v)=out-degree(v) =>  Euler tour exists

Start from v, and chose any outgoing edge of v, say (v, u). Since in-degree(u) = out-degree(u) we can pick some outgoing edge of u and continue visiting edges. Each time we pick an edge, we can remove it from further consideration. At each vertex other than v, at the time we visit an entering edge, there must be an outgoing edge left unvisited, since in-degree = out-degree for all vertices. The only vertex for which there may not be an unvisited outgoing edge is v—because we started the cycle by visiting one of v’s outgoing edges. Since there’s always a leaving edge we can visit for any vertex other than v, eventually the cycle must return to v, thus proving the claim.

> __*b*__. Describe an $O(E)$-time algorithm to find an Euler tour of $G$ if one exists. (Hint: Merge edge-disjoint cycles.)

```
  1 //defined a Vertex in a strong-connected directed graph
  2 class Vertex{
  3     List<Vertex> nexts;
  4     List<Vertex> prevs;
  5 
  6     static boolean reachable(Vertex v, Vertex u){
  7         //return true only if exist a path from v - > u
  8         //can be implemented with BFS or DFS algorithm
  9     }
 10 
 11     List<Vertex> eulerTour(){
 12         List<Vertex> tour= new LinkedList<>();
 13 
 14         for(Vertex u : this.nexts){
 15             if(this.nexts.size() == 1 || reachable(u, this)){
 16                 tour.add(u);
 17                 this.nexts.remove(u);
 18                 tour.addAll(u.eulerTour());
 19             }
 20         }
 21 
 22         return tour;
 23     }
 24 }
```


### 22-4 Reachability

> Let $G = (V, E)$ be a directed graph in which each vertex $u \in V$ is labeled with a unique integer $L(U)$ from the set $\\{1, 2, \dots, |V|\\}$. For each vertex $u \in V$, let $R(u) = \\{v \in V: u \leadsto v \\}$ be the set of vertices that are reachable from $u$. Define $\min(u)$ to be the vertex in $R(u)$ whose label is minimum, i.e., $\min(u)$ is the vertex $v$ such that $L(v) = \min \\{L(w): w \in R(u) \\}$. Give an $O(V + E)$-time algorithm that computes $\min(u)$ for all vertices $u \in V$.

DFS from the minimum $L(U)$ in $G^T$.
