# Week 1(3.16-22)
## 论文扩展
### 几个粗略的想法
- 功率控制
    - 一般资源分配、功率控制是一起做的
    - Resource sharing and power allocation for D2D-based safety-critical V2X communication       
- 增加任务卸载 
    - 之前仅考虑接入网络的选择，现在还要考虑任务的卸载  
- 不同的学习算法，然后加知识驱动，进行性能比较
    - DQN、A2C 等 
    - 但需要说明选择这些算法的原因，为什么可以用于该场景  
    - 为什么可以进行比较 他们之间有什么异同  
- 资源块的传输考虑的不细致，
    - 比如考虑资源块的优先级，时延敏感性优先级更高
- 引入的知识在进行修改，知识感觉很是牵强，而且普适性很低
    - 现在已有的研究多是将已有的算法or模型当做知识—→就会存在普适性问题
    - 但是针对特定场景，普适性好像也不重要
    - 个人认为 知识应该具有普适性(至少针对一类问题而不是一个特定的问题) 
- LEO数量的增加，考虑卫星之间的连接选择( 相对来说比较复杂，建模需要考虑的因素多)
    - 卫星间切换
    - 看到有一篇还增加了GEO MEO？增加的意义是
    - LEO satellite constellation考虑之间的切换时延
    - 还要考虑卫星波束的分配   
- 无人机的轨迹控制
    - 增加轨迹控制后，无人机的拓扑发生改变，但好像这个不是研究的重点
- - - 
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
    - 概要: 利用深度强化学习优化移动网络视频流预测功率分配的策略。目标是在服务质量约束下，尽量减少视频传输的平均能耗，避免视频失速。
    - 场景: 在视频流中，用户在由一个中央单元(CU)覆盖的多个单元之间移动。
    - 目标函数
          - ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5085aaa-e784-4816-b8af-8eb96a560aea/Untitled.png)
          - 目标函数: 通过功率分配最小化平均能耗                
          - 约束: QoS约束&最大的功率约束           
    - 方法: DDPG
          - action: 分配给第i个时隙的功率 —> 每帧的目标平均速率                        
             ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f789a211-411e-4c2b-aab5-ca8972e81673/Untitled.png)                     
          - 注水算法                            
            [注水算法进行功率分配](https://zhuanlan.zhihu.com/p/502453127)                          
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc9ef1b7-60f2-4243-820f-f7b1c0b43360/Untitled.png)                 
                            一种功率分配算法，为信道条件更好的用户分配更多的功率     
                        - state: 当前和过去的大规模信道增益与其关联的BS和相邻的BS 
                            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64b741a9-d65a-4f82-a6e3-e27504cf4cf2/Untitled.png)
                            - 大尺度信道增益
                            - the large-scale channel gains in the past time steps
                            - the large-scale channel gains between the user and the other Nb-1 BSs with the largest large-scale channel gains
                            - the buffer status
                        - reward:     
                            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b86b8e7f-03b7-4b04-92d4-7e3cee52261a/Untitled.png)
                            - 传输能量消耗
                            - 下一个时隙开始时用户缓冲区中的数据量
                    - Transmission Policy Based on DDPG
                        - Architecture of the actor and critic networks
                        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ed7e1e7-8c86-4fc2-bc44-4af65b766eed/Untitled.png)        
                - 性能提升
                    - 与最优predictive resource allocation (PRA)策略进行比较
                - DRL使用方式
                    - 利用注水模型，设计神经网络架构，增加了节点，求最佳水位和基站的信道增益节点
- - - 
### 场景建模
