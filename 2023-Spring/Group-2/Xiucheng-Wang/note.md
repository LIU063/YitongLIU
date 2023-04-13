<p id="table"></p>

## Table of Contents

- <a href="#1">Week 1 (2023.03.17 – 2023.03.23)</a>
- <a href="#2">Week 2 (2023.03.24 – 2023.03.30)</a>
- <a href="#3">Week 3 (2023.03.31 – 2023.04.06)</a>
- <a href="#4">Week 4 (2023.04.07 – 2023.04.13)</a>

<br/>

------

<br/>

<p id="1"></p>

# <a href="#table">Week 1 (2023.03.17 – 2023.03.23)</a>
## 修改pimrc论文


<br/>

<p id="2"></p>

# <a href="#table">Week 2 (2023.03.24 – 2023.03.30)</a>

## Server-Free Edge Computing 
### 1.0——全局时延最优
![图片](./assets/serverless.svg)

传统的Edge Computing (EC)多为server-user架构，user处有一个或多个task要处理，server提供算力为多个用户提供服务。

本文拟研究ServerLess EC (SLEC)问题，即总共有N个用户，每个用户 $i$ 都有一定的算力 $f_i$，并有一个大小为 $d_i$ 的任务需要处理。这样假设邻居用户算力十分充沛。一个节点可以将其任务全部传递给该邻居用户处理，并利用自己空闲的算力处理他自己的其他邻居节点的任务，从而实现全局任务的快速处理。

1. 由于通信距离的限制，每个用户都只能和其距离小于 $r$ 的用户直接通信。
2. 用户间信息传输速率与用户间的距离 $l$ 成平方反比，通信时延为 $T_{tra}=\frac{d}{\log_2 (1+\frac{s}{l^2})}$，其中$s$为单位距离信噪比，可以认为是一个常数。
3. 每个任务的处理时延为任务大小除以计算资源大小 $T_{com}=\frac{d}{f}$。
4. 用户可以将自己的任务按任意比例分成任意多份，并传递给不同的直接相连的用户或在自己本地处理该任务。
5. 用户 $i$ 可以选择利用 $f_{i,i}$ 的计算资源，来处理 $d_{i,i}$ 比例的自身任务，并将 $1-d_{i,i}$比例的任务传递给其他用户去处理，以及拿出 $f_{i}-f_{i,i}$ 比例的计算资源来处理其他用户传递过来的任务。这样其本地计算自身没有传递出去的任务的时延为 $\frac{d_{i,i}}{f_{i,i}}$。
   
这样所有用户的计算时延为

$\min_{\mathbf{f,d}}\sum_{i=1}^{N}\sum_{j\in\mathcal{N}(i)\bigcup\{i\}}\frac{d_{i,j}}{\log_2 (1+\frac{s}{l_{i,j}^2})}+\frac{d_{i,j}}{f_{i,j}}$

$s.t. \sum_{j\in\mathcal{N}(i)\bigcup\{i\}}d_{i,j}=d_{i}\qquad \forall i \in\{1,\cdots N\}$

$\sum_{j\in\mathcal{N}(i)\bigcup\{i\}}f_{i,j}\leq f_{i}\qquad \forall i \in\{1,\cdots N\}$

$d_{i,j}\geq 0$

$f_{i,j}\geq 0$

其中 $l_{i,j}$ 为节点 $i$ 与节点 $j$ 之间的距离，我们定义 $\frac{d_{i,i}}{\log_2 (1+\frac{s}{l_{i,i}^2})}$ 为 0。

### 2.0——全局花销最优

