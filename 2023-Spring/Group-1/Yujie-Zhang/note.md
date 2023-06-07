# 20230607周报
## 1、QoS-Centric Handover for Civil Aviation Aircraft Access in Ultra-Dense LEO Satellite Networks（超密集低轨卫星网络中以QoS为中心的民航飞机接入切换）
### 背景
多个超密集近地轨道卫星星座已经发射，可以为民航提供全球高带宽服务。然而，飞机和卫星的高移动性给超密集低轨卫星网络（UDLSN）中的切换方案设计带来了巨大挑战。在本文中，考虑到切换次数、负载平衡和链路可靠性，我们研究了UDLSN中民航飞机接入的以服务质量（QoS）为中心的卫星切换问题。
### 系统模型
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/127767983/18705780-4b3b-46b7-80a8-1701876026e2)  
为了确认无缝连接并满足飞机的QoS要求，考虑三个指标作为切换标准：
* 剩余可用时间：为了保证服务的连续性，往往会选择提供最长服务时间的卫星
* 可用信道资源：防止大量卫星过载，从而导致网络拥塞，空闲信道的数量被认为是切换标准之一
* 信噪比：同信道干扰可能导致链路可靠性下降，甚至通信中断
用公式表示出三个指标，飞机的QoS需求与上述三个指标密切相关，定义Q函数来表征切换动作后飞机的QoS要求，表示为三个指标的加权和。最终的目标是最大化所有飞机的Q函数，找出最好的切换策略。
## 2、A User-Centric Handover Scheme for Ultra-Dense LEO Satellite Networks（超密集低轨卫星网络中一种以用户为中心的切换方案）
### 背景
为了提供更高的服务质量（QoS）并解决低轨卫星之间频繁的切换问题，提出了一种超密集LSN的以用户为中心的切换方案。基本思想是利用卫星的存储能力来提高用户的通信质量。通过在多颗卫星上同时缓冲用户的下行链路数据，地面用户可以实现无缝切换，并始终以最佳的链路质量接入卫星。
### 系统模型
每个地面用户同时被多颗低轨卫星覆盖，用户使用便携式卫星终端（PST）与低轨卫星建立通信链路，一旦地面用户访问LSN，将被分配多个候选接入卫星（CAS）。在与LSN通信期间，用户可以根据卫星到地面链路的质量选择CAS中的任何卫星作为当前数据传输的主接入卫星（MAS）。对于CAS中的每个卫星，它为用户保留一定的缓冲空间，并存储地面站通过多播转发的用户的下行链路帧。在这种情况下，每当用户决定在CAS之间切换时，可以立即获得所请求的数据。
星地通信过程分为两个步骤，即通信建立和无缝切换。
* 通信建立：在地面用户可以访问LSN之前，PST应该搜索来自LEO卫星的周期性广播信号。一旦PST接收到来自低轨卫星的广播信号（至少一颗卫星的信号），它将测量每个接收信号强度指标（RSSI），并选择信号最强的低轨卫星作为MAS。要建立连接，PST应该向MAS发送一个包含身份验证信息的请求。一旦接入请求被批准，PST将被分配通信资源（包括接入频谱、板载缓冲空间和IP地址）和CAS。
* 无缝切换：
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/127767983/b2f2b603-8d5c-400a-bf10-422562059a19)   
在第一个切换窗口，CASs缓冲了地面站通过多播转发的用户下行链路帧P1−P8，作为CAS之一的LEO1是用户的当前MAS。在第一个切换窗口期间，LEO1成功地传输了帧P1、P3、P4，而帧P2的传输失败。对于用户的PST，它通过广播为每个接收到的帧发送确认。因此，所有CAS都可以接收ACK1、ACK3、ACK4作为对帧P1、P3、P4的确认，并将这些帧从其缓冲区中删除。在第二个切换窗口中，根据RSSI，由于通信质量更好，PST决定从LEO1切换LEO2。切换过程分为三个步骤：PST广播切换请求以通知LEO1和LEO2，以及在最后切换窗口中以位图的形式发送的ACK1、ACK3、ACK4的重复确认；LEO1接收到切换请求后，立即停止向PST发送数据帧，并通过星间链路向PST发送确认信号和向LEO2发送切换确认信号；在接收到来自PST的切换请求和来自LEO1的确认信号之后，LEO2开始向PST发送缓冲器中的请求帧P2、P5、P6、P7。确认后，所有的CAS删除缓冲区的帧，这样可以提高切换过程中可靠性传输的效率。  
另一个需要考虑的是在每个切换窗口之后更新CASs。
[1]Y. Wang, X. Qin, Z. Tang, T. Ma, X. Zhang and H. Zhou, "QoS-Centric Handover for Civil Aviation Aircraft Access in Ultra-Dense LEO Satellite Networks," 2022 IEEE/CIC International Conference on Communications in China (ICCC), Sanshui, Foshan, China, 2022, pp. 1085-1089
[2]
# 20230523周报
### 调研考虑了地面用户和低轨卫星的高移动性的论文
从网络协议体系的角度看，网络层的移动性管理协议主要解决移动节点IP地址发生变化时的IP数据转发机制，以支持通信的连续性。链路层的移动性管理主要包括切换控制和位置管理。低轨卫星高速运动或终端移动会导致终端与其服务卫星逐渐远离，为了保障服务的连续性和可靠性，需要将终端业务切换到新的卫星继续服务，该过程即为切换控制。切换控制包括波束间切换、星间切换、星间链路切换以及星地切换。位置管理是对移动终端位置变化进行跟踪、保存、更新和查找。
#### 1、A Load Balance Local LEO Satellite Network AP Selection Strategy（卫星接入控制）
LEO卫星可以作为地面网络的空间延伸，通过低时延和便捷的接入引入高质量的服务，主要挑战是LEO卫星和地面终端之间的高相对速度引起的动态性。因此如何做出正确的接入点(AP)选择决策是一个关键问题。本文针对AP选择问题，提出了一种以均衡网络负载为目标的本地卫星AP选择策略。我们建立了终端覆盖模型和数据传输速率模型，用于数据收集和性能评估。对比实验结果表明，所提出的策略能够在保持良好的吞吐量期望的同时平衡网络负载，降低切换频率。
#### 2、LISP-LEO: Location/Identity Separation-based Mobility Management for LEO Satellite Networks（路由）
在星地一体化网络中，LEO卫星和地面终端之间的相对运动是不可避免的，这将触发终端IP地址的重新分配并破坏正在进行的TCP连接。传统的移动IP协议可以通过使用家乡代理和隧道机制来解决问题。然而，对于星地一体化网络，移动IP效率低下，为了解决上述问题，本文提出了LISP-LEO，一种用于LEO卫星网络的基于位置/身份分离的移动管理协议。具体来说，（1）将地球表面划分为分区，并根据卫星运动的规律性实时维护分区-卫星映射表;（2）始终通过查询分区-卫星映射表将流量路由到目的地终端上方的卫星，从而消除了三角路由和相关的性能开销;（3）通过提出最后一跳中继来处理目的地终端上方出现多颗卫星的极端情况。仿真结果表明对于LEO-48星座，与移动IP相比，LISP-LEO在最差的路由情况下减少了55.0%的RTT，转发跳数减少了45.8%。
#### 3、DQN-ALrM Based Intelligent Handover Method for Satellite-Ground Integrated Network（切换控制）
由卫星和地面基站组成的星地一体化组网(SGIN)被视为解决全球覆盖问题的趋势。然而，高度动态的场景对用户的移动性管理，尤其是切换决策提出了巨大挑战。随着机器学习的快速发展，强化学习(RL)，如Q-learning和深度Q-network(DQN)，由于擅长解决动态多属性优化问题，已被应用于切换决策。然而，Q-learning可能会浪费大型状态空间的存储空间。此外，现有的在深度强化学习框架中训练神经网络的算法存在收敛速度慢或收敛性能不稳定的问题。因此，本文提出了一种利用动量自适应学习率的DQN框架(DQN-ALrM)的切换方法，不仅可以提高决策精度，还可以提高学习效率。
#### 4、大规模低轨卫星网络移动性管理方案（管理终端设备的位置方便接入卫星）
地面网络中的移动性管理方式主要为集中式管理，即采用本地代理来实现对终端的管理，同时终端每次发起位置更新时都要向本地代理传输消息。如果直接将这种地面网络的集中式移动性管理方法应用在低轨卫星网络场景中，就会出现以下两个问题：（1）终端频繁切换接入卫星而产生的大量报文消息，会经过星间链路和本地网络传递给本地代理。这将使得卫星星间链路和本地网络负载过高。这种负载会随着终端数量的增加而继续增大，容易导致网络瘫痪。（2）当终端距离本地代理较远时，信令的传输时延会增大。这种时延会影响终端的切换，进而影响整个网络的性能。因此，为了在寻呼时能够快速准确地找到通信终端的接入卫星，需要对卫星网络的用户终端进行有效的移动性管理，提出了一种根据地面终端密度自适应调整虚拟网关规模的算法，每次终端切换接入卫星时，仅需要通知本地网关，并在本地网关内更新接入的卫星信息。
# 20230517周报
## D-ViNE: Dynamic Virtual Network Embedding in Non-Terrestrial Networks
### 1、背景介绍
现有的虚拟网络嵌入(VNE)方法主要针对静态VNE,而当新的服务请求到达或由于故障等问题导致网络拓扑发生意外变化时，静态策略效果并不好，考虑到应用于拥有高度动态拓扑和有限资源（速率、功率）的非地面网络（NTN）比如卫星网络中，本文提出了一种动态的虚拟网络嵌入算法（D-ViNE)
### 2、系统模型
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/127767983/8e6fe0c3-5ffb-4db8-8896-3278196a5cd3)  
考虑一个支持SDN/NFV的NTN，包括卫星网络(SN)和地面网络(TN)，TN包括SDN交换机和地面节点。SDN交换机根据SDN控制器安装的流规则转发SFC请求，每个SFC请求由多个顺序的VNFs组成，地面节点和卫星都有能力执行VNFs，地面节点和SDN交换机通过有线链路互连。另一方面，卫星通过无线链路通过网关与地面节点连接，卫星之间有星间链路(ISLs）相互连接。  
* 物理网络建模：所有SN节点都能够存储流表并执行VNFs，每个节点ni∈N具有处理能力和存储能力，卫星的运动是可预测的。并将总时间划分为多个时隙，ISLs链路和TN到SN节点的链路是时变的。
* 虚拟网络建模：将SFC的任务请求用一个七元组表示，每个VNF节点有处理单元和存储单元的要求，虚拟链路有速率的要求，每条虚连接对应一条或多条物理连接。每个节点只能处理某种特定类型的VNFs，VNF的类型是有限的，VNF部署完成后，表示出完成一个SFC请求的时间。
* 优化问题建模：嵌入SFC请求fk的成本由执行VNF的节点功耗成本和VNF部署成本两部分组成。将完成每个服务请求的收益累加，减去成本，优化目标即为最大化净收益，为一个整数线性规划问题。
### 3、仿真结果
仿真结果表明本文所提出的方法相比于静态映射策略和基于禁忌搜索的映射策略在服务请求接收率和平均净收益上有更好的性能
## Network Slicing Algorithms Case Study:Virtual Network Embedding
本文提出使用强化学习算法（RL-VNE）来优化网络切片中虚拟网络请求（VNR）的映射决策问题
## 审稿
## 学习AI相关教程
# 20230511周报
## 基于元关系学习的B5G网络切片服务定制VNF部署(meta-relational learninng-based service-tailored VNF deployment for B5G network slice)
### 1、背景介绍
网络切片(NS)被提出为构建服务定制的B5G网络的新范式，每个网络切片中，为不同的B5G业务按需部署服务所需的虚拟网络功能(VNF)是一个关键问题。由于不同B5G业务之间的实时网络差异和不同的性能要求，传统的VNF部署算法在从一片部署任务切换到另一片部署任务时代价高昂。本文提出了一个元关系学习框架，以获得快速、经济地学习和适应新任务的能力为目标，关注的是如何学习来为不同的任务训练好的策略，而不是像传统的目标驱动算法那样专注于如何为单个任务训练好的策略。  
元学习（二元分类器示例）
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/127767983/46a55337-9284-420d-b1c1-f4b54d30a5a4)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/127767983/e65e937a-4c64-4e20-8fab-93906fa8887a)
### 2、系统模型
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/127767983/6077aefc-8b8a-44b5-8172-9261ab5e4dd5)  
### 2.1 知识图谱嵌入
使用TransH模型分别将切片任务和物理网络的知识嵌入到同一个向量空间中，得到M（meta-training task set)
### 2.2 meta learner module
为了动态地从M中观察到的示例任务中提取公共知识和元信息，元学习器被设计用于学习不同任务中从h到t的映射关系r。使用一个L层的神经网络，选择一个任务，计算对应的连接关系和相应的loss,然后更新模型的参数，继续得到下一个任务的连接关系，最终得到初始的映射结果。
### 2.3 deployment learner module
虽然在meta learner模块中，已经得到了初始映射关系,但由于新到达的切片任务与物理网络之间的实时交互信息还没有传递给学习器，离“服务定制部署VNF”还有一段距离。把新到达的任务的所有三元组定义为适应集A，并且将适应集A中尾部实体(即承载vnfs的物理节点)的预测过程表述为马尔可夫决策过程(MDP)，使用强化学习确定每一个VNF都被分配，然后根据最短路径的原则处理链路映射，更新参数多次迭代后得到新任务的部署方案。


