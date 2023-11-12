### Week 10
[1]Q. Chen et al., "Latency-Optimal Pyramid-based Joint Communication and Computation Scheduling for Distributed Edge Computing," IEEE INFOCOM 2023 - IEEE Conference on Computer Communications, New York City, NY, USA, 2023, pp. 1-10, doi: 10.1109/INFOCOM53939.2023.10228964.    
分布式边缘计算中基于金字塔的延迟最优联合通信和计算调度

**背景**：近年来，**分布式边缘计算（DEC）** 已经成为一种新的计算范式，通过结合边缘计算和并行计算，可以加速边缘计算的过程。然而，现有的研究假设通信时间是固定的以及工作负载可以任意分割，限制了其实际应用的可行性和普适性。  
**论文的Motivation**: 鉴于现有研究的局限性，本文重新研究了分布式边缘计算中的最小延迟联合通信和计算调度（MLCCS）问题，考虑了通信时间的动态性和工作负载的分割性，旨在提出更实用和通用的解决方案。    
**技术路线**：本文引入了**基于金字塔的计算模型**，计算每个设备的最优调度顺序和分配的工作负载。此外，提出了一种**近似任务分配算法**，将子任务分配给每个设备。  
### Week 9
# Learning to Schedule Tasks with Deadline and Throughput Constraints 
学习在截止时间和吞吐量约束下进行任务调度
## 背景
过去的研究中，任务调度问题通常被建模为多臂赌博机问题，其中每个臂代表一个任务类型。然而，这些模型没有**考虑到截止时间和吞吐量约束**，这在实际应用中是非常重要的。  

本文的动机是解决任务调度中的两个独特挑战：**数据新鲜度和吞吐量约束**。数据新鲜度要求任务在一定时间内完成，否则数据将过时。吞吐量约束要求系统能够保证一定的数据处理速度。为了解决这些挑战，本文提出了一种**在线学习算法，结合了赌博理论、Lyapunov优化和统计估计**的新设计和分析技术。  

本文考虑了任务调度场景，其中控制器每次激活K个任务类型中的一个。每个任务引发一个**随机完成时间**，并且只有在任务完成后才能获得奖励。控制器对所有任务类型的完成时间和奖励分布的**统计数据是未知的**。控制器需要学习调度任务，以**在给定的时间范围内最大化累积奖励**。
## 方法
离线Lyapunov策略：使用**Lagrangian优化方法**开发了离线Lyapunov策略，称为π<sup>off</sup>。它通过平衡最大化奖励和满足吞吐量约束之间的权衡来优化问题的Lagrangian。使用**虚拟队列Qn**来跟踪约束违反，并根据虚拟队列的值设计Lagrange乘子λn。策略根据虚拟队列的值选择具有**最高奖励率或完成率**的任务。提供了π<sup>off</sup>的性能界限，表明它在离线设置中**保证了O(√T)的遗憾值和零约束违反**。

在线Lyapunov策略：在在线学习设置中，提出了一种**具有低遗憾值和约束违反的高效算法**。由于奖励率和完成率的统计量未知，使用**经验估计器和上置信校正**来鼓励探索。为了确保由探索引起的有界遗憾值和约束违反，推导了经验均值估计的高概率置信半径。**使用两个样本均值之间的商的浓度界限构造置信半径**。算法称为π<sup>on</sup>，根据估计选择任务。引理1表明，经验均值估计与真实值的接近概率很高。  
## 动机场景  
**云计算中的任务分配**：控制器的目标是在给定的时间跨度内最大化总体效用，同时满足系统的吞吐量要求，即在单位时间内完成的任务数量。  
**无线视频流传输**：用户的目标是在给定时间内最大化其总体获得的效用，同时满足最低成功数据块下载速率的要求。  