1. 由于通信距离的限制，每个用户都只能和其距离小于 $r$ 的用户直接通信。
2. 用户间信息传输速率与用户间的距离 $l$ 成平方反比，通信时延为 $T_{tra}=\frac{d}{\log_2 (1+\frac{s}{l^2})}$，其中$s$为单位距离信噪比，可以认为是一个常数。
3. 每个任务的处理时延为任务大小除以计算资源大小 $T_{com}=\frac{d}{f}$。
4. 用户可以将自己的任务按任意比例分成任意多份，并传递给不同的直接相连的用户或在自己本地处理该任务。
5. 由于不同用户的计算资源大小$f_i$不一样，因此不同用户的单位计算成本 $c_i$ 也不一样。
6. 用户 $i$ 可以选择利用 $x_{f,i}^{i}$ 比例的计算资源，来处理 $x_{d,i}^{i}$ 比例的自身任务，并将 $1-x_{d,i}^{i}$ 比例的任务传递给其他用户去处理，以及拿出 $1-x_{f,i}^{i}$ 比例的计算资源来处理其他用户传递过来的任务。这样其本地计算自身没有传递出去的任务的时延为 $\frac{d_ix_{d,i}^{i}}{x_{f,i}^{i}f_i}$。
7. 如果用户把自身任务传递给其他用户去处理，其需要支付一定价格去购买
8. 用户自己执行自己任务的所付出的代价为 $c_i\frac{d_ix_{d,i}^{i}}{x_{f,i}^{i}f_i}$ 。
9. 我们定义用户 $i$ 将自身任务传递给用户 $j$ 的传输时延成本为 $c^{t}\frac{d_ix_{d,j}^{i}}{\log_2\left(1+\frac{s}{l_{i,j}^2}\right)}$ ，其中 $x_{d,j}^{i}$ 为将任务 $i$ 传递给用户$j$的比例，$l_{i,j}$为用户$i$ 与用户$j$之间的距离。
10. 对于用户 $i$ ，如果其将 $f_i(1-x_{f,i}^{i})$ 的计算资源拿去给其邻居节点接外包赚差价。如果其所有邻居购买的计算资源之和不大于$ f_i(1-x_{f,i}^{i})$ ，那么按其所出价格分配计算资源。如果所有邻居购买的计算资源大于 $f_i(1-x_{f,i}^{i})$ ，那么依据其所出价格，按比例分配计算资源。例如共有 $N$ 个用户购买其资源，如果购买总量不大于 $c_if_i(1-x_{f,i}^{i})$ ，则用户$k$购得的来自用户 $i$ 的计算资源为 $\frac{p_k}{c_i}$ 。那么用户$k$总计付出的成本为$p_k \frac{p_k}{c_i}\frac{d_kx_{d,i}^{k}}{x_{f,i}^{k}f_i}$，其中 $p_{k,i}$ 为用户 $k$ 为购买用户 $i$ 的单位计算资源付出钱。
11. 如果出资总价高于 $c_if_i(1-x_{f,i}^{i})$ ，那么每个用户 $k$ 得到的资源为 $\frac{p_{k,i}}{\sum_{o=1}^{N}p_{o,i}}f_i(1-x_{f,i}^{i})$ 。

## VoI

对于hole不发生变化的训练，sender和controller的state都只有当前人物的位置，区别在于sender的action是传与不传，controller的action是控制运动方向。两个agent的reward都是一样的，即距离+不掉进去。

### 1.0 版本
1. sender如果在初始时刻需要将state传送给controller，以开始游戏
2. 如果sender传输当前的state，那么sender要至少间隔N个step才能再次传输
3. controller获知sender传输的state也有N个step的时延，controller在接受到sender发送的state后，可以调整运动方向，也可以不调整。无论运动方向是否调整，直到下一次controller决策前，人物向都沿着controller决策后的方向一直运动。
4. controller预先训练好，sender基于训练好的controller决定传与不传。
   

### 1.2 版本
1. sender与controller同时初始化，sender基于controller会怎么传决定怎么控制，controller根据sender会怎么控制来决定传不传。（我估计得类似交替迭代更新的方式，比如先更新sender一段时间，再更新controller一段时间。或者参考GAN是怎么联合train出来的）

