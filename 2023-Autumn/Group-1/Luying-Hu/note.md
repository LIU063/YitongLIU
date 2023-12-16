### Week 15
1、调研多域卫星网络  
2、学习SDSN controller placement的论文

### Week 14
调研卫星网络中边缘计算和计算卸载

### Week 13
调研SDN controller placement in Satellite network  
考虑动态网络负载和时变网络拓扑  
[1]X. Li et al., “Optimized Controller Provisioning in Software-Defined LEO Satellite Networks,” in IEEE Transactions on Mobile Computing, vol. 22, no. 8, pp. 4850-4864, 1 Aug. 2023, doi: 10.1109/TMC.2022.3155657. 二区 (上海交通大学 计算机系) 使用Mininet和ONOS  
[2]L. Chen, F. Tang and X. Li, "Mobility- and Load-Adaptive Controller Placement and Assignment in LEO Satellite Networks," IEEE INFOCOM 2021 - IEEE Conference on Computer Communications, Vancouver, BC, Canada, 2021, pp. 1-10, doi: 10.1109/INFOCOM42981.2021.9488806.  
考虑拓扑的动态变化、有限的带宽和流量的变化  
[3]J. Guo, L. Yang, D. Rincón, S. Sallent, Q. Chen and X. Liu, “Static Placement and Dynamic Assignment of SDN Controllers in LEO Satellite Networks,” in IEEE Transactions on Network and Service Management, vol. 19, no. 4, pp. 4975-4988, Dec. 2022, doi: 10.1109/TNSM.2022.3184989. 二区（国防科技大学 复杂飞行器系统仿真技术重点实验室） 使用Matlab和STK  
[4]J. Guo et al., "SDN Controller Placement in LEO Satellite Networks Based on Dynamic Topology," 2021 IEEE/CIC International Conference on Communications in China (ICCC), Xiamen, China, 2021, pp. 1083-1088, doi: 10.1109/ICCC52777.2021.9580367.

[5]	T. Das, V. Sridharan and M. Gurusamy, "A Survey on Controller Placement in SDN," in IEEE Communications Surveys & Tutorials, vol. 22, no. 1, pp. 472-503, Firstquarter 2020, doi: 10.1109/COMST.2019.2935453.	一区  
[6]J. Liu, Y. Shi, L. Zhao, Y. Cao, W. Sun and N. Kato, "Joint Placement of Controllers and Gateways in SDN-Enabled 5G-Satellite Integrated Network," in IEEE Journal on Selected Areas in Communications, vol. 36, no. 2, pp. 221-232, Feb. 2018, doi: 10.1109/JSAC.2018.2804019. 一区（西北工业大学）  

### Week 12
补充专利交底书，交接

### Week 11
准备组会PPT

### Week 10
[1]Q. Chen et al., "Latency-Optimal Pyramid-based Joint Communication and Computation Scheduling for Distributed Edge Computing," IEEE INFOCOM 2023 - IEEE Conference on Computer Communications, New York City, NY, USA, 2023, pp. 1-10, doi: 10.1109/INFOCOM53939.2023.10228964.    
分布式边缘计算中基于金字塔的延迟最优联合通信和计算调度

**背景**：近年来，**分布式边缘计算（DEC）** 已经成为一种新的计算范式，通过结合边缘计算和并行计算，可以加速边缘计算的过程。然而，现有的研究假设通信时间是固定的以及工作负载可以任意分割，限制了其实际应用的可行性和普适性。  
**论文的Motivation**: 鉴于现有研究的局限性，本文重新研究了分布式边缘计算中的最小延迟联合通信和计算调度（MLCCS）问题，考虑了通信时间的动态性和工作负载的可分割性，旨在提出更实用和通用的解决方案。    
**技术路线**：本文引入了**基于金字塔的计算模型**，计算每个设备的最优调度顺序和分配的工作负载。此外，提出了一种**近似任务分配算法**，将子任务分配给每个设备。

### Week 9
[1]Q. Liu and Z. Fang, "Learning to Schedule Tasks with Deadline and Throughput Constraints," IEEE INFOCOM 2023 - IEEE Conference on Computer Communications, New York City, NY, USA, 2023, pp. 1-10, doi: 10.1109/INFOCOM53939.2023.10228901.   
学习在截止时间和吞吐量约束下进行任务调度

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
