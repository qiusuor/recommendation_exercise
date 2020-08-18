# Personal Rank

**思想：**将user与item之间的关系表示为二分图，用user节点与item节点的连通程度表示相关性。

![1597719969349](C:\Users\75043\Desktop\recommendation_exercise\PersonRank\1597719969349.png)





计算其他item对某个user的重要程度（相关性）的方法：

![1597720193259](C:\Users\75043\Desktop\recommendation_exercise\PersonRank\1597720193259.png)



公式化描述：

![1597720230096](C:\Users\75043\Desktop\recommendation_exercise\PersonRank\1597720230096.png)

其中，$PR(v)$表示节点$v$与$v_A$的重要程度（相关性）。



矩阵化描述：

![1597720554861](C:\Users\75043\Desktop\recommendation_exercise\PersonRank\1597720554861.png)

解释：

$m 个 user,n个item$

$r_0:(m+n,1),one-hot 表示选择某个顶点作为基准$

$r:(m+n,1),选定某个顶点后,其余顶点对该顶点的重要程度$

$M:(m+n,m+n)， 转移矩阵$

