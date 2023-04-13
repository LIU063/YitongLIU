# Week 4(4.6-4.12)
## 论文扩展
### 调研
### 阅读论文
[1] Y. Choi, H. Kim, S. -w. Han and Y. Han, "Joint Resource Allocation for Parallel Multi-Radio Access in Heterogeneous Wireless Networks," in IEEE Transactions on Wireless Communications, vol. 9, no. 11, pp. 3324-3329, November 2010, doi: 10.1109/TWC.2010.11.100045.     
[2]Z. Jing, Q. Yang, M. Qin and K. S. Kwak, "Long Term Max-min Fairness Guarantee Mechanism: Adaptive Task Splitting and Resource Allocation in MEC-enabled Networks," 2019 IEEE 30th International Symposium on Personal, Indoor and Mobile Radio Communications (PIMRC Workshops), Istanbul, Turkey, 2019, pp. 1-6.doi: 10.1109/PIMRCW.2019.8880847.    
[3]Z. Jing, Q. Yang, M. Qin, J. Li and K. S. Kwak, "Long-Term Max-Min Fairness Guarantee Mechanism for Integrated Multi-RAT and MEC Networks," in IEEE Transactions on Vehicular Technology, vol. 70, no. 3, pp. 2478-2492, March 2021.doi: 10.1109/TVT.2021.3059944.   
[4]M. Qin et al., "Green-Oriented Dynamic Resource-on-Demand Strategy for Multi-RAT Wireless Networks Powered by Heterogeneous Energy Sources," in IEEE Transactions on Wireless Communications, vol. 19, no. 8, pp. 5547-5560, Aug. 2020.doi: 10.1109/TWC.2020.2994367.   
[5]M. Qin et al., "Service-Oriented Energy-Latency Tradeoff for IoT Task Partial Offloading in MEC-Enhanced Multi-RAT Networks," in IEEE Internet of Things Journal, vol. 8, no. 3, pp. 1896-1907, 1 Feb.1, 2021.doi: 10.1109/JIOT.2020.3015970.    
[6]X. Jiang, F. R. Yu, T. Song and V. C. M. Leung, "A Survey on Multi-Access Edge Computing Applied to Video Streaming: Some Research Issues and Challenges," in IEEE Communications Surveys & Tutorials, vol. 23, no. 2, pp. 871-903, Secondquarter 2021, doi: 10.1109/COMST.2021.3065237.    
[7]X. Jiang, F. R. Yu, T. Song and V. C. M. Leung, "A Survey on Multi-Access Edge Computing Applied to Video Streaming: Some Research Issues and Challenges," in IEEE Communications Surveys & Tutorials, vol. 23, no. 2, pp. 871-903, Secondquarter 2021, doi: 10.1109/COMST.2021.3065237.    
### 场景建模参考
Long-Term Max-Min Fairness Guarantee Mechanism for Integrated Multi-RAT and MEC Networks  
![系统模型](https://github.com/loafluls/report_images/blob/main/images/%E7%B3%BB%E7%BB%9F%E6%A8%A1%E5%9E%8B.png)  
#### 场景
- 在这个集成网络中，每个SD的用户面协议栈由一个公共的数据包数据收敛协议(PDCP)组成，该协议由多个下层RAT协议组共享。每组RAT协议由RLC (radio link control)、MAC (medium access control)和PHY (physical)协议组成。这样的协议设计可以使SDs在PDCP层执行任务拆分操作，并将子任务流映射到每个RAT对应的较低协议层。这样，SD任务可以被卸载到多个RAT基站上，并由连接的MEC服务器(MECSs)并行计算，从而提高任务的卸载和计算效率。   
- 考虑一个集成的多RAT和MEC网络，其中一组N个SD和一组M个配备不同RAT的基站分布在一个服务区域内。每个RAT基站都是附带一个MECS，用于从SD中卸载的计算任务。SD被赋予了多RAT能力，因此它们可以同时与多个RAT基站保持连接，并将任务并发地卸载到附加的MECSs上。    
#### 任务分割模型
- 从每个SD n的应用层生成A_n(t)∈[0,A_max_n]个任务，A_n(t)是一个独立同分布(i.i.d)随机过程。  
- 假设任务是细粒度的和数据分区的，因此它们可以被任意分割成几个比例/段，并独立并行地计算。  
![分割](https://github.com/loafluls/report_images/blob/main/images/%E5%88%B0%E8%BE%BE%E7%9A%84%E4%BB%BB%E5%8A%A1.png)  
拉格朗日乘子，用于放松约束；任务积压量；虚拟队列积压  
#### 上行传输模型
![传输](https://github.com/loafluls/report_images/blob/main/images/%E9%80%9F%E7%8E%87.png)  
- 采用OFDMA，不同RAT上的数据信号一般调制在不同的频谱上，子载波之间不存在重叠  
- 在OFDMA系统中，任何子载波只能专门分配给一个SD  
#### 任务计算模型
- MECSs接收到卸载的任务后，将CPU计算频率分配给SDs进行任务计算  
- 能被MEC服务器计算的任务量:   
![计算](https://github.com/loafluls/report_images/blob/main/images/%E4%BB%BB%E5%8A%A1%E8%AE%A1%E7%AE%97.png)  
#### 任务排队模型
![排队](https://github.com/loafluls/report_images/blob/main/images/%E6%8E%92%E9%98%9F%E6%A8%A1%E5%9E%8B.png)  
任务积压量；任务处理量；任务到达量  

---
# Week 3(3.30-4.5)
## 场景建模
### 协作传输调研
Note: 主要关注
1. 现在协作传输做到什么程度
2. 研究的场景
3. 传输的业务
4. 调度的资源类型  
### 参考文献  
[1].X. Zhu, C. Jiang, L. Kuang, N. Ge and J. Lu, "Non-Orthogonal Multiple Access Based Integrated Terrestrial-Satellite Networks," in IEEE Journal on Selected Areas in Communications, vol. 35, no. 10, pp. 2253-2267, Oct. 2017, doi: 10.1109/JSAC.2017.2724478.  
[2].X. Zhu, C. Jiang, L. Kuang, N. Ge, S. Guo and J. Lu, "Cooperative Transmission in Integrated Terrestrial-Satellite Networks," in IEEE Network, vol. 33, no. 3, pp. 204-210, May/June 2019, doi: 10.1109/MNET.2018.1800164.  
[3].X. Zhu and C. Jiang, "Delay Optimization for Cooperative Multi-Tier Computing in Integrated Satellite-Terrestrial Networks," in IEEE Journal on Selected Areas in Communications, vol. 41, no. 2, pp. 366-380, Feb. 2023, doi: 10.1109/JSAC.2022.3227083.  
[4].Z. Liu, Y. Yang, K. Wang, Z. Shao and J. Zhang, "POST: Parallel Offloading of Splittable Tasks in Heterogeneous Fog Networks," in IEEE Internet of Things Journal, vol. 7, no. 4, pp. 3170-3183, April 2020, doi: 10.1109/JIOT.2020.2965566.  
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
    - 方案 (公式推导)
     1. 任务分割策略: 任务拆分，为所有任务找到最优的任务拆分策略    
            - 局部边缘计算的最优任务分割策略    
            - 局部边缘云计算的最优任务分割策略    
            上述两种策略用于讨论κ n,k的不同值来解决任务分割问题  
            - 最优任务分割策略  
     2. 协作边缘计算策略  
            - 粒子群算法： 粒子群优化(PSO)算法，传统优化算法  
            - 协同边缘云计算策略: 通过比较系统总时延的性能，更新各粒子的局部最优位置和全局最优位置  
     
#### 下周计划  
学习任务拆分问题解决策略[4]  

# Week 2(3.23-29)
## 论文扩展
### 调研
多路径技术
1) MPTCP  
MPTCP本质缺陷：  
- 内核实现、无法为应用场景提供定制优化
- 异构网络：MPTCP的多路聚合效果并不理想，由于在公网上传输多路径是异构的，5G/LTE和Wi-Fi的时延差异较大，此时就会发生多路径的队头阻塞问题（MP-HOL）。
- 流量成本：为了克服异构网络问题，有一些多路径传输方案选择发送冗余包去避免多路队头阻塞问题，但是又引入了两个新问题：重复发送数据包会极大的增加额外的数据流量成本;冗余数据包也会占用带宽资源，这又降低了整体的带宽利用效率。  
2) MPUDP  
UDP不保证数据包传递的可靠性，因此多路的时延不同会给上层应用带来大量的乱序包，并且UDP也不对丢包进行恢复，所以目前几乎很少被使用。  
3) MPRTP  
MPRTP在将数据包分配到各个路径时，依赖于各路径的带宽和时延精确估计，可是除非拥有大量物理层信息，LTE信号的预测本身就是一个非常难以解决的问题  
4) XLINK  
Zhilong Zheng, Yunfei Ma, Yanmei Liu, Furong Yang, Zhenyu Li, Yuanbo Zhang, Jiuhai Zhang, Wei Shi, Wentao Chen, Ding Li, Qing An, Hai Hong, Hongqiang Harry Liu, and Ming Zhang. 2021. XLINK: QoE-driven multi-path QUIC transport in large-scale video services. In Proceedings of the 2021 ACM SIGCOMM 2021 Conference (SIGCOMM '21). Association for Computing Machinery, New York, NY, USA, 418–432. https://doi.org/10.1145/3452296.3472893  
XLINK技术基于QUIC协议在用户态实现了WiFi/LTE/5G的多路径并行传输，有效提升传输带宽，大幅度降低传输时延与卡顿率，在高移动性场景展现出优秀的传输稳定性。  
XLINK与之前所有多路径技术最大的不同是，它直接利用应用的QoE信息实现路径的选择、切换与调度策略。从技术角度来说，XLINK突破了传统多路径协议的设计框架，在QUIC用户态特性的基础之上，提出了Client-Server QoE反馈驱动多传输调度方案，克服了的两大难题：  
•	多路队头阻塞问题带来的传输失速和聚合效率降低的问题
•	冗余数据包发送引入的高昂额外带宽成本与流量开销问题  
XLINK的整体架构如下图所示，
![XLINK的整体架构](https://github.com/loafluls/report_images/blob/main/images/XLINK%E7%9A%84%E6%95%B4%E4%BD%93%E6%9E%B6%E6%9E%84.png)
具有以下几个特点：
- 用户态部署
- 高性能
- 低成本
- 轻量化

结果: XLINK已经集在在手淘完成了大规模灰度验证，测试结果表明，XLINK在弱网下使用可以实现短视频分片平均下载耗时减少15.03%，视频分片下载弱网耗时降低25.28%。此外，在旅途中，XLINK的用户可以同时利用WiFi热点与手机LTE，在高移动性场景下仍然保持流畅的视频观看体验。


### 场景建模
#### SAGIN 车载业务分包传输
![场景建模](https://github.com/loafluls/report_images/blob/main/images/%E5%BB%BA%E6%A8%A1%E5%9C%BA%E6%99%AF.png)
由基站网络、无人机网络、近地低轨卫星网络共同组成空天地一体化网络，以提供偏远山区的网络无缝覆盖，并保障不同类型车辆业务的传输。  
车辆按照轨迹行驶，在行驶过程中，有三种类型的业务以泊松分布的形式到达车辆等待上行传输和卸载，车辆进行接入网络的选择。考虑到SAGIN中无人机、BS和LEO卫星的传输计算功能，车辆业务可以选择在一个网络上单独进行传输或者由多个不同的网络协作传输，以最小化业务延迟。  
业务到达车辆后进行业务分包，然后每个包可选择不同的传输方式，即通过UAV，BS或者LEO网络单独传输，包会被传输到核心网进行任务卸载。  
#### 分包传输
车载业务通过不同的接入进行数据包的协作传输  
- 面临问题: The delay of HoL  
- 工作概要: 接入选择+任务卸载(统一卸载到核心网上) — 信道分配 + 功率控制  
#### 在原本的基础上将场景复杂化
- LEO层: 考虑多颗卫星->卫星间的接入选择与切换->时延更明显
- UAV层: 无人机皆匀速，拓扑简单
- BS层: 数量增加，但覆盖的疏密程度不变，整体背景依旧为偏远山区
- Vehicle: 数量更多(现实生活中偏远山区的车流量本身就比较稀疏)
- 业务: 业务类型，尽可能有更多协作传输搭配，且设计的搭配之间的差距较明显  
   问题 : 如何区分不同业务: 对时延容忍度不同，紧急程度不同  
          新业务泊松分布到达
- 指标: delay(传输时延、卸载时延)；增加 cost = 传输数据费用；增加能耗 = 主要与功率相关，增加功控后可考虑

#### 算法 DRL(A3C)
- State – 信道状态、(考虑更细粒度的状态)重传包个数、传输时延(车辆到接入网、接入网到核心网(还包括传输失败重新传输的时延))、卸载时延(处理时延)
- Action – 接入网络的子信道选择(子流接口?)，功率分配
- Reward – 时延，传输数据费用，能耗(可先单独考虑不同的指标出结果图，最后可进行指标的综合考虑(对不同的指标进行加权))

### 使用的知识
- 频谱相关性知识 ->信道选择
- 通信相关的数学知识->奖励重塑

### 场景改进
1. 协作传输决策  
目标: 最小化时延  
初步想法: 一个业务分成三个包(按照一定比例 不均等分)每个包占用接入网络的一个子信道
2. 资源分配  
主要考虑信道资源与功率资源的分配  
考虑过程的完整性与合理性: 原来的工作只考虑了业务进行上行传输，在扩展的工作中考虑业务传输并卸载到BS/UAV/LEO上。 
3. 注意考虑极端场景的合理性，当车辆比较密集。例如有多车辆接入同一个基站，出现竞争，导致有些车载业务的某些包无法被服务，导致整体业务延迟到达(时延按照最后一个包到达的时间来计算)，该情况下分包传输可能会导致系统的整体性能下降。  
3. 说明multi-agent多智能体的工作量  
### 讨论确定future work
- 调研一辆车做接入选择、资源分配的工作: 主要关注他们做的什么场景，传输的什么业务，分配的资源类型
- 协作传输的工作进展：是否有做过的，如果有，关注同类工作研究的场景


# Week 1(3.16-22)
## 论文扩展
### 协作传输
- 多径协同
    - 关于quic
          - QUIC本质上是一个灵活的Reliable / Unreliable传输协议框架
    - 多路径传输技术Multi-path QUIC
          - 多通道（Multipath）技术的核心在于通过多条（物理）链路来保障网络通信的可靠性和稳定速率
          - 将QUIC和多路径技术进行结合，也就是多路径QUIC（Multipath QUIC）
          - Multipath QUIC是实现在QUIC传输层内部的多路径协议栈。相较于在应用层建立多条连接并在应用层进行分配流量和调度的方案，在协议栈内部实现多路径的好处是对于应用层透明，使用方便；同时多路径packet调度需要紧密结合路径传输层的信息（RTT/丢包率等测量信息），这在应用层也是很难做到的。相较于传统的内核态多路径解决方案MPTCP，Multipath QUIC也有易于部署迭代等优势，同时作为用户态协议栈，也更容易结合应用层需求进行调度算法的优化
- 车联网中的分包传输
   - 基于RL的星地融合网络（ISTN）中车辆数据与计算卸载方法研究-吴申师兄
        
         - 基于DDPG的ISTN车辆低成本数据卸载方法(DDPG)            
            
             - 卫星和地面蜂窝网络会协作卸载用户请求的数据            
             
             - 数据卸载队列根据紧急程度递减排列            
             
             - 考虑时间成本            
   - 注意子队列的更新: 对于那些需要立即卸载的数据，优先通过基站卸载。如果不在基站覆盖范围内则应该使用LEO进行卸载。对于不需要立即卸载的数据，可以等到车辆移动到基站覆盖范围内可以接收到基站信号时再进行卸载，这样可以节省许多的数据传输费用。
   - ![子队列更新公式](https://github.com/loafluls/report_images/blob/main/images/%E5%AD%90%E9%98%9F%E5%88%97%E6%9B%B4%E6%96%B0%E5%85%AC%E5%BC%8F.png)
- - - 
### Yangchen Yang团队工作调研
- Yangchen Yang 团队工作调研
  > Energy-Saving Predictive Video Streaming with Deep Reinforcement Learning
    >> 概要: 利用深度强化学习优化移动网络视频流预测功率分配的策略。目标是在服务质量约束下，尽量减少视频传输的平均能耗，避免视频失速。  
    >> 场景: 在视频流中，用户在由一个中央单元(CU)覆盖的多个单元之间移动。  
    >> 目标函数  
          - ![目标函数](https://github.com/loafluls/report_images/blob/main/images/yangchen%20yang%E7%9B%AE%E6%A0%87%E5%87%BD%E6%95%B0.png)  
          - 目标函数: 通过功率分配最小化平均能耗  
          - 约束: QoS约束&最大的功率约束           
    >> 方法: DDPG  
          >>> action: 分配给第i个时隙的功率 —> 每帧的目标平均速率                                       
              注水算法: 一种功率分配算法，为信道条件更好的用户分配更多的功率     
          >>> state: 当前和过去的大规模信道增益与其关联的BS和相邻的BS 
              - 大尺度信道增益  
              - the large-scale channel gains in the past time steps  
              - the large-scale channel gains between the user and the other Nb-1 BSs with the largest large-scale channel gains  
              - the buffer status  
           >>> reward:     
              - 传输能量消耗  
              - 下一个时隙开始时用户缓冲区中的数据量  
     >> Transmission Policy Based on DDPG  
           - Architecture of the actor and critic networks   
             ![PDS-DDPG架构](https://github.com/loafluls/report_images/blob/main/images/Architecture%20of%20the%20actor%20and%20critic%20networks.png)          
     >> 性能提升: 与最优predictive resource allocation (PRA)策略进行比较
     >> DRL使用方式: 利用注水模型，设计神经网络架构，增加了节点，求最佳水位和基站的信道增益节点
- - - 
### 下周工作计划
1.确定场景建模

2.完成安全层的调研
### 6G大会思考
大会中讲到未来6G星地融合是多个异构接入网络的一体融合，具有多层立体、动态时变的特点，多层复杂跨域组网导致网络架构设计困难，大尺度空间传播环境导致传输效率低，卫星的高速运动会导致网络拓扑高动态变化，进而导致业务质量难以保障。未来的空天地方向的研究可以就上述星地融合的网路特点，卫星网络的高动态拓扑变化进行深入研究。
