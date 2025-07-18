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
[[1]刘洋,王丽娜.基于树突神经网络的低轨卫星智能感知路由算法[J].工程科学学报,2023,45(03):465-474.](https://doi.org/10.13374/j.issn2095-9389.2021.11.08.007)        
[[2]魏琳慧,刘国文,刘雨等.基于深度强化学习的卫星互联网路由优化研究[J].天地一体化信息网络,2022,3(03):65-71.](https://kns.cnki.net/kcms2/article/abstract?v=BBImVa1ypluYanXXTHQJguCA5_YZvQ7qY9CRXiGgX9FIdy3qMu3Z9vd8CaW2gbXIRDEQWscWY5za7TScPjzZVkIlydusfKS8nISRwX20CZgkmzWSs0GcE3gkydAOvJvN&uniplatform=NZKPT&language=CHS)        
[[3]NI Shaojie, YUE Yang, ZUO Yong, LIU Wenxiang, XIAO Wei, YE Xiaozhou. The Status Quo and Prospect of Satellite Network Routing Technology[J]. Journal of Electronics & Information Technology, 2023, 45(2): 383-395.](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT211393)              
 
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

## Date: 2023/4/19
## 周工作汇报
### 调研全球卫星星座发展现状：
   
    
## Date: 2023/5/4
## 周工作汇报
### 1.负载均衡的路由算法论文：
1.由于地面业务的不均匀分布可能导致卫星间链路拥塞，提高网络负载平衡性能已成为LEO网络中路由算法需要解决的关键问题之一。因此，通过扩展可用路径的范围，结合拥塞避免机制，提出了一种基于LEO星座网络中基于扩展链路状态的负载平衡路由算法。仿真结果表明，该算法实现了流量负载的均衡分布，减少了链路拥塞和丢包率，提高了LEO卫星网络的吞吐量。        
本文贡献1.提出了一种基于扩展链路状态（LRES）的负载平衡路由算法。该算法不仅保持了路径集的最优性，而且降低了路径集的拥塞概率2.设计了一种自适应的拥塞阈值设置机制。该机制能更好地适应流量负荷的变化；3.提出了一种链路拥塞状态通知机制和一种重新路由机制。保证了链路状态获取的及时性，但开销较小。         
网络模型：类铱星星座，卫星覆盖地面站通信，使用虚拟拓扑模型。在快照中，网络拓扑被认为是静态的。    
基于扩展链路状态的负载均衡路由算法：首先满足延迟约束：传播时延和排队时延。ISL路径时延和上行/下行链路的延迟之和必须小于服务的最小延迟要求。链路拥塞阈值的设立：发生拥塞的剩余时延，路径的总传播时延和剩余时延的比值为r，r越大，卫星节点的丢包率大，拥塞阈值小；当丢包率小时，拥塞阈值大。链接拥塞状态通知机制：两个部分：第一个部分为状态发现机制，请求消息在最短的两条路径上发送，都拥塞则去剩下的路径发送，返回拥塞状态的值busy。第二个部分：当链路上的队列长度超过拥塞阈值时，状态将通知拥塞链接两端的两个节点的邻居节点。LCN的链路反馈时延很短。重路由机制：拥塞链路的末端节点的相邻结点为卫星1和卫星2，寻找卫星1的上游的其他路径，没有再找上游，一直到达源节点没有其他路径就发往最短路径。    
  仿真：在较低到中负载的情况下，LRES算法可以依靠其更全局的拥塞避免机制来获得比ELB和TLR算法更好的延迟性能。在高负载条件下，该算法旨在避免链路拥塞，减少丢包的发生，同时牺牲了部分延迟性能。这种算法的丢包率性能表现好，吞吐量也有提高，但是在一些条件下，牺牲了时延。这个算法在网络负载较大的时候效果好。[1]    
      
  2.针对低地球轨道卫星网络中有限区域内布置地面网关站造成的网络拥塞问题，该文提出一种基于分段路由的流量回返路由算法。轻载区和重载区根据网关与反向槽的相对位置关系动态划分。轻载区采用预平衡最短路径算法，拥塞指数定义的最小权重路径为重载区路由规则。然后，参照所有区域中的分段路由执行一致转发。仿真条件是不同大小的重载区、不同的流量密度分布和不同的流量需求。仿真结果表明，随着重载区大小的扩展，负载均衡性能在平均抑制比、平均相对吞吐量、最大链路利用率和平均时延等方面均有显著提高。该算法是LEO卫星网络路由策略的替代解决方案和指导。           
本文贡献：针对网关集中分布下的LSN流量返回，提出基于分段路由（SR）的负载均衡路由算法。构建LSN系统模型是所提算法的基础。轻载区和重载区根据网关与反向槽位的相对位置关系动态划分，不同可用区采用不同的路由规则，提高网络吞吐量，避免拥塞。轻载区采用预平衡最短路径算法，当流量收敛到重载区时使用基于拥塞指数的最小权重路由。    
  LEO卫星网络系统模型：每个网关随时只与一颗卫星进行通信。X网关布置在一个有限的区域内和一个中央基站。映入星间链路带宽、星地链路带宽以及地面链路带宽。地面流量采用地理单元离散化的方法进行处理。此外，通信信道被认为是理想的信道，无论其如何衰减、多路径等，而移动性管理被简化为一种没有异常寻址的理想方法。    
流量传输模型：流量密度是小区的流量需求与系统的最大流量需求之比，实际流量需求值是流量密度与单位服务值的乘积。单位服务值记录为u。流量值和u的单位与星间链路带宽和反馈链路带宽的单位相同。单元格k的流量密度记为f (k)，相对流量为u×f（k），星间链路总的流量携带为   
![image](https://user-images.githubusercontent.com/83910735/235978957-153ed1ab-e315-4b74-90b9-4a40eb72a1c2.png)    
反馈链路总的流量携带为   
![image](https://user-images.githubusercontent.com/83910735/235979002-f62d7d20-16e6-476f-be1f-7dae0e852e35.png)   
基于分段路由的负载均衡路由算法：    
![image](https://user-images.githubusercontent.com/83910735/235979062-6b181dab-6a64-4ef6-9fd5-cd9d930f1415.png)    
这里在删除剩余带宽小于所需带宽的链路后将链路权重配置为生成权重网络。    
仿真：该算法应用于具有卫星链路的沃克星座，仿真结果显示了在平均拒绝比、平均相对吞吐量、最大链路利用率、平均延迟和平均抖动等方面的性能。仿真结果表明，随着尺寸的扩展，平均拒绝比、平均相对吞吐量和最大链路利用率显著提高，但延迟增加不小，具有更好的负载平衡性能。由于网关布置在有限的区域内，则平均延迟更高。由于采用SR原理进行负载均衡，与其他算法对比中该算法的拒绝比最小，时延较小，证明了该算法在网关集中分布下的优势。[2]       

### 2.MEC+空天地一体化+边缘缓存+资源分配的算法:
1.空天地一体化网络分布式深度强化学习辅助资源分配算法。     
由于卫星的功率限制和频谱资源的稀缺，不同用户的服务质量（QoS）和体验质量（QoE）仍然不能得到保证。在本工作中，利用无线边缘缓存，考虑到SAGIN的中继具有边缘缓存能力，将热任务提前缓存在网络节点中。此外，利用分布式深度强化学习（DRL）优化了该过程，从而减少了传输延迟，减轻了天基网络的任务卸载压力。与先进的相关工作相比，该算法的长期节点利用率、链路利用率、长期平均收入成本比和接受率分别提高了约4.22%、31.36%、11.75%和7.14%。          
本文的贡献：1.将SAGIN资源分配问题建模为一个马尔可夫决策过程（MDP），并提出了一种基于分布式DRL的资源管理算法。2.提出了一种分布式的SAGIN资源管理架构。天基网络、空中网络和地面网络都采用分布式管理解决方案。3.对该算法进行了仿真，并与其他资源管理工作进行了比较，结果表明该算法具有较好的性能。    
由于SAGIN的异构、时变、自组织等特点，集中式资源管理方案极其难以实现。为了解决这个问题，首先在每个边缘物理域部署一个具有DRL能力的智能服务器，其次，在一个由SAGIN资源属性构建的环境中对代理进行训练，然后根据训练结果对每个用户的请求制定最优的资源分配策略。本文采用DRL方法对基于分布式架构的SAGIN资源管理进行了综合研究。     
建模：空天地一体化网络建模：基础网络和虚拟网络建模：在整个SAGIN网络系统中，主要分为地面网络控制器和卫星级基本网络资源两部分。其中，地面控制器去管理地面接入节点、卫星节点、卫星间链路和卫星-地面链路，并通过虚拟网络映射将用户请求映射到底层的真实物理域。加入负载平衡得到基础网络链接的权重：     
![image](https://user-images.githubusercontent.com/83910735/235979620-17acbf10-2d9e-4172-a31f-4617a89b04c1.png)    
马尔科夫决策过程表示为5元组：其中的状态为：   
![image](https://user-images.githubusercontent.com/83910735/235979690-8a1e7d28-8e2f-4483-aadd-a81b1918ccb3.png)    
在本文中，使用映射单个VNR的R/C比率作为该VNR的映射奖励，这个奖励值基于节点和链接的路径评估更好的路径候选人和选择最好的路径在当前网络条件下当这个路径真的被使用了：    
![image](https://user-images.githubusercontent.com/83910735/235979767-cdc5687f-bc47-4a05-ada2-90ca5e63c6eb.png)    
仿真：与SA-VNE[35], MCRM-VNE[36], GCN-VNE[37对比发现，在长期的结点和链路资源利用率，R/C比值以及长期接收率上都有较好的效果。[3]   

[[1]C. Dong, X. Xu, A. Liu and X. Liang, "Load balancing routing algorithm based on extended link states in LEO constellation network," in China Communications, vol. 19, no. 2, pp. 247-260, Feb. 2022](doi: 10.23919/JCC.2022.02.020)    
[[2]W. Liu, Y. Tao and L. Liu, "Load-Balancing Routing Algorithm Based on Segment Routing for Traffic Return in LEO Satellite Networks," in IEEE Access, vol. 7, pp. 112044-112053, 2019](doi: 10.1109/ACCESS.2019.2934932.)     
[[3]Peiying Zhang; Yuanjie Li; Neeraj Kumar; Ning Chen; Ching-Hsien Hsu; Ahmed Barnawi, ”Distributed Deep Reinforcement Learning Assisted Resource Allocation Algorithm for Space-Air-Ground Integrated Networks, ” December. 2022](doi:10.1109/TNSM.2022.3232414)       


## Date: 2023/5/11
## 周工作汇报
### 1.读了两篇论文，准备组会文献分享和PPT：


## Date: 2023/5/17
## 周工作汇报
### 1.人工智能路由算法论文：
1.基于深度强化学习的低地球轨道卫星智能路由算法（DQN-IR）[1]。本文重点探索并提出了一种利用深度强化学习模型的仅依赖于周围卫星节点状态的智能分布式路由算法（一个卫星只能获得周围的四颗卫星的状态）。该算法不需要设置额外的分类阈值或使用历史信息预测链路的状态。该算法基于准静态卫星拓扑（即拓扑快照）的假设和虚拟拓扑路由的思想。    
源卫星的智能路由过程可以分为三个步骤：1.源卫星依靠通信交互获取与周边4个卫星节点的可用信道带宽、信道信噪比（SNR）、间距、排队时延、空间定位等决策相关信息;2源卫星使用经过训练的DQN模型，根据接收到的相关信息和自身状态（如发射功率、要发送的数据量等）获取预测输出;3源卫星完成预测输出与下一个卫星节点选择之间的映射，并将要发送到所选节点的数据传输。然后将选定的节点视为新的源卫星，重复上述过程，直到数据最终传输到目的节点。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/253b90f2-e4dd-4040-9fad-80ec976dba4b)   
1) State:信噪比、带宽、排队时延、距离、是不是目标节点（0或1）       
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/bd5f1b89-4a6e-4f39-8c75-6bd73c113c4e)    
2)Action：    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/6af42095-8f7d-4dec-8f58-b4756623f4e9)    
3)Reward: 信道速率，排队时延，距离，跳数    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/c4523b82-7a6b-410a-8aec-046f488481fe)    
仿真结果：    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/7d96a5ff-f87a-401b-975d-ddaf65cd48e0)    
和其他两种贪婪算法对比，一种以距离为参考因素，一种对路由节点的带宽、信噪比、排队延迟、距离等因素设置固定的权值，并通过其加权和选择路由。    
2.基于强化学习的综合空-天-地路由方案[2]。本文提出了一种基于强化学习的综合空-天-地路由方案。通过强化学习及其奖励函数的设计，作者以最小化延迟为目标，以剩余的能量和带宽利用率作为路由的约束条件。理论分析和仿真结果表明，强化学习方法有效地解决了空-天-地集成网络中卫星带宽资源有限和热气球能量有限的问题，并成功地实现了该路由功能。与Floyd路由相比，延迟、丢包率和带宽利用率都有了显著提高。    
1.设计了一种新的空-天-地集成网络架构，并对不同的链路进行了优先排序，并利用真实的网络节点数据进行了路由性能评估。2.使用强化学习来实现网络路由。与经典的Floyd路由算法相比，该方案具有较低的开销，并且可以实时调整路由。3.实时检测剩余的能量和带宽利用率，以平衡负载。在这里，负载表示网络流量密度。除了完成正常的路由功能外，还可以根据节点的剩余能量和链路的带宽实时调整路由。    
在每种拓扑结构下，基于邻接矩阵的路由可以大大降低路由开销。邻接矩阵元素是时延，并计算热气球的能量消耗以及卫星的能量消耗和收集的能量。      
目标是最小化总延迟，同时确保能源消耗和带宽。两个约束为（1）所有节点的最小剩余能量都不低于阈值，（2）每个链路的带宽利用率不超过网络拥塞率。     
Q-learning输入为网络邻接矩阵，智能体输出当前状态下的最佳路由选择。      
1)state:状态空间S为所有节点。    
2)Action：所有可选的链路。    
3)Reward: rE和rB是当节点剩余能量过小、带宽利用率过高时造成的惩罚，它们是绝对值相对较大的负数。所有参数的阈值都是λ的函数。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/0fb4d76b-15ad-46b6-beba-5ec4ec41c692)    
仿真结果对比于Floyd算法（取两节点之间的最短路径）。     
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/221e287c-2bea-48b3-9da6-f2fdee6e6743)    
同时，所提出的q学习路由的端到端延迟和丢包率性能都优于Floyd路由，且在高负载条件下带宽利用率更高。这是因为建议的路径可以从过去发生的拥塞中学习，并在这个前提下找到延迟最小的路径。虽然传统方案的负载增加，但随着阻塞概率的增加，带宽利用率降低。基于强化学习的路由的带宽利用率仍然可以随着负载的增加而增加。        
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/00bfd65d-a56f-4f68-8c0b-ed9df5124a9b)    
随着数据包长度的增加，各种性能呈现出增加的趋势，因为数据包越长，传输要求越高。当包长度为1024时，由于链路队列容量的限制，包丢失率随着负载的增加而急剧增加，说明包长度的合理值范围不应超过512字节。当数据包长度合理时，q学习路由的性能优于Floyd路由。     
[[1]P. Zuo, C. Wang, Z. Yao, S. Hou and H. Jiang, "An Intelligent Routing Algorithm for LEO Satellites Based on Deep Reinforcement Learning," 2021 IEEE 94th Vehicular Technology Conference (VTC2021-Fall), Norman, OK, USA, 2021, pp. 1-5,](https://ieeexplore.ieee.org/document/9625325)     
[[2]X. Shi, P. Ren and Q. Du, "Reinforcement Learning Routing in Space-Air-Ground Integrated Networks," 2021 13th International Conference on Wireless Communications and Signal Processing (WCSP), Changsha, China, 2021, pp. 1-6](https://ieeexplore.ieee.org/document/9613510)   
[[3]X. Wang, Z. Dai and Z. Xu, "LEO Satellite Network Routing Algorithm Based on Reinforcement Learning," 2021 IEEE 4th International Conference on Electronics Technology (ICET), Chengdu, China, 2021, pp. 1105-1109](https://ieeexplore.ieee.org/document/9451072)    

## Date: 2023/5/25
## 周工作汇报
### 1.调研组播技术：


## Date: 2023/6/9
## 周工作汇报
### 1.深度强化学习实现路由，调试代码：
[Y. -H. Hsu, J. -I. Lee and F. -M. Xu, "A Deep Reinforcement Learning based Routing Scheme for LEO Satellite Networks in 6G," 2023 IEEE Wireless Communications and Networking Conference (WCNC), Glasgow, United Kingdom, 2023, pp. 1-6,](https://ieeexplore.ieee.org/document/10118680)    
[Yixin HUANG,Shufan WU,"Reinforcement learning based dynamic distributed routing scheme for mega LEO satellite networks,"Chinese Journal of Aeronautics, (2023),Volume 36, Issue 2, February 2023, Pages 284-291](https://www.sciencedirect.com/science/article/pii/S1000936122001297)     
### 2.查找星间通信，边缘缓存，地面站到卫星通信的能耗模型、问题公式：

## Date: 2023/6/15
## 周工作汇报
### 1.MEC+空天地一体化+边缘缓存+资源分配+能耗和时延优化的算法：
1.场景建模：每颗LEO卫星都通过回程链路连接到地面上的云服务器。地面用户处于偏远地区，没有地面网络通信基础设施的支持。每个LEO卫星m都配有一个MEC服务器，因此可以为地面用户提供计算服务。对于地面用户无法处理的计算密集型任务，计算任务可以通过无线链路卸载到LEO卫星上，或通过LEO卫星转发到云服务器上进行处理。对于地面用户能够处理的计算任务，它可以自行计算。此外，我们假设每个地面用户只有一个计算任务需要计算，并且该计算任务不能被分割。此外，考虑到低轨卫星具有高速运动的特点，地面用户与低轨卫星之间的通信时间受低轨卫星覆盖时间的限制。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/be7d2b61-b7f6-4a20-b425-ab2e7c772418)    
当地面用户有大量需要卸载的计算任务时，LEO卫星可以协同完成计算任务的处理。此外，ISL的传输速度较快，因此可以忽略从LEO卫星到另一个LEO卫星的计算任务的传输延迟。每个地面用户只能访问一个LEO卫星进行数据传输。忽略了从LEO卫星或云服务器向地面用户进行的计算结果的传输时延。每个地面用户的计算任务只有一个卸载决策。    
上行传输速率公式：       
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/79f7dd5f-ae7e-4312-9fb5-d8ccfd802b9d)     
本地时延和能耗：    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/c6c36fc1-5cca-4d97-a854-077a48f0138e)     
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/17d8d2d0-b32d-4826-b433-745cf8c01ccd)      
LEO计算时延和本地能耗：对于LEO计算：每颗低卫星的计算能力相等，时延包括传播延迟，传输延迟和计算延迟。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/8194e391-a8b6-4aa7-ad28-aca4a94bdb83)      
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/cdb9e4c2-c077-4a48-94f7-f13e1a02ce61)   
云服务器计算时延：对于云服务计算：时延包括传播延迟，传输延迟，计算延迟和回程延迟，本地能耗和LEO计算相同。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/9471b623-7b98-4423-9594-729fa7c2e70c)      
问题公式：在满足低卫星有限的计算能力和覆盖时间限制的同时，降低地面用户的总能耗。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/f8bd9f5f-09c1-4597-b768-5a55d88a8098)    
### 2.不同场景：
基于终端-卫星云的三层边缘计算体系结构，每个卫星卫星都有一个MEC服务器。这里假设用户位于偏远地区或灾区，没有地面通信网络的服务。假设用户u（u∈U）只通过单个卫星s（s∈E）访问卫星网络，并且每个用户都有一个最大长度为Q的任务队列，可以缓存任务。这些任务可以在本地计算，卸载到卫星节点，或通过接入卫星中继到远程云。由于ISL的存在，这些任务可以被传输到其他卫星进行协同计算当接入卫星计算能力不足时。这里的能耗和时延都加入了排队的一个等待的时延，能耗在云山计算时没有考虑计算的能耗。本文问题公式是尽量减少在延迟和资源约束下的长期任务处理过程中的系统能量消耗。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/f3a96275-e78d-41cf-81fb-ff6dd4d618f3)    
多任务MEC系统由三个网络段组成，即地面段、空中段和天基段。每颗卫星都部署了MEC服务器（S-MEC），为覆盖区域内的任务提供服务。多个基于无人机的空中基站（A-BS）组成了空中部分。在实际的物联网场景中，一些应用程序通常包含大量的任务。这些任务是相互依赖的，并共同工作来完成整体任务。其中一些可以并行处理，而另一些则需要按顺序进行处理。我们将这些任务建模为有向无环图（DAG）。这里考虑到地面到卫星由于路径损耗和信道噪声传输功率会出现衰减，最后计算出任务上行和下行数据速率（公式较详细）。延迟模型：只考虑传播延迟和处理延迟。能耗模型：只考虑本地和卫星执行任务的计算能耗。总消耗是时延和能耗的加权和。这里考虑了任务的优先级。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/5586ebf2-877c-46f7-97ab-0087978384a1)    
ISTN由多颗多天线LEO卫星、B个多天线BSs、N个单天线移动用户和一个CP组成。我们认为每颗卫星与其他卫星的覆盖范围不重叠，所有的BSs和卫星都有有限的高速缓存存储容量，并通过高速回程链路连接到CP。在ISTN中，请求相同内容的用户被安排成一个组播组，并通过协同波束形成由可缓存基站（BSs）和近地轨道（LEO）卫星提供服务。 为了最大限度地提高考虑网络吞吐量和回程流量的网络效用，缓存放置、LEO卫星和BS聚类和组播波束形成被共同设计并表述为一个双时间尺度的优化问题。该方案提高网络吞吐量，降低回程流量。    
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/27ba6a1d-3b60-4806-8e8d-c6aa490939cb)   
在每个时隙t的开始，无人机以恒定速度飞行，收集这些区域的数据任务。根据接收到的任务量，无人机需要决定是否在可见范围内卸载到某个卫星，然后利用云服务器进行处理，还是卸载到附近的BS进行处理。当选择了卸载目的地时，还需要确定卸载任务的比例。这是因为无人机的计算能力仍然有限。因此，部分任务由无人机执行，其余任务由卸载目的地处理。      
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/83910735/bc543b8a-52a4-4100-a121-7bcafd9812b6)    
[[1]Q. Tang, Z. Fei, B. Li and Z. Han, "Computation Offloading in LEO Satellite Networks With Hybrid Cloud and Edge Computing," in IEEE Internet of Things Journal, vol. 8, no. 11, pp. 9164-9176, 1 June1, 2021,] (doi: 10.1109/JIOT.2021.3056569.)     
[[2]H. Zhang, R. Liu, A. Kaushik and X. Gao, "Satellite Edge Computing With Collaborative Computation Offloading: An Intelligent Deep Deterministic Policy Gradient Approach," in IEEE Internet of Things Journal, vol. 10, no. 10, pp. 9092-9107, 15 May15, 2023,] (doi: 10.1109/JIOT.2022.3233383.)    
[[3]F. Chai, Q. Zhang, H. Yao, X. Xin, R. Gao and M. Guizani, "Joint Multi-task Offloading and Resource Allocation for Mobile Edge Computing Systems in Satellite IoT," in IEEE Transactions on Vehicular Technology,]( doi: 10.1109/TVT.2023.3238771.)    
[[4]D. Han, W. Liao, H. Peng, H. Wu, W. Wu and X. Shen, "Joint Cache Placement and Cooperative Multicast Beamforming in Integrated Satellite-Terrestrial Networks," in IEEE Transactions on Vehicular Technology, vol. 71, no. 3, pp. 3131-3143, March 2022,] (doi: 10.1109/TVT.2021.3138898.)    
[[5]Y. Chen, B. Ai, Y. Niu, H. Zhang and Z. Han, "Energy-Constrained Computation Offloading in Space-Air-Ground Integrated Networks Using Distributionally Robust Optimization," in IEEE Transactions on Vehicular Technology, vol. 70, no. 11, pp. 12113-12125, Nov. 2021,] (doi: 10.1109/TVT.2021.3116593.)       

## Date: 2023/6/29
## 周工作汇报
### 1.阅读空天地一体化中关于缓存的文献：
### 2.低轨卫星网络下的内容缓存和缓存内容分发的初步想法：
### 3.走迷宫方式实现DRL卫星路由算法：

## Date: 2023/7/6
## 周工作汇报
### 1.低轨卫星网络下的内容缓存和缓存内容的分发建模：
### 2.阅读空天地一体化中关于缓存和移动边缘计算的文献：


## Date: 2023/7/12
## 周工作汇报
### 1.继续完善低轨卫星网络下的内容缓存和缓存内容的分发建模：
1.公式问题   
2.文件是否分块   
3.如果几个用户对一个相同的内容具有请求需求，那么这些内容将缓存到距离这几个用户都相对较近的卫星上，折中存放缓存内容问题    
4.考虑了用户集群
### 2.尝试了带有相位因子的极地轨道卫星星座DRL卫星路由算法（索引部分代码有问题）：


## Date: 2023/9/6
## 周工作汇报
### 1.一种基于图卷积神经网络的强化学习方法实现LEO卫星网络中的移动边缘缓存论文撰写：
### 2.正在撰写专利申请的技术交底书：
