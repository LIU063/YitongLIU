# Week 3
## 场景建模
### 协作传输调研
Note: 主要关注
1. 现在协作传输做到什么程度
2. 研究的场景
3. 传输的业务
4. 调度的资源类型
#### 1. Non-Orthogonal Multiple Access Based Integrated Terrestrial-Satellite Networks - 2017  
- 概要: 研究了基于非正交多址(NOMA)的地面-卫星综合网络的下行传输，其中基于NOMA的地面网络和卫星合作为地面用户提供覆盖，同时重用整个带宽
- 系统模型
![系统模型](https://github.com/loafluls/report_images/blob/main/images/NOMA%E7%B3%BB%E7%BB%9F%E6%A8%A1%E5%9E%8B.png)
- 问题建模  
  波束成形: 使用BeamForming可以减少能量的浪费
  ![波束成形](https://github.com/loafluls/report_images/blob/main/images/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.png)
- 场景

- 方案
![方案](https://github.com/loafluls/report_images/blob/main/images/CTSN.png)
    - 协作方式  
    - 考虑指标  
            - 系统容量 : 牺牲宽带服务地面用户的部分容量，在卫星的配合下提供额外的覆盖，实现对所有用户的无缝和全面覆盖  
            - QoS   
    - 传输业务: 多媒体业务(高质量移动多媒体业务)  
    - 业务特点: 数据量大，传输需要较大的带宽  
#### 2.Cooperative Transmission in Integrated Terrestrial-Satellite Networks - 2019
- NOMA与OFDM的区别
    - NOMA - 非正交多址技术NOMA在发送端，不同发送功率的信号在频率完全复用，仅通过功率来区分
    - OFDM - 为提供高传输数据速率，3G和4G蜂窝网络均为宽带通信系统。很明显，宽带通信系统需要克服 “信号带宽大于信道带宽”的情况
- 考虑问题: 频谱共享、资源分配、最优功率分配、网络干扰(?)
- 考虑指标: 计算复杂度
- 方案
#### 3.Delay Optimization for Cooperative Multi-Tier Computing in Integrated Satellite-Terrestrial Networks
- 概要： 本文研究了星地一体化网络中的协同多层计算，即利用设备、边缘节点和云服务器的协同来处理用户的计算任务。基于所提出的三层计算框架，我们提出了最小化网络总时延的协同边缘云卸载问题。考虑到计算任务是可分割的，提出了基于部分卸载模型的最优任务分割策略，对每个计算任务推导出封闭解。在得到最优任务分割策略后，将原优化问题重新化为时隙分配策略和计算量分配策略问题。然后，我们进一步提出了边缘云计算协同策略来优化网络的延迟性能
- 场景
 ![场景](https://github.com/loafluls/report_images/blob/main/images/%E6%98%9F%E5%9C%B0%E9%9B%86%E6%88%90%E7%BD%91%E7%BB%9C.png)
- 建模  
    - 通信模型    
     1. User to BS: TDMA，每个用户和BS配备一根天线；基站之间相互独立无干扰  
     2. BS to Satellite: TDMA  
     3. Satellite to Cloud: 忽略从卫星到网关的传输延迟  
    - 计算模型  
     1. Task Model:  
     2. Offloading Model:  
    - 问题建模  
    - 方案
     1. 任务分割策略  
            - 局部边缘计算的最优任务分割策略  
            - 局部边缘云计算的最优任务分割策略  
     2. 协作边缘计算策略  
    - 场景研究
