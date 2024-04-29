波動の問題、例えば
$$
\phi(x,t) = A\cos(kx-\omega t)
$$
という波の式を
$$
\phi(x,t) = A\exp[i(kx-\omega t)]
$$
と記載して計算し、最終的には実部のみをとり、物理量を得る。
ここで$k=\check{n}\omega/c$とすると
```math
\begin{aligned}
\phi(x,t) &= A\exp[i(\check{n}x\omega/c-\omega t)] \\
          &= A\exp[i\omega(\check{n}x/c-t)] \\
\end{aligned}
```
$\check{n}=n+i\kappa$とすると
```math
\begin{aligned}
\phi(x,t) &= A\exp[i\omega((n+i\kappa)x/c-t)] \\
          &= A\exp[i\omega(nx/c-t)-\omega\kappa x/c] \\
          &= A\exp[-\omega\kappa x/c]\exp[i\omega(nx/c-t)]
\end{aligned}
```
実際の物理量は実数部になるため、
```math
\begin{aligned}
\phi(x,t) &= \Re(A\exp[-\omega\kappa x/c]\exp[i\omega(nx/c-t)]) \\
          &= A\exp[-\omega\kappa x/c]\cos[\omega(nx/c-t)]
\end{aligned}
```
となる
2次元的に考えると、
$$
\phi(\boldsymbol{r},t) = A\cos(\boldsymbol{k} \cdot \boldsymbol{r}-\omega t)
$$
ここで$\boldsymbol{k}$,$\boldsymbol{r}$はベクトルである
$$
\phi(\boldsymbol{r},t) = A\cos(k_xx+k_yy-\omega t)
$$
ここで光がxy平面に入射するとして、x軸を界面方向、y軸を界面に垂直な方向とする。
屈折角を形式的に$\check{\theta}_t$の複素数形式でかくと
```math
\begin{aligned}
k_x &= |k|\sin\check{\theta}_t &= (\check{n}\omega/c)\sin\check{\theta}_t \\
k_y &= |k|\cos\check{\theta}_t &= (\check{n}\omega/c)\cos\check{\theta}_t
\end{aligned}
```
と成分分解できる。
ここでSnellの法則を$\sin\check{\theta}_t = \sin\theta_i/(n+i\kappa)$を代入すると
$$
k_x = (n+i\kappa)(\omega/c)\sin\check{\theta}_t = \frac{(n+i\kappa)\omega}{c(n+i\kappa)}\sin\theta_i = \frac{\omega}{c}\sin\theta_i
$$
と実数になるのに対して
$$
k_y = (n+i\kappa)(\omega/c)\cos\check{\theta}_t = (n+i\kappa)(\omega/c)(1-\sin^2\theta_t)^{1/2} = (n+i\kappa)(\omega/c)\biggl(1-\frac{(n-i\kappa)^2\sin^2\theta_i}{(n^2+\kappa^2)^2}\biggr)^{1/2}
$$
と複素数になる。そこで$k_x=k'_x$、$k_y=k'_y+ik''_y$とすると
$$
\phi(\boldsymbol{r},t) = A\exp[i(\boldsymbol{k}\cdot\boldsymbol{r}-\omega t)]=A\exp[i(k'_xx+k'_yy+ik''_yy-\omega t)] = A\exp(-k''_yy)\exp[i(k'_xx+k'_yy-\omega t)]
$$
実数部をとると
$$
\phi(\boldsymbol{r},t) = A\exp(-k''_yy)\cos[i(k'_xx+k'_yy-\omega t)]
$$
となる。
故に、波の進行方向は$(k'_x,k'_y)$の実数部のみに影響して虚数部の$k''_y$は減衰量のみに影響を与える。
