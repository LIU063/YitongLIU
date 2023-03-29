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
   - ![子队列更新公式](桌面)
- - - 
### Yangchen Yang团队工作调研
- Yangchen Yang 团队工作调研
  > Energy-Saving Predictive Video Streaming with Deep Reinforcement Learning
    >> 概要: 利用深度强化学习优化移动网络视频流预测功率分配的策略。目标是在服务质量约束下，尽量减少视频传输的平均能耗，避免视频失速。  
    >> 场景: 在视频流中，用户在由一个中央单元(CU)覆盖的多个单元之间移动。  
    >> 目标函数  
          - ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5085aaa-e784-4816-b8af-8eb96a560aea/Untitled.png)  
          - 目标函数: 通过功率分配最小化平均能耗  
          - 约束: QoS约束&最大的功率约束           
    >> 方法: DDPG  
          >>> action: 分配给第i个时隙的功率 —> 每帧的目标平均速率                        
              ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f789a211-411e-4c2b-aab5-ca8972e81673/Untitled.png)                     
              注水算法                            
              [注水算法进行功率分配](https://zhuanlan.zhihu.com/p/502453127)                          
              ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc9ef1b7-60f2-4243-820f-f7b1c0b43360/Untitled.png)                 
              一种功率分配算法，为信道条件更好的用户分配更多的功率     
          >>> state: 当前和过去的大规模信道增益与其关联的BS和相邻的BS 
             ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64b741a9-d65a-4f82-a6e3-e27504cf4cf2/Untitled.png)  
              - 大尺度信道增益  
              - the large-scale channel gains in the past time steps  
              - the large-scale channel gains between the user and the other Nb-1 BSs with the largest large-scale channel gains  
              - the buffer status  
           >>> reward:     
             ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b86b8e7f-03b7-4b04-92d4-7e3cee52261a/Untitled.png)  
              - 传输能量消耗  
              - 下一个时隙开始时用户缓冲区中的数据量  
     >> Transmission Policy Based on DDPG
           - Architecture of the actor and critic networks  
             ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ed7e1e7-8c86-4fc2-bc44-4af65b766eed/Untitled.png)          
     >> 性能提升: 与最优predictive resource allocation (PRA)策略进行比较
     >> DRL使用方式: 利用注水模型，设计神经网络架构，增加了节点，求最佳水位和基站的信道增益节点
- - - 
### 下周工作计划
1.确定场景建模

2.完成安全层的调研
### 6G大会思考
大会中讲到未来6G星地融合是多个异构接入网络的一体融合，具有多层立体、动态时变的特点，多层复杂跨域组网导致网络架构设计困难，大尺度空间传播环境导致传输效率低，卫星的高速运动会导致网络拓扑高动态变化，进而导致业务质量难以保障。未来的空天地方向的研究可以就上述星地融合的网路特点，卫星网络的高动态拓扑变化进行深入研究。

# Week 2(3.23-29)
## 论文扩展
### 调研
多路径技术
1) MPTCP
MPTCP本质缺陷：
	内核实现、无法为应用场景提供定制优化
	异构网络：MPTCP的多路聚合效果并不理想，由于在公网上传输多路径是异构的，5G/LTE和Wi-Fi的时延差异较大，此时就会发生多路径的队头阻塞问题（MP-HOL）。
	流量成本：为了克服异构网络问题，有一些多路径传输方案选择发送冗余包去避免多路队头阻塞问题，但是又引入了两个新问题：
1.重复发送数据包会极大的增加额外的数据流量成本。
2.冗余数据包也会占用带宽资源，这又降低了整体的带宽利用效率。
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

具有以下几个特点：
	用户态部署
	高性能
	低成本
	轻量化

结果: XLINK已经集在在手淘完成了大规模灰度验证，测试结果表明，XLINK在弱网下使用可以实现短视频分片平均下载耗时减少15.03%，视频分片下载弱网耗时降低25.28%。此外，在旅途中，XLINK的用户可以同时利用WiFi热点与手机LTE，在高移动性场景下仍然保持流畅的视频观看体验。


### 场景建模
#### SAGIN 车载业务分包传输
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