### 2.0 完整版
1. controller需要去应对多种冰窟窿的分布，因此对于sender而言state应该是包括了当前人物位置与其观测到的冰窟窿的位置。
2. 这时sender应该传递一个矩阵，矩阵中置1的元素表示当前人物的位置，置2的表示冰窟窿的位置，3表示目标点，0表示普通节点，4表示unknown。
3. sender如果传全部的数据，需要等N个step后才能再传，controller也同样要等N个step后才能得知消息。但是如果sender只传人物周围半径为r的数据，那么只需要等$\alpha$N个step后就能再传，controller也同样只要等$\alpha$N个step后就能得知消息。
4. 这样sender相当于做一个pomdp

<br/>

<p id="3"></p>

# <a href="#table">Week 3 (2023.03.31 – 2023.04.06)</a>

## 撰写DTRL Magazine
## 视频传输问题
### 问题定义
定义$x_{i}^{j}$为从节点$i$流向节点$j$的视频流速率，$\mathcal{E}$为网络中所有边的集合，$\mathcal{V}$为网络中所有节点的集合，其中$\mathcal{V}_s$和$\mathcal{V}_d$分别表示网络中视频源节点和视频目的节点的集合。规定$e_{i}^{j}$为网络节点$i,j$之间已知的最大容量，$r_j$为目的节点$j$对清晰度的要求，$hop(i,j)$为节点$i$与节点$j$之间的最小路径跳数，$h_{max}$为已知的最大跳数值。
具体优化问题如下：

$min_{x} \sum_{(i,j)\in\mathcal{E}}x_{i}^{j}\qquad (1)$

$s.t.\qquad \max_{i} x_{i}^{j}\geq \max_{k}x_{j}^{k}\qquad \forall j \in \mathcal{V}\wedge\forall i\in \mathcal{N}(j)\wedge\forall k\in \mathcal{N}(j)\qquad (1a)$

$\max_{i} x_{i}^{j} \geq r_{j},\qquad \forall j \in \mathcal{V}_{d} \qquad (1b)$

$\max_{j} x_{i}^{j}\geq \max_{j} r_{j}, \qquad i \in \mathcal{V}_{s}\qquad (1c)$

$x_{i}^{j}\leq e_{i}^{j},\qquad \forall (i,j)\in \mathcal{E}\qquad(1d)$

$hop(i,j)\leq h_{max},\qquad  \forall i \in \mathcal{V}_s\wedge\forall j \in \mathcal{V}_d\qquad (1e) $

约束(1a)保证了对于任意节点$j$其流入的视频清晰度不能高于其流出的视频清晰度。
约束(1b)保证了目的节点的流入视频清晰度，需要满足其清晰度需求。
约束(1c)保证了源节点流出的最大视频清晰度，要大于所有用户中最大的清晰度需求。
约束(1d)保证了节点$i$与节点$j$之间的可传输的视频流清晰度不能大于链路的最大传输容量。
约束(1e)保证了用户节点和源节点之间的最短路径的跳数不能超过$h_{max}$，也就是所有数据必须要在$h_{max}$内传输到目的节点。

### 问题求解
已用动态规划解决


# <a href="#table">Week 4 (2023.04.07 – 2023.04.13)</a>
## 修改DTRL Magazine

## VoI
可以将sender传输次数从12次缩减到6次，依然可以在4*10的范围，4个hole的条件下，以最短的次数(12步)走到goal

## 视频传输
1. 对问题做了进一步的改进，加上了VR FoV的问题，也就是假设多个用户同时请求一个VR视频，但是他们观看时间、观看区域、观看清晰度都不相同(相当于用户约束从一维变三维)，最小化总传输成本
2. 动态规划可以找到最优解，同时用贪心的方式以O(MN)的复杂度实现了最优解99.5%的性能，甚至在很多情况下，贪心的解和最优解完全一样。(看不懂，但是大受震撼)

### 问题一

#### 问题

---

