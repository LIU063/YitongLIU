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
