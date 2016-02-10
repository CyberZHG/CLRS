## 16.5 A task-scheduling problem as a matroid

### 16.5-1

> Solve the instance of the scheduling problem given in Figure 16.7, but with each penalty $$w_i$$ replaced by $$80 - wi$$.

| $$a_i$$ |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $$d_i$$ |  4 |  2 |  4 |  3 |  1 |  4 |  6 |
| $$w_i$$ | 10 | 20 | 30 | 40 | 50 | 60 | 70 |

$$\langle a_5, a_4, a_3, a_6, a_7 \rangle$$, $$w_1 + w_2 = 30$$.

### 16.5-2

> Show how to use property 2 of Lemma 16.12 to determine in time $$O(|A|)$$ whether or not a given set $$A$$ of tasks is independent.

Inserting by deadline.

