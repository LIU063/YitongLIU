<p id="table"></p>

## Table of Contents

- <a href="#1"> 1 $^{st}$
- <a href="#2"> 2 $^{nd}$
- <a href="#3"> 3 $^{rd}$
- <a href="#4"> 4 $^{th}$
- <a href="#5"> 5 $^{th}$
- <a href="#6"> 6 $^{th}$ 
- <a href="#7"> 7 $^{th}$
- <a href="#8"> 8 $^{th}$
- <a href="#9"> 9 $^{th}$
- <a href="#10"> 10 $^{th}$
- <a href="#11"> 11 $^{th}$

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


<br/>

<p id="4"></p>

# <a href="#table"> Week 4 (2023.04.07 – 2023.04.13)</a>

## 修改DTRL Magazine

## VoI
可以将sender传输次数从12次缩减到6次，依然可以在4*10的范围，4个hole的条件下，以最短的次数(12步)走到goal

## 视频传输
1. 对问题做了进一步的改进，加上了VR FoV的问题，也就是假设多个用户同时请求一个VR视频，但是他们观看时间、观看区域、观看清晰度都不相同(相当于用户约束从一维变三维)，最小化总传输成本
2. 动态规划可以找到最优解，同时用贪心的方式以O(MN)的复杂度实现了最优解99.5%的性能，甚至在很多情况下，贪心的解和最优解完全一样。(看不懂，但是大受震撼)

<br/>

<p id="5"></p>

# <a href="#table">Week 5 (2023.04.14 – 2023.04.18)</a>

## 修改论文

## 图神经网络扩展性的研究
### Movitation 
1. 多智能体强化学习一般难以处理智能体数量变化的问题
2. 图神经网络通常认为具有可扩展性
3. 图神经网络实际上也可以看成一种共享参数的多智能体网络
4. 造成这种差异的根源在于观测维度的变化
### Insight
图神经网络节点的度，对应了聚合邻居信息时的观测数据维度，因此为了保证图神经网络的可靠扩展，应该根据节点的度，来分配不同的聚合模型


<p id="6"></p>

# <a href="#table">Week 6 (2023.04.19 – 2023.04.27)</a>
## 图神经网络泛化性研究
### 图节点中不同的度，对于AGG Net而言本质上对应了不同的输入类型和输出类型。
1. 对于一个既有高度和低度的图，AGG Net本质上类似在所有class数据上训练。而如果只在高度或低度图上训练，本质上相当于只训练了dataset集中一个class的数据，那么不可避免的会发生对单一class，即单一度的过拟合。这是因为对于不同度的节点而言，其需要提取的message的分布其实和其邻居数量有关。例如对于SINR优化问题，其message的本质是计算干扰和大小，这就会导致不同度节点的message对应的输出分布是不一样的。
2. 进一步分析可以得到一个结论，即如果GNN需要输出的每个节点的optimal value分布与节点的度相关，那么在单一度上训练的效果将不具有泛化能力。反之，弱GNN Node的optimal value分布与节点的度无关，则在任一度上训练的GNN都应具有一定的泛化能力。
3. 这个可以从多类回归的角度去解释，做资源分配的本质是对输入的数据做回归预测。如果节点的度会影响最终的optimal value，那么可以将不同度的节点视为不同class的数据，每个class的ground truth具有不同的分布。那么给每个度分配特定的AGG Net相当于在单一class数据上做回归任务。对于所有度用同样的AGG Net相当于先做分类判断该数据属于哪一个class，在做回归来判断这个数据的具体回归值。
4. 不论对于分类还是回归任务而言，数据的class越少训练难度也就越小，训练精度也就越高。2分类的性能显然高于1000分类。
具体而言，类似人脸识别，识别单一人像的难度远小于同时识别多个人的难度。
5. 对于图像而言，精确到该图像更可能属于某几个类的处理难度是巨大的。但是对于图节点，可以轻易获知其度的大小。
6. 因此为每个不同的度节点训练不同的AGG Net是有意义的

### GNN与FL
1. GNN在推理的时候知道全图所有节点共享一个聚合神经网络，FL的每个用户也共享一个NN
2. GNN在训练过程中需要收集全图所有节点的loss以此计算平均loss来更新聚合函数。FedSGD下每个用户在计算完自己的loss或gradient后，传到服务器上做梯度聚合从而更新globe model
由此可以得到一个暴论：GNN所面临的大部分问题，其实FL中也有
根据这个思路看的话，不同的节点类型和节点的度，如果会造成节点需要输出的ground truth label的分布不同。那么用一个共享的AGG Net去做训练，相当于FL中不同用户的数据分布是Non-IID的

## Zero-Shot User for Personalized FL
在N个Non-IID用户下分别train出来了多个personalized model。假设有第N+1个用户，在不训练的条件下，直接利用前N个personalized model组合出一个可以给第N+1个用户的model

## VoI的一种定义尝试
信息价值->传输增益->决策增益 Decision Gain
当前数据的传输价值
$VoI_{\pi}(s) = \sum_{a\in \mathcal{A}} \pi(a;s)|Q(s,a)|$
加绝对值的目的，是因为一些state的传输可能导致系统决策崩塌，或者策略
$\pi$
做出的所有action中收益有正有负

决策增益
$\sum_{a\in \mathcal{A}} \pi(a;s)Q(s,a) - \sum_{a^{-}\in \mathcal{A}}\pi(a^{-};s^{-})Q(s,a^{-})$
只要决策增益大于传输成本就需要传输该数据

<p id="7"></p>

# <a href="#table">Week 7 (2023.04.28 – 2023.05.04)</a>

## Joint Optimization of AIGC and Resource Allocation
*赶紧水，时不我待，那帮人也太能写了

联合优化diffusion model的denoise层数、以及实时更新率(是全denoise全再传，还是边denoise边传，有个进度条一样的东西，甚至允许用户自行添加噪声或设置中断)和边缘计算那一堆玩意，做性能和时延的tradeoff

(diffusion+dynn?)

<p id="8"></p>

# <a href="#table">Week 8 (2023.05.05 – 2023.05.11)</a>

## Dynamic Diffusion
大力出奇迹

要巧妙的构造数据集，主要就是进一步拓宽diffusion的均值原理，本来加的噪声都是零均值且方差固定的噪声噪声，可以在$t_i$到$t_i + 1$间添加多种不同方差的噪声，但是这些噪声的方差的均值还是个固定值。

## VoI Letter Intro
写的有点懵

## RingSFL配对
用贪心做了个RingSFL的两两配对和龙博合作整一个GC

<p id="9"></p>

# <a href="#table">Week 9 (2023.05.12 – 2023.05.18)</a>

## Effectively Heterogeneous Federated Learning: A Pairing and Split Learning Based Approach
和沈在一起写，预计周五写完

## Mutual Knowledge Distillation for Efficient Diffusion Training
用K个设备分别学denoise T/K的部分，然后相互蒸馏，提高收敛速度


<p id="10"></p>

# <a href="#table">Week 10 (2023.05.19 – 2023.05.25)</a>

## GC论文

## QMIX-GNN
可以证明GNN是置换不变的，同时基于Graph的UAV trajectory design problem也是置换不变的。因此，基于Kolmogorov-Arnold定理，可以设计一个agent数量任意多的分布式MARL算法



