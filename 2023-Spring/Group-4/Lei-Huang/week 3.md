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
- 场景
<img src="https://github.com/loafluls/report_images/blob/main/images/NOMA%E7%B3%BB%E7%BB%9F%E6%A8%A1%E5%9E%8B.png" width = "600" height = "500" alt="波束成形" align=center />

考虑一个地面卫星综合网络的下行通信场景。每个基站配备N根天线进行下行传输，可为其覆盖半径内的用户提供服务。卫星配备M根天线，可为覆盖范围内所有用户提供下行传输。
- 问题建模      
  波束成形: 使用BeamForming可以减少能量的浪费        
<img src="https://github.com/loafluls/report_images/blob/main/images/%E6%B3%A2%E6%9D%9F%E6%88%90%E5%BD%A2.png" width = "600" height = "500" alt="波束成形" align=center />  

- 方案  
    - 协作方式:在基站的覆盖范围内就通过基站或者基站卫星协作传输，在基站的覆盖范围仅通过卫星传输     
    - 考虑指标   
            - 系统容量 : 牺牲宽带服务地面用户的部分容量，在卫星的配合下提供额外的覆盖，实现对所有用户的无缝和全面覆盖    
            - QoS     
    - 传输业务: 多媒体业务(高质量移动多媒体业务)    
    - 业务特点: 数据量大，传输需要较大的带宽    
    - 资源调度:      
      地面资源分配方案: 地面波束成型、群内功率分配和群间功率分配(功率资源、频谱资源)      
      卫星的资源分配方案：卫星波束成型和功率分配(功率资源、频谱资源)  
      
#### 2.Cooperative Transmission in Integrated Terrestrial-Satellite Networks - 2019
- 概要: 本文研究了地星综合网络中的协同传输问题，分别讨论了单播和多播两种情况  
- NOMA与OFDM的区别  
    - NOMA：非正交多址技术NOMA在发送端，不同发送功率的信号在频率完全复用，仅通过功率来区分  
    - OFDM：提供高传输数据速率, 需要克服 “信号带宽大于信道带宽”的情况  
- 场景
<img src="https://github.com/loafluls/report_images/blob/main/images/%E5%9C%BA%E6%99%AF_2023_0440_2.jpg" width = "600" height = "500" alt="场景" align=center />

- 考虑问题: 频谱共享、资源分配、最优功率分配、网络干扰(?)  
- 考虑指标: 计算复杂度  
- 方案    
     <img src="https://github.com/loafluls/report_images/blob/main/images/CTSN.png" width = "850" height = "500" alt="方案" align=center />  

    - 协作方式: 在合作单播传输方案中，地面网络基于NOMA技术为用户提供服务，而卫星为无法接入地面网络的用户提供额外的覆盖，也为超出地面网络服务能力的用户提供覆盖    
    - 考虑指标    
            - QoS   
    - 传输业务: magazine中没具体给出   
    - 业务特点: 无  
    - 资源调度: 主要调度频谱资源、功率资源   
#### 3.Delay Optimization for Cooperative Multi-Tier Computing in Integrated Satellite-Terrestrial Networks - 2023
- 概要： 本文研究了星地一体化网络中的协同多层计算，即利用设备、边缘节点和云服务器的协同来处理用户的计算任务。基于所提出的三层计算框架，我们提出了最小化网络总时延的协同边缘云卸载问题。考虑到计算任务是可分割的，提出了基于部分卸载模型的最优任务分割策略，对每个计算任务推导出封闭解。在得到最优任务分割策略后，将原优化问题重新化为时隙分配策略和计算量分配策略问题。然后，我们进一步提出了边缘云计算协同策略来优化网络的延迟性能
- 场景  
    <img src="https://github.com/loafluls/report_images/blob/main/images/%E6%98%9F%E5%9C%B0%E9%9B%86%E6%88%90%E7%BD%91%E7%BB%9C.png" width = "600" height = "500" alt="场景" align=center />
    考虑星地一体化网络，其中卫星为没有连接光纤的地区的地面基站提供回程传输。然后，地面用户可以基于传统的4G/5G技术接入基站进行通信和计算服务。  
- 建模  
    - 通信模型    
     1. User to BS: TDMA；每个用户和BS配备一根天线；基站之间相互独立无干扰  
     2. BS to Satellite: TDMA  
     3. Satellite to Cloud: 忽略从卫星到网关的传输延迟  
    - 方案
     1. 任务分割策略: 任务拆分，为所有任务找到最优的任务拆分策略  
            - 局部边缘计算的最优任务分割策略  
              
            - 局部边缘云计算的最优任务分割策略  
     2. 协作边缘计算策略
     
#### 子任务分割
