## 16.5 A task-scheduling problem as a matroid

### 16.5-1

> Solve the instance of the scheduling problem given in Figure 16.7, but with each penalty $w\_i$ replaced by $80 - wi$.

| $a\_i$ |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $d\_i$ |  4 |  2 |  4 |  3 |  1 |  4 |  6 |
| $w\_i$ | 10 | 20 | 30 | 40 | 50 | 60 | 70 |

$\langle a\_5, a\_4, a\_3, a\_6, a\_7 \rangle$, $w\_1 + w\_2 = 30$.

### 16.5-2

> Show how to use property 2 of Lemma 16.12 to determine in time $O(|A|)$ whether or not a given set $A$ of tasks is independent.

Inserting by deadline.