## 问题表述
为了数学描述这个过程，我们将Γ<sup>π</sup><sub>n</sub>表示在策略π下第n次试验选择的臂，这个策略只基于过去的观察结果，没有未来信息。在我们的模型中，我们考虑了老虎机反馈设置，也就是说，控制器只能在第n次试验后观察到向量：  
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/2792744b-e1d7-4824-ac37-421ee8512b5b"></div>
给定时间跨度T，根据策略π启动试验的数量是：
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/142f99cc-6a96-4cd2-a45b-5fd26b0e67b6"></div>
策略π下的总累积奖励为：
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/932d20c8-c2a5-4bf5-b39c-02c2eac834c0"></div>
需要注意的是，设计旨在最大化累积奖励的策略可能会导致低吞吐量（单位时间内成功完成的试验数量）。为了解决这一服务质量（QoS）问题，我们为控制器引入了以下吞吐量约束：
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/37369bf7-6f51-4a5f-9eaf-026efbda0cd3"></div>
因此，控制器的目标是找到一个在线策略π<sup>OPT</sup>（最佳策略），满足：
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/ad4c290b-1871-4ee7-8d0f-eefed3f250f5"></div>
然而，由于{X<sub>k,n</sub>, R<sub>k,n</sub>}序列及其统计数据是事先未知的，因此找到π<sup>OPT</sup>是不可能的，我们的目标是设计一个在线学习策略π，该策略在与π<sup>OPT</sup>相比具有良好的竞争性能。对于这一目标，性能度量指标是遗憾值和约束违反，定义如下：
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/fc0d7a88-39a4-4242-93df-f978f48c3fe0"></div>

这些公式用于定量评估策略 π 的性能，其中 "Regret" 表示了策略与最佳策略之间的性能差距，而 "Constraint Violation" 表示了策略是否满足了约束条件。研究人员通常希望设计策略，以最小化 "Regret" 并确保 "Constraint Violation" 接近零，以获得最佳的性能和可行性。

其中，OPT(T)是策略π<sup>OPT</sup>的期望累积奖励。我们的**目标是获得一个次线性的遗憾值和随着给定时间跨度T迅速减小的约束违反**。**由于臂的统计数据是未知的**，为了实现这一目标，我们必须在老虎机类型反馈中**平衡利用和探索**之间的权衡，设计了一个高效的**在线策略来优化这个权衡**以进行最佳学习。

## 最优离线策略的近似
**Lagrange Multiplier（拉格朗日乘子）**：在约束优化问题中，拉格朗日乘子是用来考虑约束条件的方法之一。它们通过将约束条件引入目标函数，从而将**优化问题转化为一个无约束问题**。λn 是与约束 c(p) ≥ α 相关的拉格朗日乘子，它用于平衡最大化奖励和满足约束条件之间的权衡。  
**Virtual Queue（虚拟队列）**：虚拟队列 Qn 用于跟踪约束违反的 "债务"，即约束条件在前 n 次决策中的违反情况。它在每个决策点更新，考虑了任务的完成时间和约束条件的关系。通过虚拟队列，算法试图管理约束条件的满足情况。  
**Balance Parameter（平衡参数）**：1/V 是平衡参数，用于调整虚拟队列与拉格朗日乘子之间的关系。这个参数可以用来平衡约束条件的满足和最大化奖励之间的权衡。  
**Pessimistic Mechanism（悲观机制）**：为了确保零约束违反（constraint violation），算法引入了一种悲观机制，通过使虚拟队列过高估计约束违反来实现。这意味着虚拟队列会预测比实际情况更严格的约束条件，以确保满足约束。  

Theorem 1说明了在离线设置中，当T足够大时，π<sup>off</sup>可以保证O(√T)的遗憾（regret），并且零约束违反（zero constraint violation）。在在线学习设置中，π<sup>off</sup>将作为我们设计高效算法的指导。这个定理表明在足够大的时间范围内，π<sup>off</sup>的性能是很好的，但对于小时间范围可能需要更复杂的算法来实现相似的性能。
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/fe8eb5d5-cd78-4040-8b3d-b4fa3d4c8944"></div>

##  基于lyapunov的在线策略
在线学习设置中的一种高效算法，它具有低遗憾和约束违反。由于算法在开始时并不了解（r<sub>k</sub>，c<sub>k</sub>）的信息，因此它使用（r<sub>k</sub>，c<sub>k</sub>）的**经验估计值**，同时引入一种**上置信度修正**，以鼓励探索未知信息。为了确保探索不会导致过多的遗憾和约束违反，我们需要计算（r<sub>k</sub>，c<sub>k</sub>）的经验均值估计的**高概率置信半径**。需要注意的是，r<sub>k</sub>和c<sub>k</sub>都是两个期望值之比，因此**传统的赌博领域的集中不等式不适用**于这种情况。因此开发了适用于估计奖励率和约束率的**新型集中半径**。
<div align=center><img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/bc6c9dd4-6640-4f05-9670-fc229926e357"></div>

