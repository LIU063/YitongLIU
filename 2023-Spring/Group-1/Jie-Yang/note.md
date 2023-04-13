## Date: 2023/3/23
## 周工作汇报
### 1.总结了（流量均衡算法）路由性能的评价指标：      
1. 考察流量在网络中的分散程度，引入流量分散指数.   
![流量分散指数公式](https://user-images.githubusercontent.com/83910735/226950801-320b70ed-dd47-42b2-a484-da99cfd3ea67.png)   
其中，ｎ代表了星间链路数量，代表仿真时间内经过第i条星间链路的总数据包数。ＴＤＩ的取值范围为０到１，越大的ＴＤＩ值代表流量在网络中更加分散，越小的ＴＤＩ值代表流量在网络中更加集中。
2. 网络平均时延(根据网络所有端到端通信时延求平均而得)   
3. 网络丢包率   
4. 路由震汤（路由调整次数）   
5. 通信开销   
6. 传统路由评价指标如端到端时延，网络平均时延，网络丢包率等都只属于“黑箱”式的评价指标，它们只能从网络外部（总体业务影响上）对路由算法的整体性能做出解释，但是无法从网络内部揭示算法性能变化的真正原因。同时，这些传统路由评价指标往往是一段时间的统计结果，异常路径评价指标，重点放在分析它们在故障情况下的抗毁性能表现[1]     
7. 吞吐量  
### 2.查阅了几篇卫星网络路由算法的文章：       
1. 全局一局部混合策略的卫星网络流量均衡技术ＨＧＬ算法的设计分两个步骤来实现。第一步，ＨＧＬ算法根据星间大尺度的流量需求变化基线，采用全局策略，在全网范围上完成最优的流量初步分配。这一阶段的最优流量分配问题被建模为一个求网络总流量成本最小化的多商品流优化问题。在第二步，ＨＧＬ针对不可预测的突发流量波动，采用局部策略，完成实时的路由调整。在这个阶段，当一颗卫星检测到其某条链路的缓冲队列占用率超过一定阈值时，它将显式地通知其上游卫星分流一部分流量到其他卫星。[1]   

2. 针对大规模单层 LEO 极轨道宽带卫星网路提出了一种面向单播应用的路由算法无关多径的单播路由算法-NDM。（是静态路由）该算法通过离线方式查找源卫星节点到目的卫星节点最多三条不相关路径。通过对卫星节点拥塞程度的划分，设计网络在非拥塞区选择主路径进行数据传输，进入轻度拥塞状态后，源节点选择一条备份路径进行数据的并行传输，进入重度拥塞或者节点失效时，将原有主路径断开，此时源节点采用剩余所有备份路径进行数据并行重传（这些路径是距离最短路径）。特点就是在地面计算好路径上传到卫星，节省传输数据时寻找路径的时间，其次使用了大规模的星座来仿真（Teledesic 星座288颗卫星）。   

3. 最小动态成本（Minimal Dynamic Cost  ，MDC）单播路由算法。（是动态路由）MDC 算法最终目标是找出一条实时的最短时延路径。MDC单播路由算法充分考虑到数据排队时延、节点处理时延和路径传播时延，将卫星从源节点到目的节点传输数据所带来的时延（该路径上所有卫星节点排队时间、数据处理时间和星间链路传播时间的总和转化为所消耗的成本，则成本最小的路径作为数据的传输路径。）转化为动态成本，并在路由发现的过程中设定最小跳数洪泛区域，大大减小不必要的资源浪费，通过引入M/M/1/k 模型设定可以容忍的丢包概率计算每颗卫星节点缓冲区域排队阈值，从而减少丢包现象的发生。   

4. 组播路由是多颗卫星之间。而实现卫星组播路由的核心是构建一颗以卫星组播源点为根、组成员为树节点或叶节点的组播树，从而尽可能共享传输路径，降低总宽带占用，从而完成单点到多点的实时通信。该算法利用卫星组成员的分布情况，将LEO极轨星座模型简化为曼哈顿街区网络，最不存在路径绕远的相邻象限聚合成簇，从而将组成员划分为两个簇。其中每个簇选择一颗卫星作为簇头，将簇头作为次源点，以该次源点为根节点逐步生成组播树，同时簇头负责簇内组成员的管理工作并直接与源节点进行信息交互，但是基于源点的组播树构建并不等价于基于中心节点的组播树构建。该算法采用分布式概念，分担源节点的管理压力，降低计算复杂度,并通过设定优先级尽可能避免组播绕路，提高链路共享率。[2]   
[[1]刘子鸾. 卫星网络路由与流量控制关键技术研究[D].北京邮电大学,2018.](https://doi.org/10.1177/1550147717692586)  
[[2]朱晓攀.大规模低轨宽带卫星网络路由关键技术研究[D].中国科学院大学,2020.](DOI:10.27562/d.cnki.gkyyz.2020.000061)
 
 
## 6G大会：
### 动态拓扑和路由算法：
1.预测性路由   
2.卫星跨层之间连接   


## Date: 2023/3/30
## 周工作汇报
### 1.卫星网络路由算法的文章： 
1.针对低地球轨道卫星网络，该文作者提出了基于分段路由的负载均衡路由算法。该算法考虑了全球流量的地理分布不均匀性，改善了在有限区域内布置网关造成的网络拥塞。该算法参考SR，动态划分轻载区和重载区。预平衡最小生成树是轻负载区路由的基础，而重负载区路由是指基于拥塞指数的最小权重路径。仿真结果表明，在Walker星座下，随着重负载区大小的增大，平均拒绝比、平均相对吞吐量和最大链路利用率均有提高，但是，规模增加时，平均时延和资源消耗会增加，在重负载区规模较小阶段，避免拥堵的性能不好。该算法的切入点是流量返回，但只考虑网络的即时信息，没有利用网络历史信息。[1]    

2.LEO卫星网络提出了许多路由算法，但它们在应用于巨型星座时可能会面临可扩展性问题。对于数百到数千颗卫星，路由算法需要高效。在本文中，作者提出了一种面向倾斜轨道的巨型星座的分布式可生存路由算法，该算法包括基本的X-Y路由算法、故障恢复机制、部分记录环路避免机制和基于矢量的下一跳选择机制，具体为：   
a.识别并形式化了倾斜星座中由平面间 ISL 形成的螺旋形状。基于这一拓扑特性，提出了一种针对倾斜星座的基本X-Y路由算法。每颗卫星利用网络拓扑的规律性独立选择通往每个目的地的多个主路径和辅助路径。    
b.提出一种故障恢复机制来处理链路故障，该机制由受限泛洪机制和预绕行机制组成。通过在数据包中添加生存时间 （TTL） 字段以及卫星维护一个状态变量指示此路径上断开的链接数来实现。   
c.提出一种部分记录环路避免机制来处理路由过程中的环路。在此机制中，数据包遍历的卫星仅在必要时记录在数据包标头中。每个数据包包含一个字段，指示记录的节点数，并在其标头中包含卫星 ID 列表。    
d.该文提出一种基于矢量的下一跳选择机制，a） 是否已遍历下一跳，b） 下一跳是否是回溯节点，c） 方向是否为主方向，d） 路径是否有断开的链接，每一个为一个变量，变量值为0或1，根据此确定评估向量，选择最大的为最终的方向。    
e.仿真是在Starlink的第一阶段星座上进行的，本文详细说明了仿真使用到的各种参数值。仿真结果表明，所提路由算法能够降低信令开销，减少链路故障时的端到端延迟。[2]   
### 2.卫星网络技术研究方向：
1.基于人工智能的卫星路由   
2.基于多层网络的卫星路由   
3.基于SDN的卫星路由    
4.预测性路由：与传统的路由和转发机制不同，预测性路由的网络节点不是通过洪泛来指示拓扑变化，而是定期切换路由表来反映不同时间点下网络拓扑的变化。   
5.每个卫星只能有两条轨内和两条轨间星间链路。这极大地限制了整个网络的通信能力，无法实现最佳带宽和最低时延。因此，新一代路由算法可以允许卫星之间的星座连接更加灵活和自由（如跨层连接）    
[[1]W. Liu, Y. Tao and L. Liu, "Load-Balancing Routing Algorithm Based on Segment Routing for Traffic Return in LEO Satellite Networks," in IEEE Access, vol. 7, pp. 112044-112053, 2019](https://sci-hub.wf/10.1109/ACCESS.2019.2934932)        
[[2]X. Qi, B. Zhang and Z. Qiu, "A Distributed Survivable Routing Algorithm for Mega-Constellations With Inclined Orbits," in IEEE Access, vol. 8, pp. 219199-219213, 2020](https://sci-hub.wf/10.1109/ACCESS.2020.3041346)    
    
    
## Date: 2023/4/5
## 周工作汇报
### 1.6G PPT：
### 2.基于人工智能的路由算法：
1.基于树突神经网络的低轨卫星（Low-Earth orbit，LEO）智能感知路由算法[1]。本文所设置的低轨卫星网络基本星座构型为Walker（64/8/1)，本文算法主要分为三个阶段：星间链路态势感知阶段、星间链路质量感知阶段、路由决策阶段该算法。   
a.首先利用蚁群算法做出路由选择，收集输出结果，进而构造训练集，训练树突神经网络（Dendrite net，DD）。
b.在星间链路态势感知阶段，对卫星之间的可视性约束（几何可视和天线可视）进行分析，以此为前提得出当前时刻各个卫星之间的建链状态；设置链路监测周期，周期性获取星间链路的建链情况；   
c.在神经网络链路质量感知阶段，将卫星节点之间的距离、时延、时延抖动、丢包率等链路状态信息作为树突网络的输入参数，训练好的树突神经网络通过对链路状态信息进行处理，输出满足多种QoS因素的下一跳路由选择的评估值矩阵；      
![image](https://user-images.githubusercontent.com/83910735/230129371-0c5e9f5a-b7b8-4695-a9db-f2c55a2b8416.png)    
d.在路由决策阶段将评估值矩阵的倒数作为邻接矩阵通过迪杰斯特拉（Dijkstra）算法，得出源节点和目的节点之间的初始路径；最后周期性监测卫星网络拓扑，实时修正初始路径。    
![image](https://user-images.githubusercontent.com/83910735/230129485-67455bd9-fe46-48ad-998d-851458c0e31a.png)    
路由算法与智能感知技术融合，可以提升路由的分析和决策能力，但当卫星网络规模较大时，很难直接输出满足复杂约束的路径，会导致算法收敛时间较长.     

2.针对卫星互联网的智能路由问题利用基于双延迟深度确定性策略梯度的深度强化学习算法，解决网络的实时路由优化问题[2]。提出一种卫星互联网的智能化架构:    
![image](https://user-images.githubusercontent.com/83910735/230129726-7257ae8b-09a7-4ca3-8c9c-47fc542498a7.png)    
a.数据平面。数据平面中的无线感知模块包含多种无线网络接入方法，用于感知卫星互联网中各个终 端设备生成的数据。该模块收集大量环境数据，并使用它们预测网络流量。    
b.控制平面。控制平面包含部署在地面网络中心和卫星的控制器，实现网络的集中管理和控制。   
d.智能平面。智能平面是整个智能化架构的大脑，负责根据当前的网络状态需求，实时捕获网络信息，并有效地调整网络资源的分配。   
e.应用平面。应用平面主要为各种应用程序提供 定制的程序接口，以确保功能的高效运行。    
提出了TD3算法作为DRL路由优化算法的一种，可以处理高维的输入和连续状态空间，TD3算法在采用传统Actor-Critic（演员-评论家） 强化学习架构的基础上，增加了一个Critic网络，组成包含一个Actor和两个Critic的强化学习架构，Actor使用策略梯度方法根据状态拟合策 略函数来选择动作，两个Critic则根据当前的状态对Actor 做出的动作进行评估，并选取两个Critic网络表示的Q值 中较小的那一个作为Q函数更新的目标。    
![image](https://user-images.githubusercontent.com/83910735/230130330-e9ddab5e-a0ea-4c46-ad8c-108f47de731f.png)     
3.基于深度强化学习的低地球轨道卫星智能路由算法（DQN-IR）。本文重点探索并提出了一种利用深度强化学习模型的仅依赖于周围卫星节点状态的智能分散路由算法（一个卫星只能获得周围的四颗卫星的状态）。该算法不需要设置额外的分类阈值或使用历史信息预测链路的状态。该算法基于准静态卫星拓扑（即拓扑快照）的假设和虚拟拓扑路由的思想.     
a.state:    
![image](https://user-images.githubusercontent.com/83910735/230261741-039e09c7-7bc5-4143-882f-0fbe710d9f53.png)     
b.action:    
![image](https://user-images.githubusercontent.com/83910735/230261772-b521b90e-68c6-47e1-8d3f-30338b3e2547.png)    
c.reward:     
![image](https://user-images.githubusercontent.com/83910735/230261796-a8690a09-5059-4061-95ce-f16c57e478dc.png)     
而所提出的DQN-IR算法通过在传统的DQN算法的基础上更新目标网络的参数来改进该方法，这可以描述如下。每次训练结束后，它将记录传输路径的总奖励。如果当前的总奖励高于之前的所有奖励，这意味着当前的传输路径是最优的。此时，将主网络的参数复制到目标网络中。同时，为了防止目标网络的参数更新过频繁，本文将计数器n设为0。    
![image](https://user-images.githubusercontent.com/83910735/230261880-9e017b76-b645-462a-939c-0eefe8b859f6.png)     
和其他两种贪婪算法对比，一种以距离为参考因素，一种对路由节点的带宽、信噪比、排队延迟、距离等因素设置固定的权值，并通过其加权和选择路由。      
[[1]刘洋,王丽娜.基于树突神经网络的低轨卫星智能感知路由算法[J].工程科学学报,2023,45(03):465-474.](https://doi.org/10.13374/j.issn2095-9389.2021.11.08.007)        
[[2]魏琳慧,刘国文,刘雨等.基于深度强化学习的卫星互联网路由优化研究[J].天地一体化信息网络,2022,3(03):65-71.](https://kns.cnki.net/kcms2/article/abstract?v=BBImVa1ypluYanXXTHQJguCA5_YZvQ7qY9CRXiGgX9FIdy3qMu3Z9vd8CaW2gbXIRDEQWscWY5za7TScPjzZVkIlydusfKS8nISRwX20CZgkmzWSs0GcE3gkydAOvJvN&uniplatform=NZKPT&language=CHS)        
[[3]NI Shaojie, YUE Yang, ZUO Yong, LIU Wenxiang, XIAO Wei, YE Xiaozhou. The Status Quo and Prospect of Satellite Network Routing Technology[J]. Journal of Electronics & Information Technology, 2023, 45(2): 383-395.](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT211393)        
[[4]P. Zuo, C. Wang, Z. Yao, S. Hou and H. Jiang, "An Intelligent Routing Algorithm for LEO Satellites Based on Deep Reinforcement Learning," 2021 IEEE 94th Vehicular Technology Conference (VTC2021-Fall), Norman, OK, USA, 2021, pp. 1-5,](https://ieeexplore.ieee.org/document/9625325)       
 
## Date: 2023/4/13
## 周工作汇报
### 阅读文献：
[[1]M. Hu et al., "QoS-Aware Software-Defined Multicast in LEO Satellite Networks," in IEEE Transactions on Aerospace and Electronic Systems, vol. 58, no. 6, pp. 5307-5317, Dec. 2022,](https://ieeexplore.ieee.org/document/9763445)     
[[2]M. Hu, M. Xiao, Y. Hu, C. Cai, T. Deng and K. Peng, "Software Defined Multicast Using Segment Routing in LEO Satellite Networks," in IEEE Transactions on Mobile Computing, 2022,](https://ieeexplore.ieee.org/document/9927319)         
[[3]E. Ekici, I. F. Akyildiz and M. D. Bender, "A multicast routing algorithm for LEO satellite IP networks," in IEEE/ACM Transactions on Networking, vol. 10, no. 2, pp. 183-192, April 2002,](https://ieeexplore.ieee.org/document/993300)         
[[4]Chen Q, Giambene G, Yang L, et al. Analysis of Inter-Satellite Link Paths for LEO Mega-Constellation Networks[J]. IEEE Transactions on Vehicular Technology, 2021, 70(3): 2743-2755](https://ieeexplore.ieee.org/abstract/document/9351765)         
[[5]C. Ren, X. Chen, H. Xiang, Y. Wang, Y. Li and H. Li, "On Efficient Delay-Aware Multisource Multicasting in NFV-Enabled Softwarized Networks," in IEEE Transactions on Network and Service Management, vol. 19, no. 3, pp. 3371-3386, Sept. 2022,](https://ieeexplore.ieee.org/document/9816079)          
### 多播路由在倾斜轨道星座上的应用：
1.倾斜轨道星座网络中的网络拓扑结构比较特殊，需要考虑卫星之间的通信延迟、如何构造网络拓扑。    
a.在计算倾斜星座中的路由路径时，需要考虑卫星的偏移量。   
b.地面用户的接入卫星的选择也是一个重要的问题，特别是在多重覆盖的典型的倾斜巨星座网络中。在路由协议的设计中应考虑跳点的差异。在极轨星座网络中用户-卫星接入不同引起的路径变化。路径更改最多需要一跳。而路径的变化在倾斜的LEO星座中更重要。