# 20230504周报
## 1、准备组会相关内容
## 2、阅读之前调研的空天地相关的部分论文

# 20230419周报
## 一、LEO路由算法
### 1、LEO卫星星座的非对称差分路由
O. Markovitz and M. Segal, "Asymmetric Differential Routing for Low Orbit Satellite Constellations," ICC 2022  
摘要：LEO星座创建了一个网络，其中包括通过卫星间链路连接的卫星（作为路由节点），以及动态连接到一个或多个卫星的卫星终端。瞬态、高速变化与高延迟相结合，对设计能够提供保证带宽并支持频繁变化而不会丢包的路由协议提出了独特的挑战。目前的工作主要集中在多个网关和终端之间的端到端路由，并且不提供有保证的服务。本文解决了使用非对称差分路由(ADR)将流量从LEO星座上的源终端路由到目标终端的问题。计划“半固定”路线。ADR使大部分计划的路线保持固定，并且只需要进行较小的（差异）调整即可解决切换问题。
链接：https://ieeexplore.ieee.org/abstract/document/9839156
### 2、LEO星座网络中基于扩展链路状态的负载均衡路由算法
C. Dong, X. Xu, A. Liu and X. Liang, "Load balancing routing algorithm based on extended link states in LEO constellation network," in China Communications  
摘要：作为卫星通信网络的重要组成部分，LEO卫星星座网络是研究热点之一。由于地面业务的不均匀分布可能导致星间链路拥塞，提高网络负载均衡性能已成为LEO网络中路由算法需要解决的关键问题之一。因此，通过扩大可用路径范围，结合拥塞避免机制，提出一种基于LEO星座网络中扩展链路状态的负载均衡路由算法。仿真结果表明，该算法实现了业务负载的均衡分布，降低了链路拥塞和丢包率，提高了LEO卫星网络的吞吐量。
链接：https://ieeexplore.ieee.org/document/9722787
### 3、一种基于实时流量的LEO卫星星座空间网络负载均衡路由方法
H. Liming, K. Shaoli, S. Shaohui, M. Deshan, H. Bo and Z. Meiting, "A load balancing routing method based on real time traffic in LEO satellite constellation space networks," 2022 IEEE 95th Vehicular Technology Conference: (VTC2022-Spring)  
摘要：随着卫星间链路的快速发展，路由算法将成为低地球轨道卫星星座的关键问题，特别是对于天基物联网网络。该文提出一种基于卫星链路历史流量的路由技术负载均衡策略。在传统基于快照的卫星路由算法的基础上，将各链路的过往流量参与计算最优路径，并考虑对整个星座网络中的流量负载分布进行优化。该算法显著缓解了卫星网络部分热点区域高流量负载负担造成的网络拥塞和丢包问题。仿真结果表明，该方法能够有效改善高负载条件下网络流量负载不平衡导致的时延性能下降，同时降低了丢包率，优化了业务的时延稳定性。
链接：https://ieeexplore.ieee.org/document/9860540
### 4、基于真实卫星、飞行和航运数据的天空地一体化网络的深度学习辅助路由
D. Liu, J. Zhang, J. Cui, S. -X. Ng, R. G. Maunder and L. Hanzo, "Deep Learning Aided Routing for Space-Air-Ground Integrated Networks Relying on Real Satellite, Flight, and Shipping Data," in IEEE Wireless Communications,2022  
摘要：目前的海上通信主要依赖传输资源贫乏的卫星，因此性能不如现代地面无线网络。随着跨大陆空中交通的增长，依靠商用客机的航空自组网这一有前途的概念有可能通过空对地和多跳空对空链路加强基于卫星的海上通信。在本文中，我们设想了支持泛在海上通信的空-空-地一体化网络，其中低地球轨道卫星星座、客机、地面基站、船舶分别作为空间、空中、地面和海洋层。为了满足异构业务需求，适应天-空-地一体化网络的时变性和自组织性，我们提出了一种深度学习辅助多目标路由算法，该算法利用准可预测网络拓扑结构并以分布式方式运行。我们的仿真结果基于北大西洋地区的真实卫星、飞行和航运数据，表明集成网络通过减少端到端延迟、提高端到端吞吐量以及提高路径寿命来提高覆盖质量。结果表明，我们的深度学习辅助多目标路由算法能够实现接近帕累托最优的性能。  
链接：https://ieeexplore.ieee.org/document/9762643
## 二、	星地一体化＋边缘计算+物联网（任务卸载/资源分配）
### 1、协同计算卸载的卫星边缘计算：一种智能深度确定性策略梯度方法
H. Zhang, R. Liu, A. Kaushik and X. Gao, "Satellite Edge Computing with Collaborative Computation Offloading: An Intelligent Deep Deterministic Policy Gradient Approach," in IEEE Internet of Things Journal,2022  
摘要：使能卫星网络具有边缘计算能力，可以进一步补充单一地面网络的优势，为用户提供全方位的计算服务。卫星边缘计算是未来星地一体化网络不可或缺的潜在技术。本文提出了一种由端-星-云组成的三层边缘计算架构，可以在三个平面处理任务，星间协同实现星载负载均衡。面对具有不同服务需求的多变随机任务队列，我们制定了在延迟和资源约束下最小化系统能耗的目标问题，并联合优化卸载决策、通信和计算资源分配变量。此外，资源分配基于预留机制，保证了星地链路的稳定性和计算过程的可靠性。为了适应动态环境，我们提出了一种基于深度确定性策略梯度(DDPG)算法的智能计算卸载方案，该方案由多个不同的深度神经网络(DNN)组成，以输出离散和连续变量。此外，通过设置合法动作的选择过程，实现了多任务并发下的卸载位置和资源分配的同步决策。仿真结果表明，所提方案通过保证按需完成任务，有效降低系统总能耗，优于基准算法
链接：https://ieeexplore.ieee.org/abstract/document/10032271/
### 2、移动边缘计算星地网络中的星间协同卸载决策与资源分配
作者：Tong M, Li S, Wang X, et al.出处：Sensors, 2023  
摘要：支持移动边缘计算(MEC)的卫星地面网络(STN)可以为物联网(IoT)设备提供任务计算服务。但是，由于某些应用的任务需要大量的计算资源，有时本地卫星的MEC服务器计算资源不足，而相邻卫星的MEC服务器计算资源却冗余。因此，我们研究了支持MEC的STN中的卫星间合作。首先，我们设计了一个支持MEC的STN架构的系统模型，其中本地卫星和相邻卫星通过星间协作协助物联网设备完成计算任务。本地卫星将一些任务迁移到相邻卫星以利用它们的空闲资源。接下来，制定和分解所有物联网设备的任务完成延迟最小化问题。然后，我们提出了一种星间协同联合卸载决策和资源分配优化方案，该方案由基于灰狼优化(GWO)算法的任务卸载决策算法和基于拉格朗日乘数法的计算资源分配算法组成。通过不断迭代得到最优解。最后，仿真结果表明，所提出的方案比其他基线方案取得了相对更好的性能。
链接：https://www.mdpi.com/1424-8220/23/2/668
### 3、卫星物联网移动边缘计算系统联合多任务卸载与资源分配
F. Chai, Q. Zhang, H. Yao, X. Xin, R. Gao and M. Guizani, "Joint Multi-task Offloading and Resource Allocation for Mobile Edge Computing Systems in Satellite IoT," in IEEE Transactions on Vehicular Technology,2023.  
摘要：对于卫星物联网(IoT)中的多任务移动边缘计算(MEC)系统，不同任务之间存在依赖关系，需要收集并联合卸载。由于卫星通信和计算资源的稀缺性，合理分配计算和通信资源至关重要。为了解决这个问题，我们在卫星物联网中提出了一种联合多任务卸载和资源分配方案，以提高卸载效率。我们首先构建了一个新的资源分配和任务调度系统，其中任务由多个基于无人机(UAV)的空中基站收集和决策，边缘计算服务由卫星提供。此外，我们研究了框架中的多任务联合计算卸载问题。具体来说，我们将具有依赖关系的任务建模为有向无环图(DAG)，然后我们提出了一种注意机制和近端策略优化(A-PPO)协作算法来学习最佳卸载策略。仿真结果表明，A-PPO算法可以在25步内收敛。此外，与几种基线算法相比，A-PPO算法在默认情况下至少降低了8.87%的成本。总之，本文为卫星物联网中多任务MEC系统的成本优化提供了新的见解。
链接：https://ieeexplore.ieee.org/abstract/document/10024305/
### 4、基于双时间尺度学习的星地一体化远程物联网任务卸载
D. Han et al., "Two-Timescale Learning-Based Task Offloading for Remote IoT in Integrated Satellite-Terrestrial Networks," in IEEE Internet of Things Journal,2023  
摘要：在本文中，我们提出了一种集成的卫星地面网络(ISTN)架构，以支持远程物联网(IoT)的延迟敏感任务卸载，其中卫星网络通过提供额外的通信资源、回程来作为地面网络的补充容量和无缝覆盖。在这种架构下，我们研究了如何为BS和物联网用户共同做出卸载链路选择和带宽分配决策。考虑到不同的决策时间粒度，我们制定了一个双时间尺度的随机优化问题，以最小化整体任务卸载延迟。为了适应双时间尺度网络动态并表征状态-动作关系，我们建立了一个分层马尔可夫决策过程(H-MDP)框架，其中有两个独立的代理处理双时间尺度网络管理决策，并相应地制定了两个基于MDP的进化子问题。为了有效地解决子问题，我们进一步开发了一种基于混合近端策略优化(H-PPO)的算法。具体来说，混合的actor-critic架构旨在处理混合的离散和连续动作。此外，还设计了一个动作掩码层和一个动作整形函数，以从时变动作集中抽取可行的任务卸载决策。广泛的仿真结果验证了所提出的ISTN架构和基于H-PPO的算法的优越性，尤其是在频谱资源稀缺和流量负载大的场景中。
链接：https://ieeexplore.ieee.org/abstract/document/10018447/
### 5、面向天空地一体化网络的分布式深度强化学习辅助资源分配算法
P. Zhang, Y. Li, N. Kumar, N. Chen, C. -H. Hsu and A. Barnawi, "Distributed Deep Reinforcement Learning Assisted Resource Allocation Algorithm for Space-Air-Ground Integrated Networks," in IEEE Transactions on Network and Service Management,2022  
摘要：为实现6G愿景中的万物互联(IoE)，天基、空基、地基网络呈现融合趋势。与传统通信系统相比，天空地一体化网络(SAGINs)可以提供无缝的全球网络连接，同时充分利用不同网络的特性实现协同和互补。然而，随着互联网全球覆盖率的不断提高，智能终端的数量和种类不断增多，各种高带宽业务不断涌现，通信数据传输量呈爆炸式增长。尽管机载处理转发、高通量卫星等通信技术不断发展，但由于卫星的功率限制和稀缺性，不同用户的服务质量(QoS)和体验质量(QoE)仍然无法得到保证。在这项工作中，借鉴无线边缘缓存，考虑到SAGIN的中继具有边缘缓存能力，将热点任务提前缓存在网络节点中。此外，该过程使用分布式深度强化学习(DRL)进行优化，从而减少传输延迟并减轻天基网络的任务卸载压力。与先进的相关工作相比，所提算法的长期节点利用率、链路利用率、长期平均收益成本比和接受率分别提高了约4.22%、31.36%、11.75%和7.14%。
链接：https://ieeexplore.ieee.org/abstract/document/9999560/
### 6、星地一体化车载网络可靠上行同步维护：基于高阶统计的授时提前更新方法
L. Zhen, Y. Wang, K. Yu, G. Lu, Z. Mumtaz and W. Wei, "Reliable Uplink Synchronization Maintenance for Satellite-Ground Integrated Vehicular Networks: A High-Order Statistics-Based Timing Advance Update Approach," in IEEE Transactions on Intelligent Transportation Systems, 2023  
摘要：星地一体化车联网可以为海量车辆提供无处不在的无限网络连接，有望在6G支持的智能交通系统(ITS)中发挥重要作用。然而，由于其高动态的信道环境和有限的卫星载荷，上行链路同步已成为制约车载通信性能的主要瓶颈。着眼于保持可靠的上行链路同步，我们在本文中提出了一种高效的定时提前(TA)更新方法。
链接：https://ieeexplore.ieee.org/abstract/document/9646554/
## 三、LEO卫星物理层安全
### 1、基于尖峰神经网络的LEO-MIMO系统射频指纹识别
Q. Jiang and J. Sha, "RF Fingerprinting Identification Based on Spiking Neural Network for LEO–MIMO Systems," in IEEE Wireless Communications Letters, 2023  
摘要：低地球轨道(LEO)卫星有望成为无线通信领域的创新源泉，其物理层安全性值得关注。然而，许多物理层安全技术在用于LEO卫星时会受到过度功耗和高延迟的阻碍。这篇短文提出了一种基于尖峰神经网络(SNN)的低轨卫星通信系统的能效射频指纹识别(RFFI)方法。此外，我们研究了与通道无关的RFF特征转换和数据扩充，以增强系统的鲁棒性。数值结果表明，我们提出的模型可以在正交频分复用(OFDM)信号的信噪比(SNR)为25dB时产生高达95.26%的识别精度，并且与现有的模型相比，功耗降低了63.3%。
链接：https://ieeexplore.ieee.org/abstract/document/9960779/
## 四、基于LEO卫星的非地面网络
### 1、基于LEO卫星的非地面网络的基于上行链路区域的调度
V. Mandawaria et al., "Uplink zone-based scheduling for LEO satellite based Non-Terrestrial Networks," 2022 IEEE Wireless Communications and Networking Conference (WCNC)  
摘要：为了向分布在全球各地的网络设备提供覆盖，已认识到非地面网络(NTN)可以补充地面网络并将其扩展到偏远地区。由于高差分延迟和多普勒频移极大地影响了NR-NTN用户的性能，低轨卫星NTN在5G-NR协议方面面临着几个前所未有的挑战。在这项工作中，我们研究了NTN小区内的大差分延迟和多普勒频移对5G-NR资源分配和媒体访问控制(MAC)协议的影响。然后，我们提出了一种基于上行链路区域的调度技术，以解决基于LEO卫星的NTN的LEO卫星的高差分延迟和多普勒频移问题。最后，我们通过对最近开发的三星NR-NTN系统级模拟器进行数值模拟，将其与传统的5G-NR协议进行比较，从而验证了所提出策略的性能。
链接：https://ieeexplore.ieee.org/abstract/document/9771894
### 2、基于LEO的非地面网络中的无缝切换：服务连续性和优化
F. Wang, D. Jiang, Z. Wang, J. Chen and T. Q. S. Quek, "Seamless Handover in LEO Based Non-Terrestrial Networks: Service Continuity and Optimization," in IEEE Transactions on Communications,2023  
摘要：在未来的无线网络中开发非地面网络(NTN)已被广泛认为可以为偏远和未服务地区带来先进的通信服务。近地轨道(LEO)星座已成为NTN提供无缝和快速全球连接的有前途的组成部分。然而，由于天生的动态特性，移动性管理，特别是卫星间的切换(HO)，对保证NTN数据服务的稳定和连续性起着重要作用。受此启发，本文提出了一种基于条件切换(CHO)机制的HO优化策略，以增强基于LEO的NTN中的服务连续性。首先设计了一个与链路服务时间和服务能力相关的奖励函数，用于修改候选目标卫星的监测条件。提出最优目标选择算法以获得每个CHO的最大奖励。然后，构建服务连续性性能图(SCG)模型以预测服务持续时间中不同的潜在CHO组合。在SCG的基础上，为每个接入用户预测计算出支持优质稳定数据业务的HO序列。仿真结果表明，所提出的HO优化方案可以明显降低不同NTN条件下的切换率，并且可以更好地增强NTN服务连续性。
链接：https://ieeexplore.ieee.org/abstract/document/9984697/
## 五、超密集LEO星地一体化
### 1、超密集LEO星地一体化6G中的服务感知资源编排：一种业务功能链方法
X. Qin, T. Ma, Z. Tang, X. Zhang, H. Zhou and L. Zhao, "Service-Aware Resource Orchestration in Ultra-Dense LEO Satellite-Terrestrial Integrated 6G: A Service Function Chain Approach," in IEEE Transactions on Wireless Communications,2023  
摘要：随着低地球轨道(LEO)卫星部署规模的迅速扩大，超密集低轨卫星地面综合网络(LTIN)被设想为第六代(6G)系统中实现无缝连接和通信的有前途的架构。高速数据速率服务。特别是对于传输距离远、时延要求高的超远程实时业务，融合网络可以保证其端到端的业务连续性。然而，由于综合网络的大规模、异构性和高移动性，为服务交付的高效资源编排带来了诸多挑战。对于每项服务，其数据都需要经过一系列机载处理，然后才能下载到地面网络以供进一步应用。为此，引入了服务功能链(SFC)，一种有序串联的网络功能(NF)，以支持服务提供。通过在LTIN上分配组成NF，我们提出了一种有效的多服务交付方案，以最大限度地减少整体交付完成延迟，同时考虑到多个SFC之间的资源共享和竞争。首先，我们将多重SFC嵌入问题表述为非合作博弈，该博弈进一步证明为具有至少一个纳什均衡(NE)的加权潜在博弈。借助所提出的全局协调机制，我们设计了两种算法来获得NE。一种是具有更快收敛性的最佳响应(BR)算法，而另一种是具有更多最佳解决方案能力的自适应播放(AP)算法。然后，提出了随机学习(SL)算法以适应网络动态并减少全局信息交换。最后，广泛的仿真验证了所提出算法的收敛性和有效性。
链接：https://ieeexplore.ieee.org/abstract/document/10032237
### 2、基于斯塔克尔伯格平均场博弈的超密集LEO卫星网络中海量用户动态数据卸载
D. Wang, W. Wang, Y. Kang and Z. Han, "Dynamic Data Offloading for Massive Users in Ultra-dense LEO Satellite Networks based on Stackelberg Mean Field Game," IEEE INFOCOM 2022  
摘要：低地球轨道(LEO)卫星网络被视为一种有前途的技术，可为偏远地区（如农村地区）提供无缝服务。在本文中，我们考虑了具有大规模用户的超密集LEO卫星网络（例如SpaceX Starlink）中的动态数据卸载问题，其中每个用户在考虑其状态信息、其他用户的影响以及支付给卫星的价格。为了研究用户和卫星之间的交互问题，我们采用Stackelberg博弈算法来制定问题。具体来说，卫星是领导者，并决定在每个时间段计算任务的价格。相反，用户是追随者，根据自己的状态、其他用户的影响以及支付给卫星的价格来决定功率分配。然后，由于用户规模大，影响难以考虑，我们采用平均场博弈算法，将来自他人和卫星的影响转化为平均场项，并将优化问题重新表述为Stackelberg平均场博弈(SMFG)问题。接下来，我们通过泰勒展开将Fokker-Planck-Kolmogorov (FPK)方程转化为线性形式，并采用G-prox primal-dual hybrid gradient (PDHG)算法来解决用户的优化问题。此外，我们采用伴随算法来解决卫星的优化问题。最后，数值结果表明了所提算法的有效性。
链接：https://ieeexplore.ieee.org/document/9798204
## 六、考虑LEO卫星高动态特性
### 1、基于DVB的LEO卫星系统的动态功率和带宽分配
ETRI Journal, 2022  
摘要：低地球轨道(LEO)卫星星座可用于为整个地球提供网络覆盖。本研究考虑了LEO卫星系统中的多波束频率复用。在这样的系统中，由于卫星的快速移动，信道是随时间变化的。本研究提出了一种高效的功率和带宽分配方法，该方法采用两种线性机器学习算法，并将信道条件和流量需求(TD)作为输入。借助简单的线性系统，所提出的方案允许在动态信道和TD条件下优化资源分配。此外，将有效的投影方案添加到所提出的方法中，以便当TD超过最大允许系统容量时，提供的容量最接近TD。仿真结果表明，所提出的方法优于现有方法。
链接：https://onlinelibrary.wiley.com/doi/abs/10.4218/etrij.2022-0192
### 2、去除基础设施移动带来Qos瓶颈的LEO网络
L. Liu et al., "Geographic Low-Earth-Orbit Networking without QoS Bottlenecks from Infrastructure Mobility," 2022 IEEE/ACM 30th International Symposium on Quality of Service (IWQoS)  
摘要：低地球轨道(LEO)卫星巨型星座承诺为偏远地区的地面用户提供来自太空的宽带、低延迟网络基础设施。然而，由于快速移动的LEO卫星和地球自转，它们面临着来自基础设施移动性的新QoS瓶颈。两者都会导致频繁的空地链路中断，并在全球范围内挑战网络延迟、带宽和可用性。今天的LEO网络用固定锚点（地面站）掩盖了基础设施的移动性，但会导致单点带宽/延迟瓶颈。相反，我们设计LBP以从基础设施移动性中消除LEO网络的QoS瓶颈。LBP通过地理寻址移除远程陆地固定锚点，以获得更短的延迟和更多的带宽。它采用本地的、轨道方向感知的地理路由来避免全局路由更新，以实现高网络可用性。LBP通过根据卫星轨道方向细化切换策略，进一步缩短了路由路径。我们在受控测试台和跟踪驱动仿真中的实验验证了LBP将网络延迟降低了1.64倍，带宽提高了9.66倍，并将网络可用性提高到了100%。
链接：https://ieeexplore.ieee.org/abstract/document/9812903
## 七、其他
### 1、为新兴的LEO卫星网络启用低延迟的星地拓扑
Y. Zhang, Q. Wu, Z. Lai and H. Li, "Enabling Low-latency-capable Satellite-Ground Topology for Emerging LEO Satellite Networks," IEEE INFOCOM 2022   
摘要：网络拓扑设计对于在未来的集成卫星和地面网络(ISTN)中实现低延迟和高容量至关重要。然而，现有的研究主要集中在ISTN星间拓扑的设计上，而对星地拓扑的设计及其对可达到的网络性能的影响知之甚少。研究各种星地设计对ISTN网络性能的影响。我们发现，新兴巨型星座的高密度和高动态特性共同带来了巨大的挑战，例如严重的路由不稳定性、网络可达性低、ISTN路径上的高延迟和抖动。为了缓解上述挑战，我们制定了低延迟星地互连（LSGI）问题，针对ISTN中空间和地面段的集成，同时最小化最大传输延迟并保持路由稳定。我们进一步设计算法，通过明智地协调分布式地面站之间地对卫星链路的建立来解决LSGI问题。综合实验结果表明，我们的解决方案可以优于现有的相关方案，平均延迟减少约19%，抖动平均减少70%，同时保持最高的网络可达性。
链接：https://ieeexplore.ieee.org/abstract/document/9796886 
### 2、LEO卫星网络可持续传输优化的动态组网
F. Wang, D. Jiang, Z. Wang, J. Chen and T. Q. S. Quek, "Dynamic Networking for Continuable Transmission Optimization in LEO Satellite Networks," in IEEE Transactions on Vehicular Technology, 2022  
摘要：低地球轨道(LEO)卫星网络(LSN)被设想为地面网络的补充和增强。LEO星座为全球用户，特别是偏远地区的用户提供低延迟、高速的数据传输。但是，由于移动性的性质，必须预先配置LSN网络模式。与固定模式相比，LSN的动态组网将带来更多好处，但同时也面临更多挑战。动态LSN网络中的两个主要问题是如何增加网络传输容量(NTC)以及如何在服务期间保持出色的NTC性能。受这两个问题的启发，我们首先构建了一个时变连通图来表示LSN特征随时间的变化。然后提出了一种基于支持向量机(SVM)的LSN组网方案，以提高NTC性能。SVM模型在每个时隙预测每种链路类型，以优先考虑类型匹配任务的传输。接下来，构建网络性能图(NPG)以显示不同时隙划分的潜在NTC性能。利用动态规划寻找LSN服务连续性最优的时隙序列。仿真结果表明，与现有的LSN组网方案相比，所提出的基于SVM的动态规划传输接触规划(NSDP)方案可以实现卓越的NTC性能和服务连续性。
链接：https://ieeexplore.ieee.org/abstract/document/10002869/
### 3、软件定义LEO星座的交通工程
M. Hu, M. Xiao, W. Xu, T. Deng, Y. Dong and K. Peng, "Traffic Engineering for Software-Defined LEO Constellations," in IEEE Transactions on Network and Service Management, 2022  
摘要：新兴的低地球轨道(LEO)卫星网络有望提供世界上最先进的互联网服务。此外，地面网络在不断发展，并且已经开始采用相对较新的软件定义网络(SDN)范例。在本文中，我们利用SDN功能的优势并利用流量工程(TE)来增强宽带LEO卫星网络中的星间链路性能。我们研究了用于SDN增强型LEO星座的单播和组播TE，以增强基于卫星的互联网服务。在LEO卫星网络中，单播支持无处不在的网络接入并提供基础网络服务，而组播则具有优越的卫星视频分发功能。对于网格ISL网络中的单播TE，我们提出了一种简单而高效的基于k段路由的策略和分段路由(SR)技术，与多商品流解决方案相比，它可以实现接近最优的最大链路利用率。同时，我们的解决方案消除了路由表，只强加了存储在数据包标头中的少量路由信息。对于多播TE，我们采用直线斯坦纳树(RST)来最大限度地节省带宽，并利用避障直线斯坦纳树(OARST)来解决多个多播组的争用问题。基于RST和OARST，我们提出了一种有效的每流管理方案，以在链路容量有限的情况下平衡多个多播流之间的流量。仿真结果证明了我们的方法在减少路由信息和容纳更多组播组方面的有效性和效率。
链接：https://ieeexplore.ieee.org/abstract/document/9828016/
### 4、多卫星协同通信：利用非正交传输中的时间异步性
M. Zhao, N. Ye, Q. Ouyang, Y. Jin, Y. Jin and L. Zhao, "Multi-Satellite Cooperative Communication: Exploiting Time Asynchrony in Non-Orthogonal Transmissions," in IEEE Transactions on Vehicular Technology, 2023  
摘要：近地轨道星座的日益密集化使得通过多星协同传输提高数据速率成为可能。然而，卫星网络的大空间尺度使得时间不同步性不容忽视。在本文中，我们利用异步非正交传输进行多星协作通信以提高公平感知率。将异步容量扩展到多星协作场景，进而制定优化问题，联合考虑星端关联、功率分配和解码顺序。为了剖析这些耦合变量，我们提出了一种基于偏好列表的算法，该算法在以下两个阶段之间迭代。首先，给定预先指定的偏好列表，通过基于Gale-Shapley算法的策略解决多对多双边匹配。然后，发射功率和解码顺序由Dinkelbach-like算法联合优化。基于以上结果，偏好列表被更新以反映用于迭代细化的卫星间干扰。仿真结果表明，引入协作传输将公平率提高了12%，利用时间异步又提供了7%的增益。
链接：https://ieeexplore.ieee.org/abstract/document/10006363/
### 5、统一的空中接口设计方案是未来的重要研究方向
为了支持多种业务的传输，终端极其简单地接入最适合天地网的节点。统一空口体制，在空中接口分层结构上，采用相同的设计方案，采用相同的传输和交换技术。
### 其他前沿代表性文献
[1] W. Liu, H. Yang, and J. Li, “Multi-Functional Time Expanded Graph: A Unified Graph Model for Communication, Storage, and Computation for Dynamic Networks Over Time,” IEEE Journal on Selected Areas in Communications, vol. 41, no. 2, 2023  
[2] Z. Xiao, T. Mao, Z. Han, and X.-G. Xia, “Near Space Communications: A New Regime in Space-Air-Ground Integrated Networks,” IEEE Wireless Communications, vol. 29, no. 6, 2022  
[3] L. Cai, J. Pan, W. Yang, X. Ren, and X. Shen, “Self-Evolving and Transformative (SET) Protocol Architecture for 6G,” IEEE Wireless Communications, 2022  
[4] F. Lyu, F. Wu, Y. Zhang, J. Xin, and X. Zhu, “Virtualized and Micro Services Provisioning in Space-Air-Ground Integrated Networks,” IEEE Wireless Communications, vol. 27, no. 6, 2020  
[5] D. Zhou, M. Sheng, J. Li, and Z. Han, “Aerospace Integrated Networks Innovation for Empowering 6G: A Survey and Future Challenges,” IEEE Communications Surveys and Tutorials, 2023  
[6] S. Gu, Q. Zhang, and W. Xiang, “Coded Storage-and-Computation: A New Paradigm to Enhancing Intelligent Services in Space-Air-Ground Integrated Networks,” IEEE Wireless Communications, vol. 27, no. 6, 2020  
[7] D. Liu, J. Zhang, J. Cui, S. X. Ng, R. G. Maunder, and L. Hanzo, “Deep Learning Aided Routing for Space-Air-Ground Integrated Networks Relying on Real Satellite, Flight, and Shipping Data,” IEEE Wireless Communications, vol. 29, no. 2, 2022


