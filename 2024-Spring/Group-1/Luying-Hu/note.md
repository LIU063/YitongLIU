# 2024.4.1
## 进展  
对Digital Twin network进行调研，重点关注如何解决DT应用中存在的问题

[1]Y. Lu, S. Maharjan and Y. Zhang, "Adaptive Edge Association for Wireless Digital Twin Networks in 6G," in IEEE Internet of Things Journal, vol. 8, no. 22, pp. 16219-16230, 15 Nov.15, 2021.  考虑时延和能耗

- 我们提出了一种无线数字孪生边缘网络模型，通过将数字孪生与边缘网络集成，以实现超连接体验和低延迟边缘计算等新功能。为了在无线数字孪生网络中高效构建和维护数字孪生，我们提出了关于**动态网络状态**和不同网络拓扑结构的**边缘关联**问题。此外，根据不同的运行阶段，我们将问题分解为两个子问题，包括**数字孪生放置和数字孪生迁移**。此外，我们开发了一种基于深度强化学习（DRL）的算法来找到数字孪生放置问题的最优解，然后利用迁移学习来解决数字孪生迁移问题。    
**设备数字孪生**：是物理设备的完整复制，包含硬件配置、历史运行数据、实时状态等信息。  
**服务数字孪生**：是通过针对特定应用提取多个设备的运行状态而构建的轻量级数字副本。  

[2]Y. Tao, J. Wu, X. Lin and W. Yang, "DRL-Driven Digital Twin Function Virtualization for Adaptive Service Response in 6G Networks," in IEEE Networking Letters, vol. 5, no. 2, pp. 125-129, June 2023. 考虑成本和收益  
- 随着数字孪生资源需求的动态增长，新兴的 6G 服务需求正在迅速增长，这给数字孪生**资源管理和服务质量 （QoS） 优化**带来了挑战。我们提出了一种具有数字孪生功能虚拟化（DTFV）的新型软件定义DTN架构，用于自适应6G业务响应。   
在我们提出的DTFV（数字孪生虚拟化）中，硬件资源（例如，计算资源、存储资源）和孪生资源（例如，数据集资源、模型资源）首先从网络设备孪生中解耦。通过数据识别和模型结构分析，相似度得分最接近的资源将被放入同一个数字孪生资源池中。然后，这些虚拟化的数字孪生资源可以被智能调度以构建**虚拟数字孪生（VDT）**。  
对于每个服务请求，DTFV初始化一个VDT，该VDT关联多个基本数字孪生以响应其动态需求。

[3]Y. Zhou, R. Zhang, J. Liu, T. Huang, Q. Tang and F. R. Yu, "A Hierarchical Digital Twin Network for Satellite Communication Networks," in IEEE Communications Magazine, vol. 61, no. 11, pp. 104-110, November 2023.  
- 在卫星网络中，在线操作和快速反应严重依赖于低延迟模型同步。然而，DT模型与卫星实体之间的较长传播路径给实时模型同步带来了巨大的挑战。同时，拓扑结构可能会中断PS和DT之间的连接。在动态卫星网络中，DT必须随着物理实体的移动和环境的变化而不断演化。因此，必须解决**同步延迟大和网络动态**的问题。  
我们提出了一种分层架构HDTN-SCN，为各种应用提供差异化的数据服务。在系统中，**边缘DT**部署在分布式地面站中，为实时业务制定物理实体。因此，**中央DT**部署在集中式网络控制中心（NCC）中，以促进全局决策和优化。

## 计划
结合SDN controller placement的论文思考怎么做

# 2024.3.25
## 进展  
再细读一遍文章[2]还是没有太大启发，对Digital Twin satellite network进行调研

相关文章的重点：

0、怎么实现DT系统或DT架构？  
- 一些大论文，比较复杂，做不了

1、用DT干什么事？  
- 比如获取物理对象的信息、获取全局信息，预测未来网络状态等等，大多数只是文字描述一下使用了DT这个技术辅助完成了一些功能，但是重点不在DT上，建模中没看到有什么不一样。
- 
2、用DT时应考虑什么因素跟实际更相符？  
- 比如有篇论文是考虑了DT对CPU频率的估计偏差，建模的公式中有加入这部分。  
- 在估计SAGINs网络的当前状态时，重要的是要承认技术延迟可能会限制它们提供完全准确表示的能力。这可能会导致计算资源的计算略有差异，例如真实实体和数字实体之间的CPU频率和其他属性。然而，在优化整体延迟时，我们目前的重点是任务卸载过程。因此，我们在估计所有计算能力强的实体(包括车辆、基站和卫星)的可用CPU频率时考虑了偏差。  
- 实际计算时延与DT估计时延有差异。研究发现，数字孪生估计偏差增加会导致任务卸载延迟增加和能耗的减少。因此，在优化任务计算时，应考虑数字孪生估计偏差，以提高延迟和能耗效率。
- 
3、如何解决DT应用中存在的问题？  
- 比如有篇论文，针对构建卫星网络DT的同步时延大和网络动态问题给出了架构和解决方法。  
- 尽管DT承诺了有吸引力的愿景，但如何为卫星通信网络构建DT仍然是一个悬而未决的问题。在构建卫星网络DT的所有挑战中，同步时延是一个重要问题。在卫星网络中，在线操作和快速反应严重依赖于低延迟模型同步。然而，DT模型与卫星实体之间的较长传播路径给实时模型同步带来了巨大的挑战。同时，拓扑结构可能会中断PS和DT之间的连接。在动态卫星网络中，DT必须随着物理实体的移动和环境的变化而不断演化。因此，必须解决同步延迟大和网络动态的问题。

## 计划
1、对如何解决DT应用中存在的问题进行重点调研


# 2024.3.18
## 进展
1、参与项目书  
2、阅读论文，思考怎么把数字孪生融入到之后的工作中  
[1]X. Shen, J. Gao, W. Wu, M. Li, C. Zhou and W. Zhuang, "Holistic Network Virtualization and Pervasive Network Intelligence for 6G," in IEEE Communications Surveys & Tutorials, vol. 24, no. 1, pp. 1-30, Firstquarter 2022.  
[2]Z. Ji, S. Wu and C. Jiang, "Cooperative Multi-Agent Deep Reinforcement Learning for Computation Offloading in Digital Twin Satellite Edge Networks," in IEEE Journal on Selected Areas in Communications, vol. 41, no. 11, pp. 3414-3429, Nov. 2023.  
3、回顾强化学习，学习文章[2]的算法  
## 计划
1、搞懂文章[2]的细节，跟贺博讨论