##  多个中断时间选择
具体来说，在每次选择一个任务后，控制器可以从有限的离散集合T = {t1, t2, ..., tL} 中选择一个中断时间。这里tL可以是+∞，也就是说，控制器认为等待任务完成是最优的。在这种情况下，需要注意，对于[K] × T中的任何一对（k，t），在确定性策略下，观察到的随机过程在n上是独立同分布的。  
定理3考虑 R<sub>k,n</sub> 独立于X<sub>k,n</sub>的情况。 (a) 如果X<sub>k,n</sub> ∼ Exp(λ)，则对于所有t>0，r<sub>k,t</sub>= E[R<sub>k,1</sub>]λ且c<sub>k,t</sub> = λ，即中断时间的选择不会影响奖励率和完成率。 (b) r<sub>k,t</sub>和r<sub>k,t</sub>是高斯分布、均匀分布、逻辑分布和伽玛完成时间分布的t单调递增函数。  
定理3的一些观察结果：(a) 当完成时间由于无记忆特性呈指数分布时，中断不会产生影响。 (b) 对于许多轻尾完成时间分布，最佳中断时间是无限的。  

## 实验结果
实验设置：我们使用伯努利分布式奖励和重尾分布式完成时间评估 K = 4 个臂的π<sup>off</sup>和π<sup>on</sup>算法。手臂统计设计如下：
<div align=center><img width="700" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/006124d5-f9f4-415e-bffd-e3d05ddc1814"></div>

臂1和臂2被设置为奖励率低但完成率高，臂3和臂4则相反。  
在我们的模拟设置中，我们选择V=√T、δ=d/√T，图中的每个点都是 100 个独立实验的平均值。  
图1绘制了π<sup>off</sup>、π<sup>on</sup>和最优随机策略π(p*)在不同时间间隔T下的奖励率R(T)/T。它表明离线和在线设计都达到了最优设计的速率，如我们的理论结果所示。  
图1(b)和图2(b) 证实了π<sup>on</sup>违反约束的缩放行为，即当 T 足够大时，其随速率 O(1/T) 变化，这也在我们的理论结果中得到了揭示。他们还表明，当 T 足够大时，如果选择适当的 V 和 δ 值，我们确实可以获得负约束违反。  
<div align=center><img width="700" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/121794362/abbd6f51-6a0d-4514-96b7-50f7e6db121e"></div>


### Week 8

1、完成了嵌入VNFs的代码，能跑通，但还有点问题。

2、学习处理时延的论文。

[1]Q. Liu and Z. Fang, "Learning to Schedule Tasks with Deadline and Throughput Constraints," IEEE INFOCOM 2023 - IEEE Conference on Computer Communications, New York City, NY, USA, 2023, pp. 1-10, doi: 10.1109/INFOCOM53939.2023.10228901.

### Week 7

1、项目工作。

### Week 6

1、学完了代码，把VNFs改成复用类型，参照论文中的算法嵌入VNFs。

[1]G. Wang, S. Zhou, S. Zhang, Z. Niu and X. Shen, "SFC-Based Service Provisioning for Reconfigurable Space-Air-Ground Integrated Networks," in IEEE Journal on Selected Areas in Communications, vol. 38, no. 7, pp. 1478-1489, July 2020, doi: 10.1109/JSAC.2020.2986851.

2、撰写查新报告。

### Week 4

1、学了A2C（Advantage Actor-Critic）算法和DGL；

2、学习贺博的论文。


### Week 3

1、撰写项目申请书；

2、学习贺博的代码。


### Week 2

1、配置环境；

2、学完后思考如何利用Graph Transformer。
- GAT的self-attention只计算邻居节点，而Transformer的self-attention会考虑所有的节点。
- Graph Transformer结合了Transformer的核心（全局关注）和GNN的核心（考虑图的拓扑属性）。
