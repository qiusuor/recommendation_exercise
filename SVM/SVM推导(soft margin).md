SVM（soft margin)

hinge loss:

$loss=max(0,1-y_i(Wx_i+b))$
令$\xi_i=1-y_i(Wx_i+b), \xi_i \ge0$
损失函数改为
$$
\left\{               \begin{array}{**lr**}               min_{W,b} \frac{1}{2}W^2 + C*\xi_i\\               s.t.  y_i(WX_i+b) \ge 1-\xi_i ,\ \xi_i \ge 0            \end{array}  \right.
$$



拉格朗日函数：

$L(W,b,\xi,\lambda,\mu)=\frac{1}{2}W^2+C\sum\limits_{i=1}^N\xi_i+\sum\limits_{i=1}^N\lambda_i(1-\xi_i-y_i(Wx_i+b))-\sum\limits_{i=1}^N\mu_i\xi_i$

强对偶定理同样成立，求解min问题，

对W求导，$W=\sum\limits_{i=0}^N\lambda_iy_ix_i$

对b求导，$\sum\limits_{i=0}^N\lambda_iy_i=0$

对$\xi_i$求导，$C-\lambda_i-\mu_i=0$

$\lambda_i \ge 0$

$ \mu_i \ge 0$

b的求解与hard margin类似，找一个非零的$\lambda_i,得到、\xi_i=C-\lambda_i,代入1-\xi_i-y_i(Wx_i+b)=0求解$。


代入整理，将问题转化为
$$
\left\{               \begin{array}{**lr**}               \underset{\lambda}{max}L=\sum\limits_{i=1}^N\lambda_i-\frac{1}{2}\sum\limits_{i=1}^N\sum\limits_{j=1}^{N}\lambda_i\lambda_jy_iy_jx_i^Tx_j  \\               s.t.  0 \le \lambda_i \le C,\ \sum\limits_{i=0}^N\lambda_iy_i=0             \end{array}  \right.
$$
用SMO算法求解$\lambda$即可。