定义$x_i^j$为从节点$i$流向节点$j$的视频流速率，$\mathcal E$ 为网络中所有边的集合，$\mathcal V$为网络中所有节点的集合，其中$\mathcal V_s$和$\mathcal V_d$分别表示网络中视频源节点和视频目的节点的集合。规定$e_i^j$为网络节点$i,j$之间已知的最大容量，$r_j$为目的节点$j$对清晰度的要求，$hop(i,j)$为节点$i$与节点$j$之间的最小路径跳数，$h_{max}$为已知的最大跳数值。

优化目标函数：
$$
min_x\sum\limits_{(i,j)\in\mathcal{E}}x_i^j \tag 1
$$
约束条件：
$$
\underset i{\max}x_i^j \ge \underset k{\max}x_j^k \ \ \ \ \  \forall j \in \mathcal{V},\forall i \in \mathcal{N}(j),\forall k \in \mathcal{N}(j) \tag{1a}
$$

$$
\underset i{\max}x_i^j\ge r_j \ \ \ \ \  \forall j \in \mathcal{V}_d \tag{1b}
$$

$$
\underset j{\max}x_i^j \ge \underset j{\max}r_j \ \ \ \ \ \forall i \in \mathcal{V}_s \tag{1c}
$$

$$
x_i^j\le e_i^j \ \ \ \ \ \forall (i,j) \in \mathcal{E}\tag{1d}
$$

$$
hop(i,j)\le h_{max} \ \ \ \ \ \forall i \in \mathcal{V}_x,\forall j \in \mathcal{V}_d\tag{1e}
$$



#### 求解

---

##### 视频源节点唯一的情况

- 命题1：

  ​		只考虑有流量的边，即$ x_i^j>0,(i,j)\in\mathcal E$，这些边组成了一棵以视频源节点为根节点，所有叶节点均为目的节点的树，其中每条边上的流量方向为从根节点向叶节点的方向，即深度增加的方向。

  证明：

  - 显然上述这棵树的结构一定能满足约束条件。下证最优解一定具有上述结构。
  - 显然为了满足约束条件$(1a)$与$(1b)$，视频源节点必须有能够到达所有目的节点的路径。在此基础上，若有流量的边组成的子图不连通，则与视频源节点不连通的连通分量必然与所有目的节点不连通，删去这部分连通分量的流量，答案更优。
  - 假设子图不为树，则：若子图存在环，则设环上距离视频源节点最近的节点为$v$，删去环上具有流向$v$的流量的边，子图仍然满足约束条件，且答案更优；若子图存在不同节点$u,v$使得$u,v$间内部不相交路径不唯一，则删去任意$u,v$间路径上具有流向$v$的流量的边，子图仍然满足约束条件，且答案更优。
  - 假设树上有一个叶节点$v$不是目的节点，则删去$v$的深度最大的孩子数不为$1$的祖先节点到$v$之间的路径，子图仍然满足约束条件，且答案更优。
  - 证毕

- 设$\delta[v][h][S]$表示从$v$出发，经过不超过$h$跳，连通$S$内所有节点的树的最小代价，其中$v \in \mathcal V,S \subseteq \mathcal V_d$，若这样的树不存在，则设$\delta[v][h][S]=+\infty$

  显然$\delta[v][h][S]$有初始条件$\delta[d][h][\{d\}]=0,0\le h\le h_{max},d\in\mathcal V_d$

