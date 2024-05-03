# Optical Simulation 4
## Snellの法則
```math
\Re(\check{n}_i)\sin\theta_i = \Re(\check{n}_j)\sin\theta_j
```
ここで$`\check{n}`$は複素屈折率、$`\Re()`$は実数部を示す
（詳しくは[「物性なんでも Q&A」第 2 回](https://home.sato-gallery.com/research/crystal_letters_nandemoQA(2).pdf)参照）
## 光学アドミッタンス
```math
\eta_j=\begin{cases}
    \dfrac{n_j}{\mu_0c}\cos\phi_j & \text{s偏光}　\\
    \dfrac{n_j}{\mu_0c\cos\phi_j} & \text{p偏光}
\end{cases}
```
ここで$`\mu_0`$は真空の透磁率、$`c`$は光速を示す。

Snellの式を適用して、入射角を$'\theta'$とすると
```math
\cos\phi_j = \bigl(1-\sin^2\phi\bigr)^{1/2} = \biggl(1-\frac{n_0^2}{n_j^2}\sin^2\theta\biggr)^{1/2} = \frac{(n_j^2-n_0^2\sin^2\theta)^{1/2}}{n_j}
```
なので
```math
\eta_j=\begin{cases}
\dfrac{(n_j^2-n_0^2\sin^2\theta)^{1/2}}{\mu_0c} & \text{s偏光}　\\
\dfrac{n_j^2}{\mu_0c(n_j^2-n_0^2\sin^2\theta)^{1/2}} & \text{p偏光}
\end{cases}
```
## 位相差
```math
\delta_j = \frac{2\pi n_j d_j\cos\phi_j}{\lambda}=\frac{2\pi d_j(n_j^2-n_0^2\sin^2\theta)^{1/2}}{\lambda}
``` 
## マトリクス法
``` math
M_j =
    \begin{pmatrix}
    \cos\delta_j & \dfrac{i}{\eta_j}\sin\delta_j\\
    i\eta_j\sin\delta_j & \cos\delta_j
    \end{pmatrix}
```
で示される特性マトリクスを用いて
``` math
\left(
    \begin{matrix}
    B \\
    C
    \end{matrix}
\right) 
= \prod_{j=1^{m}} M_j
\left(
    \begin{matrix}
    1 \\
    \eta_{sub}
    \end{matrix}
\right) 
```
にて計算
## 反射率
```math
R=\biggl|\frac{\eta_0B-C}{\eta_0B+C}\biggr|^2
```

## 透過率
```math
T=\frac{4\eta_0\Re(\eta_s)}{|\eta_0B+C|^2}
```

## 参考
[任意の屈折率を持つ層からなる光学多層膜フィルタの最適設計](http://surf.ml.seikei.ac.jp/fopt/Kougaku-Houkoku.pdf)