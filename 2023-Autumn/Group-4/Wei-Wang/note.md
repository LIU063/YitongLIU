### Date: 2023/9/10

[![sample-image](./IMG_7998.png)](https://unic.xidian.edu.cn/ "西安电子科技大学泛在网络与智能计算研究组")

------------------------------------------------
### 本周工作

## MARL解决3C资源调度工作

### 1.目前进展
>  针对之前出现的两个问题，即收敛性差，和 credit assigment 问题，本周对仿真代码做出如下调整：

1. 简化了部分模型，主要集中在拍卖过程由多轮拍卖调整成单轮的第二价格拍卖（Vickrey）， task 的 VoI的分布采用服从二八定律的 Pareto 分布； 归一化 SP Agent 的 动作空间成为上一时刻出价的百分比（0.5-1.5）

2. 对于 credit assignment 问题， 目前的做法是使用优势函数对各个 SP Agent 的 reward 做归一化的处理，优势函数设置成服务累计VoI的平均值，由采样获得。

目前在设置 Nsp 1个 SP3个， MEC 5 个的仿真坏境下进行 MADDPG 、MFMARL、MFMARL-v (我们提出的) 三种算法的实验。



### Date: 2023/9/5

[![sample-image](./IMG_7998.png)](https://unic.xidian.edu.cn/ "西安电子科技大学泛在网络与智能计算研究组")

------------------------------------------------
### 本周工作

## MARL解决3C资源调度工作

### 1.目前进展
> 仿真程序的大体框架已经编写完成，目前正在调试MARL算法，使其收敛并取得理想的效果。

### 2.目前主要问题
> - MARL算法(MARDDPG/MFMARL)难以收敛，且性能较差(对比固定策略)；
> 
> - 不同智能体之间的reword差异比较大，即存在 credit assignment 问题；

### 3.解决思路

- 针对算法难以收敛的问题，目前的想法是首先简化之前的系统模型，包括将多轮拍卖模型简化成 Vickrey auction， 将 task 的部署模式设置成3种固定策略之间的选择； 其次，是在智能体之间共享额外信息，如资源利用率；

- 针对 credit assignment 问题， 目前的正在查阅相关文献，已查阅的文献中如下, 其中均有解决此类问题的方法；

> [1] Sunehag P, Lever G, Gruslys A, et al. Value-decomposition networks for cooperative multi-agent learning[J]. arXiv preprint arXiv:1706.05296, 2017.
> 
> [2] Foerster J, Farquhar G, Afouras T, et al. Counterfactual multi-agent policy gradients[C]//Proceedings of the AAAI conference on artificial intelligence. 2018, 32(1).
> 
> [3] Iqbal S, Sha F. Actor-attention-critic for multi-agent reinforcement learning[C]//International conference on machine learning. PMLR, 2019: 2961-2970.
> 
> [4] Long Q, Zhou Z, Gupta A, et al. Evolutionary population curriculum for scaling multi-agent reinforcement learning[J]. arXiv preprint arXiv:2003.10423, 2020.
