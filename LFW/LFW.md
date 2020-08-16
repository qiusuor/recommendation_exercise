# LFW

基本思想：将user与item分别表示为一个向量，是UI矩阵分解的方式之一。

用途：

- 计算user的toplike
- 计算item的topsim
- 计算item的topic(对item向量聚类)



建模公式：

$p^{LFW}(u,i)=p_u^Tq_i=\sum \limits_{f=1}^{F}p_{uf}q_{if}$

loss function:

$loss=\sum \limits_{(u,i) \in D} (p(u,i)-p^{LFW}(u,i))^2 + \alpha |p_u|^2+\alpha|q_i|^2$



求偏导：

$\frac{\partial loss}{\part p_{uf}}=-2(p(u,i)-p^{LFW}(u,i))q_{if}+2\alpha p_{uf}$

$\frac{\partial loss}{\part q_{if}}=-2(p(u,i)-p^{LFW}(u,i))p_{uf}+2\alpha q_{if}$



梯度下降：

$p_{uf}=p_{uf}-\beta \frac{\part loss}{\part p_{uf}} $

$q_{if}=q_{if}-\beta \frac{\part loss}{\part q_{if}} $





负样本选取规则：充分展现而用户未点击的样本。

