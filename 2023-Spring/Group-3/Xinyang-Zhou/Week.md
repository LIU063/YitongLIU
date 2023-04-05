# **周报-Week03**
##### 时间：2023.03.30——2023.04.05

### **一、主要工作内容和进展**
1、参考文章推导博弈论公式，建立模型 

学习三种动态价格方案

Baek B, Lee J, Peng Y, et al. Three dynamic pricing schemes for resource allocation of edge computing for IoT environment[J]. IEEE Internet of Things Journal, 2020, 7(5): 4292-4303.
https://ieeexplore.ieee.org/abstract/document/8959172


![](./pic/3.jpg)

2、做6G ppt

3、找近三年分布式论文



### **二、下周工作计划**

继续看博弈论的内容，解优化问题




# **周报-Week02**
##### 时间：2023.03.23——2023.03.29


##### 1、《CoopFL: Accelerating federated learning with DNN partitioning and offloading in heterogeneous edge computing》
文章来源：
Wang Z, Xu H, Xu Y, et al. CoopFL: Accelerating federated learning with DNN partitioning and offloading in heterogeneous edge computing[J]. Computer Networks, 2023, 220: 109490.
![](./pic/coopfl.png)


**本文可参考的点：**

![](./pic/workflow.png)







##### 2、《无线分布式学习系统的模型优化与资源管理》
文章来源：刘胜利. 无线分布式学习系统的模型优化与资源管理[D].浙江大学,2022.
这是一篇浙江大学的博士论文，比较具有参考价值。

**本文可参考的点：**
**去中心化无线分布式系统链路选择与资源优化** 
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week02/pic/1.png)

**（1）模型：( 学习模型  +  通信模型 )**

学习模型：去中心化学习模型
通信模型：D2D通信

基于以下分析，建立最小化总训练开销的数学优化问题。
- 单次训练时延分析：本地模型计算和模型传输。max（comp+comm）
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week02/pic/汇聚.png)
- 单次能耗分析：本地模型计算和模型传输。
- 收敛速率分析：若D2D网络需要最多𝑆次训练才收敛到正确率需求𝜀，则该收敛步数的上界𝑆可以表示为：
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week02/pic/s.png)

为提高去中心化无线分布式学习系统的通信效率和能量效率，应该通过联合优化链路选择、模型汇聚权重、算力分配以及无线资源分配，最小化总训练开销。数学上可以建模为：
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week02/pic/建模.png)

把上述问题分为三个子问题：
算力和无线资源分配优化、模型汇聚权重优化以及链路选择优化.

给定链路选择方案和功率分配时，分别求解本地算力和带宽分配优化，汇聚权重优化问题。


**（2）链路选择**
链路选择是为了平衡收敛速率和单次训练开销对模型训练性能的影响。当被激活的D2D链路数量增加时，系统需要更少的步数收敛到给定的正确率。相反，单次训练开销随着激活链路数量的增加而增大。
全连通网络不一定是系统最优的。也就是说，在基于D2D的去中心化无线分布式学习系统中，存在最优的链路选择，使得模型训练的开销最小。




### **二、下周工作计划**

找一下FL和MEC联合参考文献，继续讨论idea




# **周报-Week01**
##### 时间：2023.03.16——2023.03.22
### **一、主要工作内容和进展**

##### 1、《EFFICIENT SPLIT-MIX FEDERATED LEARNING FOR ON-DEMAND AND IN-SITU CUSTOMIZATION》论文阅读

文章来源：Hong J, Wang H, Wang Z, et al. Efficient split-mix federated learning for on-demand and in-situ customization\[J]. arXiv preprint arXiv:2203.09747, 2022.

该论文已被 **ICLR2022** 接收。

**本文可参考的点：** （也是标题中所阐述的）
**按需**：**on-mand**
**现场定制**：**in-situ customization**

本文中提出了一种新的Split-Mix FL策略，一旦训练完成，就提供了模型大小和鲁棒性的现场定制（in-situ customization）。通过学习一组不同大小和鲁棒性级别的基本子网络来实现定制，然后根据推理需求按需聚合这些子网络。这种混合策略在通信、存储和推理方面实现了高效率的定制。实验结果表明，我们的方法比现有的异构架构FL方法提供了更好的现场定制。



本文参考了第一个允许现场模型大小切换的异构宽度解决方案(HeteroFL)的工作（**发表在ICLR2021**）。然而，由于本地设备预算限制，导致大型模型训练不足，因为在这个里面训练的是大模型。
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week01/pic/1（a）.png)


提出的Split-Mix框架提供了宽度的现场定制和对抗性鲁棒性，以解决异质性和动态问题，从而实现有效的训练和推理。如图，可以使用每层1/4通道(或宽度)的子网作为模型宽度定制的基本模型。为简单起见，我们将其表示为×0.25 net，而一个×1 net可以分为4个×0.25基本模型。
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week01/pic/1（b）.png)

**讨论**：和龙博讨论之后感觉在这个基础上改可能比较不太好实现，后续再讨论看看有没有能创新的点。

##### 2、《无线分布式学习系统的模型优化与资源管理》

文章来源：刘胜利. 无线分布式学习系统的模型优化与资源管理[D].浙江大学,2022.
这是一篇浙江大学的博士论文，2022年12月的，比较具有参考价值。

**本文可参考的点：**
全篇介绍了近年来在单层无线分布式学习系统、多层无线分布式学习系统以及去中心化无线分布式学习系统等三个场景下的相关工作。
**（1）单层无线分布式学习系统**
分布式训练机制主要有以下方案，以及其解决的问题和举例如下：
其中包括了一个**空中计算**的一些问题。（之前龙博给过这个idea）
![](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Xinyang-Zhou/Week01/pic/3.png)


**（2）去中心化无线分布式系统** 
1、网络拓扑结构影响分析
2、D2D链路选择

去中心化分布式学习系统中链路选择与资源优化本章内介绍了去中心化分布式学习的系统模型，包括学习模型和通信模型，给出了单次训练时延、能耗以及收敛速率分析，并定义了总训练开销，建立了最小化训练开销的系统优化问题。在给定的链路选择方案基础上，设计了本地算力分配、无线资源分配以及汇聚权重优化算法。
![](\pic\2.png)



### **二、下周工作计划**
继续阅读这篇博士论文，还有一些章节的idea可以参考，和师兄讨论方向。