# 20230323周报
## 面向内容服务的空地集成6G网络资源分配  
[论文链接](https://ieeexplore.ieee.org/document/9874801/)
### 1、主要内容  
&emsp;&emsp;在空地集成6G网络中提出了一个包含内容源、SAGINE和终端用户三个实体的资源分配系统模型，并将问题表述为三方匹配。加入一些限制条件将三方匹配问题转化成限制性三方匹配问题并开发了面向内容的R-TMSC资源分配(COR<sup>2</sup>A)算法和面向用户的R-TMSC资源分配(UOR<sup>2</sup>A)算法来解决上述问题。
### 2、系统模型
* 网络模型：内容源与sagine之间的匹配是多对多匹配，而内容源与用户之间、sagine与用户之间的匹配是一对多匹配。  
* 信道模型：考虑了未来地面终端与天基或空基网络之间的通信场景（视距链路和非视距链路）。
* CSP的收入：匹配用户提供的价格减去其支付给SAGINEP的数据传输成本的总和。
* 用户满意度：用户- sagine下行链路的数据传输速率。  
最终问题建模为：  
![1209117444e2ba50e4bf5a664213c82](https://user-images.githubusercontent.com/127767983/227089432-f7599381-142b-42b5-8329-de37232f0762.png)
### 3、R-TMSC描述
&emsp;&emsp;在TMSC中，每个参与者都有一个只包含一种类型的其他实体的偏好列表，即内容源只对用户排序，用户只对SAGINE排序，SAGINE只对内容源排序，TMSC的核心是寻找稳定的三方匹配结果。H=C×U×e表示所有可能的三元组的集合，w是稳定的匹配结果，是H的子集。定义阻塞三元组（非稳定的三元组，且相对于每个agent本来的匹配结果，每个agent都更喜欢现在的匹配结果），如果没有阻塞三元组，则说明该匹配是稳定的，将P1优化问题描述为最大化稳定匹配三元组的个数P2，这是一个NP-complete问题。  
![94852c88d83e8bd8a88972c7578bb84](https://user-images.githubusercontent.com/127767983/227089615-cf0a1f82-61a8-49ff-9743-64dc764171bf.png)  
&emsp;&emsp;每个内容源的用户首选项列表由一个主列表组成，该主列表按降序对用户进行排序，报价高的用户优先级高；每个用户根据产生的数据传输速率所衡量的服务质量对可接受的SAGINE进行排序，创建用户偏好列表；内容来源与SAGINE无关，所以偏好列表均为1。加入限制后变成了R-TMSC问题。  
![0ec89be6ba1425ceb11d424b094b8d3](https://user-images.githubusercontent.com/127767983/227089696-ade9a1c8-b887-4df0-b01b-869ba4c5148f.png)
### 4、算法
#### 1、COR<sup>2</sup>A算法
&emsp;&emsp;从空匹配开始，找到最合适的三元组，然后将其添加到w中。每一个合适的三元组都是通过首先选择一个满足特定需求的内容源（面向内容的）来生成的，然后这个所选的内容源选择最适合的用户来满足其需求，最后，被选中的用户选择最合格的SAGINE。  
#### 2、UOR<sup>2</sup>A算法
&emsp;&emsp;从空匹配开始，每一个最合适的三元组都是通过首先选择一个满足特定需求的用户（面向用户）来创建的，然后被选择的用户再选择一个满足其特殊需求的最合适的SAGINE。最后，所选SAGINE从它的首选项列表中随机选择一个内容。  
#### 3、解耦的资源分配算法（DRA算法）
&emsp;&emsp;DRA算法将三方匹配问题就转化为两方匹配问题，分别是SAGINE-Content对和用户，降低了计算复杂度。但需要对三个实体进行解耦，这将导致每个实体的偏好信息缺乏，从而导致性能下降。
### 5、仿真结果
&emsp;&emsp;所提出的两种算法与DRA算法、贪心算法、最优解算法等几种算法相比在吞吐量、CSP收益和用户满意度方面都有更好的性能。

# 20230330周报
## 基于SFC的空天地一体化网络资源分配
### 1、主要内容
针对SAGIN系统中网络设备和链路部署统一管理的难点，采用SFC技术解决了多网集成过程中的设备和链路问题，本文研究了基于业务类型的SFC SAGIN架构，提出了一种基于时延预测的SFC映射方法,NFV技术用于感知网络节点和链路的负载，以确保网络资源的最大利用率，计算部署路径的时延，选择时延最小的路径作为SFC映射路径。
### 2、系统模型
* 物理网络模型：  
使用加权无向图GV={NV,LV} 代表虚拟网络,其中NV代表所有虚拟节点，LV代表所有虚拟链路，虚拟网络的示例如图所示：  
![61af79e19e398b3f8a1ebd21a7b71a2](https://user-images.githubusercontent.com/127767983/228540623-093bfc2f-1e3b-4a69-8a24-beaff882deab.png)  
虚拟节点用六边形表示。每个虚拟节点的CPU资源需求由矩形中的第一个数字表示。方括号中的数字表示虚拟节点的候选域。每个虚拟节点可以有两个候选域。虚链路用虚线表示，每条虚链路都有相应的带宽资源需求，用虚线旁边的数字表示。  
同样使用加权无向图 GS={NS,LS}表示底层网络，NS代表所有的物理节点，LS代表所有的物理链路，底层网络的示例如图所示：  
![d25e956ca953020c535b4f40ab46a07](https://user-images.githubusercontent.com/127767983/228542538-fa4aa79f-0548-4817-adf2-a9a2d3eb46f8.png)  
底层网络分为三个不同的域，物理节点用圆表示。每个物理节点都有其可用的CPU容量，由节点旁边矩形中的第一个数字表示，节点有其延迟，由节点旁边矩形中的第二个数字表示。底层网络的域内链路用实线表示，域间链路用虚线表示。物理链接旁边的括号有两个参数，第一个表示物理链路的可用带宽容量，第二个表示物理链路的延迟。
* SFC请求建模：每个SFC请求应包括节点、连接节点的链路、业务流所需的VNF顺序、带宽要求、时延要求等。因此，SFC请求模型可以用Q = {N, L, V, B, D}表示。其中N表示节点，L表示链路，V表示VNF序列，B表示SFC请求的带宽要求，D表示SFC请求的延迟要求。常见的SFC请求类型有三种，第一种是原点与目的节点一一对应，原点与目的节点之间只有一条链路。第二种类型是源节点和目标节点之间的关系是一对多。从起点出发，路径的链接不同，目的节点也不同。第三种是源节点和目的节点是一对一的，但是从源节点到指定的目标节点有多条链路。
### 3、问题公式化
根据SFC的要求，通过评估负载情况、正常运行概率和各种路径延迟，从多条路径中选择当前网络状态下的最优部署路径。  
* 节点负载参数：该节点上已使用的计算资源与网络中部署SFC请求所需的节点计算资源的和占该节点所有计算资源的比例  
* 链路负载参数：链路已占用带宽与SFC请求所需链路带宽的和占链路总带宽的比值  
* 部署链路的总资源消耗：所有计算节点的容量之和与所有链路的带宽之和的和
* SFC请求部署到网络的总业务时延：数据处理时延和部署链路时延组成  
最终问题建模成最小化总业务时延（约束条件为总时延上限为用户指定的时延、节点所需要的资源小于或等于该节点所拥有的资源、链路所需的资源量小于或等于该链路所拥有的资源量）
### 4、基于时延灵敏度的SFC映射算法
提出了一种基于延迟感知的业务功能链映射算法：输入SFC请求Q和物理网络Gv，输出为部署链路延时TDq和部署路径Pq。该算法的主要工作是根据请求的大小、带宽要求和延迟要求对SFC请求进行分类。每个请求都属于一个业务类型。在每项服务中，采用KSP算法选择k条延迟最短、资源开销最小的路径。计算每一个的资源开销和延迟路径，选择延迟最小的路径作为SFC的部署路径，如果延迟小于用户指定的延迟，则生成SFC，否则部署失败。
### 5、仿真结果
CPU资源利用率高27.8%，链路资源利用率高22.7%。业务接受率提高了21.5%，时延性能提高了38.2%，总资源消耗降低了25.2%。
# 20230406周报
## 多目标问题相关调研
### 1、多目标问题
多目标优化是指在某个场景中在需要达到多个目标时，由于容易存在目标间的内在冲突，一个目标的优化是以其他目标劣化为代价，因此很难出现唯一最优解，需要在它们中间做出协调和折中处理，使总体的目标尽可能的达到最优
### 2、多目标图映射问题
* 图映射问题研究如何将一副图中的节点和链路按照其连接关系和约束条件映射到另一幅图中
* 图映射问题中优化目标数量多，问题约束条件复杂，是典型的NP-hard问题，现有基于最优化和元启发式的求解方法不能满足实时性的计算需求，而启发式的求解方案效果不佳
* 需要高精度、强实时性的多目标图映射问题的高效解法
### 3、遇到的问题
* 只关注单一的一方面，比如时延等
* 对多目标问题通过线性加权等方法转变成单目标问题求解了（刻画目标和解不够精细，解的优劣性难以得到保证）
* 目前还没有找到特别符合的论文阅读
* 创新点似乎在求解复杂的多目标图映射问题上，做到真正的多目标求解，做法上的创新点想不到（可能引入多目标图映射的场景后，模型应该是差不多的？）
# 20230413周报
## 基于深度强化学习的工业物联网云边缘协同SFC映射
### 1、主要内容
支持NFV的云边缘协同IIoT架构可以以业务功能链(SFC)的形式高效地为大量IIoT流量提供灵活的服务。高效的云边缘协作、合理的综合资源消耗、不同的服务质量仍然是需要解决的关键问题。因此，为了平衡工业物联网服务的质量以及计算和通信资源消耗，设计了一个多目标SFC部署模型来描述工业物联网的不同业务需求和特定的网络环境。然后，提出了一种基于深度q学习的SFC在线部署算法，通过迭代训练，有效地学习SFC部署方案与其性能之间的关系。
### 2、系统模型
* 支持NFV的云边协同工业物联网架构（NFV-enabled CECIIoT architecture）：  
首先把CECIIoT网络建模为有向图G = (V, E)，其中V是节点的集合，E是链路集合，节点由服务器节点N(可以托管和运行VNF)和路由器节点Q（仅用于转发流量）两种类型构成。服务器节点根据位置可分为边缘服务器M和云服务器C。每个服务器节点有计算资源容量和处理能力两个属性，为了表示网络的负载状态，引入两个变量分别描述服务器和物理链路的负载状态。
![f6110d15074610a582e805c1b5a42d0](https://user-images.githubusercontent.com/127767983/231478365-e4c759e7-7bf2-4bd8-a1c0-f628cbaa207b.png)
* SFC Model:SR = {SR1, SR2, . . . , SR|SR|}表示SFC请求集合，每一个SFC请求可以用一个元组表示。SFC请求可以分为时延敏感型和资源密集型两种，根据不同的需求分别将VNF部署在边缘服务器和云服务器上。
* 时延模型：传输、传播、处理、排队时延
### 3、优化目标
![c77b919aefbd6bf1299dca167181f85](https://user-images.githubusercontent.com/127767983/231526412-7038db68-4516-4e37-99b0-1c10b779f9b1.png)
## 多目标优化问题
## DQL等相关知识的学习
