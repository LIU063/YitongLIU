### Date: 2023/11/7

[![sample-image](./IMG_7998.png)](https://unic.xidian.edu.cn/ "西安电子科技大学泛在网络与智能计算研究组")

------------------------------------------------
### 本周工作

## MARL解决3C资源调度工作

目前，正在调试剩余仿真实验的代码，预期的仿真实验：SP（Agent）加入/离开的收敛曲线； Sp任务价值分布的帕累托参数和回报关系； zipf不同参数和 MEC 收益关系图；使用不同拍卖方式获得的收益对比；

[sample-image](./fig/Figure_5.pdf)



### Date: 2023/10/29

[![sample-image](./IMG_7998.png)](https://unic.xidian.edu.cn/ "西安电子科技大学泛在网络与智能计算研究组")

------------------------------------------------
### 本周工作

## MARL解决3C资源调度工作

1）增加SP数目体现 MFMARL、MFMARL-v 的优势与MADDPG相比

[sample-image](./fig/Figure_1.pdf)

2）设置消融实验展示 MFMARL-v 对比 MFMARL

[sample-image](./fig/Figure_4.pdf)

3）改变 MEC 数目展示 NSP 的受益曲线

[sample-image](./fig/Figure_2.pdf)

4）收敛速度对比
[sample-image](./fig/Figure_33.pdf)

### Date: 2023/10/16

[![sample-image](./IMG_7998.png)](https://unic.xidian.edu.cn/ "西安电子科技大学泛在网络与智能计算研究组")

------------------------------------------------
### 本周工作

## TVT论文修改

目前基本修改完成。

## MARL解决3C资源调度工作

### 1.目前进展

Nsp 1个 SP3个， MEC 5 个的仿真坏境下 reword 曲线。

 ![sample-image](./Figure_1.png)]

Nsp 1个 SP6个， MEC 5 个的仿真坏境下 reword 曲线。

 ![sample-image](./Figure_2.png)]

### 2.后续实验

1）增加SP数目体现 MFMARL、MFMARL-v 的优势与MADDPG相比

2）设置消融实验展示 MFMARL-v 对比 MFMARL

3）改变 MEC 数目展示 NSP 的受益曲线

4）测试不同任务分布下 SP和 NSP 收益



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
