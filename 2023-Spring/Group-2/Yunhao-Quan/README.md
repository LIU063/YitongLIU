# 第12周周报
## 制作组会PPT
## 复现修改URLLC可靠调度论文代码(https://ieeexplore.ieee.org/document/10093058)


















# 第一周周报


## 工作进度
本周主要调试无人机避障代码，之前提出的2个DQN，一个负责规划路线，一个负责避障的方法难以收敛，改换基于MCTS(蒙特卡洛树搜索的方法)，在不同的树搜索深度下测试碰撞发生的概率，编写baseline对比算法，与树搜索算法进行比较。下一步考虑参考TWC2021一篇文章的场景将此问题的goal改成让各个用户和速率最大的点。后续继续调试代码，绘制图表，准备撰写论文



## 6G大会
可解释性资源调配推理要求利用可解释性AI进行透明、可靠、可担责的按需服务，目前这一方向很少有人提到，相应的可解释性框架也少之又少，可以探索一番。
# 第二周周报


## 工作进度
画架构图以及论文所需的结果图。
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure1.jpg)
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure2.png)
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure3.png)
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure4.png)
## 下周工作安排
尽快撰写完论文，投稿。
# 第三周周报
上周提到的对比算法实现及其性能比较
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure3.svg)
# 第四周周报
## 修改论文
## 调研XAI在MARL中的应用
   (1)能否采用shapely的方法评估合作MARL过程中的参与者贡献程度
   
   (2)MARL shapely值计算复杂度可能会很高
   
   (3) MARL场景的选取
## 配置环境，在muliti-gym中尝试实现MARL shapely计算。
# 第五周周报
在算法收敛性分析图中，random算法在刚开始会出现小幅度上升，修改环境,debug解决这一问题。
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/fig3.svg)

# 第六周周报
修改论文Introduction和大纲结构
# 第七周周报
修改论文并投稿
 
# 第八周周报

调研XAI在物理层的应用
## Guaranteed Dynamic Scheduling of Ultra-Reliable Low-Latency Traffic via Conformal Prediction(https://ieeexplore.ieee.org/document/10093058)
URLLC 在上行链路上的动态调度，可以显著提高eMBB 设备等共存业务的效率，只在需要的时候分配资源。主要的挑战是URLLC包生成过程中的不确定性，这要求在接下来的帧中使用URLLC流量预测器。在实践中，这种预测可能会高估或低估要生成的URLLC数据量，从而导致为URLLC数据包预先分配的资源量过高或不足。这篇文章为URLLC数据包引入了一种新的调度器，它提供了对可靠性和延迟的正式保证，而不考虑URLLC流量预测器的质量。利用了在线共形预测(CP)的最新进展，并遵循动态调整分配资源数量的原则，以满足设计者设定的可靠性和延迟要求。
## Modular Model-Based Bayesian Learning for Uncertainty-Aware and Reliable Deep MIMO Receivers(https://arxiv.org/pdf/2302.02436.pdf)
在无线接收器的设计中，深度神经网络(dnn)可以与传统的基于模型的接收器算法相结合，实现基于模型/数据驱动的模块化混合架构，这样的体系结构通常包括多个模块，每个模块执行不同的功能。众所周知，传统训练的基于dnn的模块会产生校准不良、通常过于自信的决策。这意味着不正确的决策可能在没有任何指示其不够准确的情况下通过体系结构传播。为了解决这个问题，本文提出了一种将贝叶斯学习与基于模型/数据驱动的混合架构相结合的无线接收器设计方法。所提出的方法被称为基于模块模型的贝叶斯学习，可以更好地校准模块，提高整个接收器的精度和校准。