- 命题2：
  $$
  dp[d][h][\{d\}]=0\ \ \ \ \ 0\le h\le h_{max},d\in\mathcal V_d \tag{2a}
  $$

  $$
  dp[v][h][\emptyset]=+\infty\ \ \ \ \ v\in \mathcal V,0\le h\le h_{max} \tag{2b}
  $$

  $$
  dp[v][h][S] = \underset{T\subseteq S}\min\{dp[v][h][T]+dp[v][h][S\backslash T]\}\ \ \ \ \ v\in \mathcal{V},0\le h\le h_{max},S\subseteq\mathcal V_d \tag{2c}
  $$

  $$
  dp[v][h][S] = \underset{(v,u)\in \mathcal{E},e_v^r\ge \underset{j\in S}\max\{r_j\},k<h}\min\{dp[u][k][S]+\underset{j\in S}\max\{r_j\}\}\ \ \ \ \ v \in \mathcal V,1\le h\le h_{max},S \subseteq \mathcal V_d \tag{2d}
  $$

  ​		则由以上状态转移方程得到的$dp[v][h][S]=\delta[v][h][S]$

  证明：

  - 使用数学归纳法。先证$|\mathcal V_d|=1$时结论成立。假设$G=\{\mathcal V,\mathcal E\},\mathcal V_d=\{a\}$，令$\mathcal E'=\{(i,j)|(i,j)\in\mathcal E,e_i^j\ge r_a\},\mathcal V'=\{v|v\in\mathcal V,hop(a,v)\ in\ \{\mathcal V,\mathcal E'\}\le h_{max}\},G'=\{\mathcal V',\mathcal E'\}$，则问题退化为$G'$上的单源最短路径问题，$(2c)$的转移是无意义的，因为$\{a\}\backslash T$与$T$中必有一个集合为空集，$(2d)$则退化为最短路径的更新公式。易证，$G'$内有$dp[v][h][S]=\delta[v][h][S]$。由于$G\backslash G'$中的点不受$(2c)$和$(2d)$的影响，有$dp[v][h][S]=\delta[v][h][S]$在$G$上成立。
  - 假设$|\mathcal V_d|=k$时结论成立。则当$|\mathcal V_d|=k+1$时，对于任意$T\subseteq \mathcal V_d,|T|\le k$，易证$\delta[v][h][T]$与将$T$视为$\mathcal V_d$时的$\delta[v][h][T]$一致，因此有$dp[v][h][T]=\delta[v][h][T]$。因此只需证明$dp[v][h][\mathcal V_d]=\delta[v][h][\mathcal V_d]$。由$(2c)$可得$\delta[v][h][\mathcal V_d]\le dp[v][h][\mathcal V_d] \le \underset{T\subseteq \mathcal V_d}\min\{\delta[v][h][T]+\delta[v][h][\mathcal V_d\backslash T]\}$，且至少存在一个$v$使得左右不等号同时取等。记这样的$v$为$v'$，从$v'$出发用$(2d)$更新与$v'$相邻的节点，则有$\delta[v][h][\mathcal V_d]\le dp[v][h][\mathcal V_d]\le \underset{(v',v)\in \mathcal{E},e_{v'}^v\ge \underset{j\in \mathcal V_d}\max\{r_j\},k<h}\min\{\delta[v][k][\mathcal V_d]+\underset{j\in \mathcal V_d}\max\{r_j\}\}\ (v\ is\ adjacent\ to\ v')$，且至少存在一个$v$使得左右不等号同时取等。记这样的$v$为$v''$，重复这个过程，直到$\forall v\in\mathcal V$，$\delta[v][h][\mathcal V_d]=dp[v][h][\mathcal V_d]$，结论得证。
  - 证毕

- 于是对于原问题，$dp[s][h_{max}][\mathcal V_d]$就是最优解，其中$s$为唯一视频源节点。

##### 视频源节点不唯一的情况

- 类似多源网络流问题的处理方式，添加一个“超级视频源节点”$\theta$，且对于所有视频源节点$s \in \mathcal V_s$，添加边$(\theta,s)$，其容量为无穷大，且在这条边上的任何流量均无需代价。

  状态转移方程推广为：
  $$
  dp[d][h][\{d\}]=0\ \ \ \ \ 0\le h\le h_{max},d\in\mathcal V_d \tag{3a}
  $$

  $$
  dp[v][h][\emptyset]=+\infty\ \ \ \ \ v\in \mathcal V,0\le h\le h_{max} \tag{3b}
  $$

  $$
  dp[v][h][S] = \underset{T\subseteq S}\min\{dp[v][h][T]+dp[v][h][S\backslash T]\}\ \ \ \ \ v\in \mathcal{V},0\le h\le h_{max},S\subseteq\mathcal V_d \tag{3c}
  $$

  $$
  dp[v][h][S] = \underset{(v,u)\in \mathcal{E},e_v^u\ge \underset{j\in S}\max\{r_j\},k<h}\min\{dp[u][k][S]+\underset{j\in S}\max\{r_j\}\}\ \ \ \ \ v \in \mathcal V,v \not= \theta,1\le h\le h_{max},S \subseteq \mathcal V_d \tag{3d}
  $$

  $$
  dp[\theta][h][S] = \underset{(\theta,u)\in \mathcal{E},k\le h}\min\{dp[u][k][S]\}\ \ \ \ \ 0\le h\le h_{max},S \subseteq \mathcal V_d \tag{3e}
  $$

- 命题2：

  ​		视$\theta$为唯一的视频源节点，用上述状态转移方程求得的最优解在删去$\theta$及与之相连的边之后也是原问题的最优解。

  证明：

  ​		由于$\mathcal V_s$并没有参与状态转移，$\mathcal V_s$对$dp[v][h][S]$和$\delta[v][h][S]$均无影响，只需要证明$(3e)$的合理性即可。显然对于从$\theta$出发连向$s,s\in \mathcal V_s$中的边，由于其传输不计代价，$(3d)$转化为$(3e)$。结合命题1的证明可证明命题2。

#### 实现

---

- 首先枚举$\mathcal V_d$的子集$S$。
- 对于每个$S$，首先枚举$v$，然后枚举$S$的子集$T$，进行$(3a)$的转移，将状态被更新的节点以及其对应跳数加入按照$dp$值从小到大顺序排列的小根堆中。
- 使用类似Dijkstra算法的策略，每次从堆顶取出元素使用$(3b)$和$(3c)$更新与当前节点相邻的节点，将被更新的节点及其对应跳数加入小根堆。

时间复杂度：$O(3^knh_{max}+2^kmh_{max}\log m)$，其中$k=|\mathcal V_d|,n=|\mathcal V|,m=|\mathcal E|$。

如果需要记录最优解的具体流量方案，则需要另外存储$dp[v][h][S]$对应的流量方案，在状态更新时同时更新流量方案中的边。由于命题1，这些边的个数不会超过$n$，所以最终时间复杂度为：$O(3^kn^2h_{max}+2^knmh_{max}\log m)$


/*
input format:
<size_V> <size_E> <size_Vs> <size_Vd> <h_max> the number of vertex, the number of edges, the number of senders, the number of receivers, the max jumps of the transmission
then size_E lines, each line: <i> <j> <e_ij> means an edge in the graph, whose max capasity is e_ij
then size_Vs integers in a single line, each number: <s> means s is a sender
then size_Vd lines, each line: <r> <r_j> means vertex r is a receiver with definition requirement of r_j

sample input:
10 13 1 3 4
1 2 4000
1 3 4000
1 4 4000
2 3 4000
3 4 4000
2 5 4000
3 6 4000
4 7 4000
5 6 4000
6 7 4000
5 8 4000
6 9 4000
7 10 4000
1
8 480
9 1080
10 4000

output:
minimum cost: 15600
edges:
7 -> 10 [4000]
6 -> 9 [1080]
7 -> 6 [1080]
4 -> 7 [4000]
1 -> 4 [4000]
5 -> 8 [480]
2 -> 5 [480]
1 -> 2 [480]

explanation:
            1
          / | \
         2--3--4
        /   |   \
       5 -- 6 -- 7
       |    |    |
       8    9    10
1 is the sender, 8 is a receiver with weight 480, 9 is a receiver with weight 1080, 10 is a receiver with weight 4000.
*/
```

（这个代码还有点问题不想改了，下面的代码里已修复这个问题）

### 问题二

#### 问题

---

在问题一的基础上，增加目的节点对视频视角区间和视频时刻的需求，即$r_j=\{sec_j,tim_j,def_j\}$，每条边上可以传输任意多个时刻的、任意多个区间的任意多个清晰度的视频，且输出流量中的每一时刻的每一区间的流量，需要有对应时刻的、包含该区间的、清晰度不低于该输出的清晰度的输入流量。流量的代价计算方式为视角区间长度乘以清晰度再求和，不同时刻的流量分别统计。求在$h_{max}$的跳数约束下的最优传输方式。

#### 求解

---

- 定义
  $$
  cost(S)=\sum\limits_{t\in \{tim_v|v\in S\}}|\bigcup\limits_{v\in S}[tim_v=t](sec_v\times [0,def_v])|\ \ \ \ \ S\subseteq \mathcal V_d \tag 4
  $$
  其中
  $$
  [q]=\left\{\begin{aligned}&0,&q=False\\&1,&q=True\end{aligned}\right. (q\ is\ a\ boolean\ equation)
  $$
  引入集合的数乘的概念，
  $$
  0S=\empty,1S=S
  $$
  $sec_v\times [0,def_v]$为区间$sec_v$与区间$[0,def_v]$的直积，为一个二维矩形

- 直观上理解，$cost(S)$表示将$S$中所有的目的节点全部连在一条链路上，这条链路上拥有最大流量的边的流量。

- 记$\mathscr S$表示$\{\bigcup\limits_{v \in S}sec_v|S\subseteq \mathcal V_d\}$，即$\{\bigcup\mathcal S|\mathcal S\in2^{\{sec_v\}}\}$，直观上理解为所有目的节点的请求的区间中取任意个进行并集运算后的集合族。

- 记$\mathscr W=\mathcal V_d\times\mathscr S$，即$\mathcal V_d$与$\mathscr S$的直积。

- 命题3：

  ​		同问题一引入“超级视频源节点”，并将状态转移方程推广为

  $$
  dp[d][h][\{d\}\times\mathcal S]=0\ \ \ \ \ 0\le h\le h_{max},d\in\mathcal V_d,\mathcal S\in\mathscr S \tag{5a}
  $$

  $$
  dp[v][h][\emptyset\times \mathcal S]=+\infty\ \ \ \ \ v\in \mathcal V,0\le h\le h_{max},\mathcal S \in \mathscr S \tag{5b}
  $$

  $$
  dp[v][h][S] = \underset{T\subseteq S}\min\{dp[v][h][T]+dp[v][h][S\backslash T]\}\ \ \ \ \ v\in \mathcal{V},0\le h\le h_{max},S\subseteq\mathscr W \tag{5c}
  $$

  $$
  dp[v][h][S\times \mathcal S] = \underset{(v,u)\in \mathcal{E},e_v^u\ge cost(S),k<h}\min\{dp[u][k][S\times \mathcal S]+cost(S)\}\ \ \ \ \ v \in \mathcal V,v \not= \theta,1\le h\le h_{max},S \subseteq \mathcal V_d,\mathcal S \in \mathscr S \tag{5d}
  $$

  $$
  dp[\theta][h][S\times \mathcal S] = \underset{(\theta,u)\in \mathcal{E},k\le h}\min\{dp[u][k][S\times \mathcal S]\}\ \ \ \ \ 0\le h\le h_{max},S \subseteq \mathcal V_d,S \subseteq \mathcal V_d,\mathcal S \tag{5e}
  $$
  
  ​		则$dp[\theta][h][\mathcal V_d\times\bigcup\limits_{v\in \mathcal V_d}sec_v]$为该规划问题的最优解。
  
  证明：
  
  ​		同命题2。

#### 实现

---

类似于问题一的实现方式，但是由于被枚举的集合变为了原先集合与所有可能出现的视频区间的集合$\mathscr S$的直积，而$|\mathscr S|=2^k$，其中$k$为目的节点的数量，若使用同问题一的实现方法，算法的时间复杂度为：$O(9^knh_{max}+4^kmh_{max}\log m)$，其中$k=|\mathcal V_d|,n=|\mathcal V|,m=|\mathcal E|$。同样若需要记录具体方案的话则需要在此基础上乘以$n$。

在此我们假设总视频的角度区间只由四部分组成，目的节点对于视频角度的请求由其中的若干个部分组成，则算法复杂度变为：$O(3^{(k+4)}nh_{max}+2^{(k+4)}mh_{max}\log m)$。


output:
minimum cost: 43200
edges:
1 -> 4 { [(0, 4000, 4000, 4000), time = 0] }
4 -> 7 { [(0, 4000, 4000, 4000), time = 0] }
7 -> 10 { [(0, 4000, 4000, 4000), time = 0] }
7 -> 6 { [(0, 0, 1080, 1080), time = 0] }
6 -> 9 { [(0, 0, 1080, 1080), time = 0] }
1 -> 2 { [(480, 480, 0, 0), time = 0] }
2 -> 5 { [(480, 480, 0, 0), time = 0] }
5 -> 8 { [(480, 480, 0, 0), time = 0] }

explanation:
            1
          / | \
         2--3--4
        /   |   \
       5 -- 6 -- 7
       |    |    |
       8    9    10
1 is the sender, 8 is a receiver with weight 480, 9 is a receiver with weight 1080, 10 is a receiver with weight 4000.





#### 贪心策略



- 定义
  $$
  \mathcal P(u,v)=the\ path\ from\ u\ to\ v\ with\ the\ length\ of\ hop(u,v)\ in\ graph\{\mathcal V,\{(u,v)|(u,v)\in\mathcal E,e_u^v\ge cost(\{u\})\}\}
  $$

  $$
  len(p)= the\ length\ of\ p\ which\ is\ a\ path\ in\ the\ graph
  $$

1. 建立“超级视频源点”$\theta$，将$\theta$加入$\mathcal V$，将$\forall s\in\mathcal V_s,(\theta,s)$加入$\mathcal E$，并令$e_\theta^s=+\infty$。
2. 将$\forall d\in\mathcal V_d$按照第一关键字$len(\mathcal P(d,\theta))$降序，第二关键字$cost(\{d\})$降序，第三关键字$\sum\limits_{v\in \mathcal V_d}[tim_d=tim_v]$降序进行排序，记排序结果为$\{d_1,d_2,\dots,d_{|\mathcal V_d|}\}$
3. $k\leftarrow1,\mathcal C\leftarrow \{\{\theta\},\emptyset\}$
4. 从$\theta$开始在$\mathcal C$上进行深度优先搜索，寻找$v=argmin\{len(\mathcal P(d_k,v))\cdot cost(\{d_k\})\}$，并记录$\theta$到$v$的路径$P$，设深度优先搜索时当前节点为$x$，遍历的下一条边是$e$，则若$e_x^v$不足以在这条边上增加传输$d_k$所需内容的流量，或者$e$不含有与$d_k$需求时刻相同的流量，则回溯。
5. 在$P$中的边上增加传输$d_k$所需内容，并在相应$e_i^j$上减去增加的代价。
6. 在$\mathcal P(d_k,v)$中所有边上增加传输$d_k$所需内容，并在相应$e_i^j$上减去$cost(\{d_k\})$，并将这些边加入$\mathcal C$。
7. 若$k=|\mathcal V_d|$，则结束，$\mathcal C$为具体传输方案，否则$k\leftarrow k+1$，回到4.

时间复杂度：$O(km)$，其中$k=|\mathcal V_d|,m=|\mathcal E|$。

在随机生成的数据上进行比较测试的结果为平均贪心策略找到的解的代价为dp策略找到的解的代价的$1.05$倍左右，但存在不到$1\%$的数据出现dp策略找到解但贪心策略无解的情况。
