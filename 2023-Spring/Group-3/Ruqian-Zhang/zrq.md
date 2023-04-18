<p id="table"></p>

# Table of Contents

- <a href="#1">Week 1 (2023.3.23)</a>
- <a href="#2">Week 2 (2023.3.30)</a>
- <a href="#3">Week 3 (2023.4.6)</a>  
- <a href="#4">Week 4 (2023.4.13)</a>
- <a href="#5">Week 5 (2023.4.19)</a>

<br/>  

<p id="1"></p>  

# **周报-Week 1**
## 2023.3.23
## **一、基于场景的策略优化方法的按需服务可行性调研**
- 考虑做某种场景下的优化算法，作为按需服务的策略方案。经过调研，同一KPI场景下，如高时延低可靠性相关场景有很多不同针对性的优化算法，没有办法找到一个优化算法可以粗略的概括该场景的按需服务策略并作为该场景的按需服务方法。所以这个方向暂时认为走不通。
- 考虑到要使做的按需服务要与之前所做的场景聚类结合起来，做基于6G场景分类的按需服务方法，由于上个场景分类的工作，最主要的结果是KPI雷达图以及每类场景的KPI知识以及KPI特征，重点寻找能够基于该结果为按需服务输入的一个按需服务方法。由此观之，为每个已经分类的场景找到一个普适的场景优化方法，不太行得通。准备调研一下机器学习等相关AI有关的方法。



## **二、文献调研**
### **参考文献**  

[1] Selberg E, Etzioni O. Multi-service search and comparison using the MetaCrawler[C]//Proceedings of the Fourth Int'l WWW Conference, Boston. 1995.  
[2] Mezni H, Benslimane D, Bellatreche L. Context-aware service recommendation based on knowledge graph embedding[J]. IEEE Transactions on Knowledge and Data Engineering, 2021, 34(11): 5225-5238.  
[3] Yang Y, Ma M, Wu H, et al. 6G network AI architecture for everyone-centric customized services[J]. arXiv preprint arXiv:2205.09944, 2022. 
*** 
文献调研的主要方向是多服务、按需服务、服务相关。首先调研了文献[1],该文章讲的多服务，是讲的基于元爬虫的多服务搜索和比较，主要用于web上的服务，与我所需要的多服务不同，因此不展开说关于该文献的内容。  


### **1. Context-aware service recommendation based on knowledge graph embedding**  
- 该文章主要讲的是提出了一个基于知识图谱的上下文感知服务推荐方法（C-SKG），其中上下文感知服务推荐（CASR）该方法讲环境感知整合到推荐系统，并且基于环境上下文感知提供适合该用户环境的服务和项目内容等。  C-SKG中包括了用户画像和评委、用户评论、服务的功能和Qos属性、用户和服务的上下文信息以及用户、服务、上下文之间的关系。其中上下文感知是通过RNN实现的（利用RNN的"记忆力"网络），通过将服务推荐转化为节点邻近计算问题，以便预测顶级服务。
- 整个上下文感知推荐过程分为三步推荐过程，包括嵌入上下文知识图谱，提取邻居用户和候选服务。最后，根据活跃用户的上下文对后者进行优化，并返回评分最高的内容。  

    - C-SKG嵌入：该步骤的目的是将C-SKG嵌入到低维向量空间中，以便于提取活跃用户的邻域。结果是具有与活动用户的当前上下文相关的所有信息的矢量化的知识子图，即相似的用户及其偏好的服务。  
    - 对隐藏关系和评级的预测：这一步是通过使用嵌入空间中的负实例和邻近度得分来实现的，该得分有助于预测相似上下文中隐藏的用户-服务连接及其评级。
    - 服务推荐：该步骤旨在基于用户/服务向量的贴近度，提炼CSKG嵌入空间中相似用户和相似服务的子集。这是通过处理C-SKG完成阶段产生的负面实例，并使用计算的上下文相似性来惩罚它们的分数。最后，使用基于惩罚的评分函数对候选服务进行评估和排序，并将前k个服务返回给活跃用户。
![C-SKG](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/C-skg.jpg?raw=true)

- 基于该文章内容得到的一些启发：

$$
\begin{CD}
   用户 @>>> 服务 @>>> 上下文 \\
@VV对应于V @VV对应于V @VV对应于V \\
   6G用户 @>>> （按需）服务 @>>> 环境（场景） \\
\end{CD}
$$

### **2. 6G network AI architecture for everyone-centric customized services**  
通过边缘AI的方法实现6G按需服务，主要是基于资源调度和优化的一个6G按需服务（用户定制化服务），其中提到了基于KPI雷达图为输入，通过AI架构实现资源分配的一个按需服务方法，该方法十分适用于我的工作，本周只是略读，下周讲仔细研究该文章，并得到自己如何去按需服务的一个确定想法。

## **三、下周工作计划**
仔细研究文献[3]的内容，并调研文章中的边缘AI以及相关AI架构的知识，基于该文献的方法提出我的基于场景聚类的按需服务方法的实现架构。 

<br/>

***
  
<p id="2"></p>  

# **周报-Week 2**
## 2023.3.30   
### **参考文献**  
[1] Yang Y, Ma M, Wu H, et al. 6G network AI architecture for everyone-centric customized services[J]. arXiv preprint arXiv:2205.09944, 2022. 
*** 
## **一、6G network AI architecture for everyone-centric customized services 细读**
1. 该文章主要提出了用户端的服务需求区（Service Requirement Zone, SRZ）和系统端的用户满意度（User Satisfaction Ratio, USR）的概念以及网络AI架构。
- 用户端 SRZ：表征和可视化单个用户的特定任务的集成服务需求和偏好。即可视化每个用户任务的复杂和动态的需求，通过使用一组E2E性能界限来表征期多维服务需求，这些界限共同决定了用户的整体QOE。
- 系统端 USR：为了衡量6G系统保证每个人的QOE的服务能力即评估系统满足不同SRZ各种任务的整体服务能力。通过将各个SRZ逐个与所获得的性能结果进行比较，计算出一段时间内所有服务任务中满意任务的百分比。
- 网络AI架构：以多层多功能节点（ MNodes）为基本元素的网络AI架构整合了S2C3A的本地系统网络资源，通过定制SRZ为不同的任务提供原生AI服务平台以支持具有保证服务质量的定制服务。

2. SRZ：  
使用具有多个KPI的雷达图来可视化每项任务的SRZ，以表征用户综合的、多维的服务需求和偏好。如图1中，一般来说，SRZ越大，棕色区域面积越大，表示服务需求越低，反之亦然。
![SRZ雷达图](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/SRZ.jpg)
- 为了保证每个用户的QOE，未来的6G系统应该整合和编排跨多个域的异质网络资源，随时随地提供以每个人为中心的定制服务，从而将网络切片技术转移到任务级的最细粒度。在实践中，每种类型的任务都有相似的SRZ，即针对一组用户的事实上的服务模型。  
- 尽管用户行为和服务环境是动态的，但这些SRZ相当稳定，因为大多数用户通常不会妥协他们的服务需求和服务质量，除非服务连续性和高质量无法同时满足。在这种情况下，一些用户可能接受扩展的SRZ，其具有更低的要求和降低的质量以维持服务连续性，例如在高速列车中。具有普适智能的6G系统应该能够高效地识别、分配和管理不同用户环境、应用场景和网络条件下的各种任务的异质网络资源。

3. USR：  
在6G中，各种任务的动态SRZ被用作定制服务提供和性能优化的QOE目标。  
$$USR=\dfrac{N_s}{N_T}$$  
其中 $N_s$ 是成功服务的计数器， $N_T$是服务的总数计数器。   
- USR可以用于评估6G系统在满足各种任务的单个SRZ方面的整体服务能力，而不是考虑任何特定的用户位置、应用场景、网络条件或运营环境。  
- 具有相似网络资源量的不同系统。USR越高，系统在利用有限的网络资源高效地服务于各个SRZ的不同任务方面就越智能。  
![AI架构图](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/AI%E6%9E%B6%E6%9E%84.jpg)
## **二、思考**   
- 该文章中所提出的SRZ和USR以及网络AI架构的概念，都对于我的基于聚类的按需服务很有帮助，并且十分贴合我的上一步聚类的结果，接轨进入按需服务。其中的基于KPI雷达图的SRZ概念，可以借鉴，可以将之前聚类的几大场景的KPI雷达图进行SRZ定制，并通过自己提出一个网络AI架构进行"按需服务"，以USR来衡量按需服务的效率。  
- 不过目前这个网络AI架构不太清楚其原理，以及思考如何改进SRZ和USR的概念。由于该文章中USR的计算是基于每个任务的SRZ的二元硬判决，即系统是否能同时满足特定于任务的关键绩效指标。但是除了这种二进制分类方法外，SRZ和USR的定义还可以分别从用户端和系统端扩展到多个尺度。

## **三、下周工作计划**   
### **参考文献**  
[1] X. Chen, Y. Deng, G. Zhu, D. Wang, and Y. Fang, “From Resource Auction to Service Auction: An Auction Paradigm Shift in Wireless Networks,” IEEE Wireless Communications, early access, May 2022.   
[2] Y. Xiao, G. Shi, Y. Li, W. Saad, and H. V. Poor, “Toward Selflearning Edge Intelligence in 6G,” IEEE Communications 
Magazine, vol. 58, no. 12, pp. 34-40, Dec. 2020.  
[3] Z. Feng, Z. Wei, X. Chen, H. Yang, Q. Zhang, and P. Zhang, “Joint Communication, Sensing, and Computation Enabled 6G Intelligent Machine System,” IEEE Network, pp. 34-42, Nov./Dec. 2021.  
[4] X. Shen, J. Gao, W. Wu, M. Li, C. Zhou, and W. Zhuang, “Holistic Network Virtualization and Pervasive Network Intelligence for 6G,” IEEE Communications Surveys & Tutorials, Vol. 24, No. 1, pp. 1-30, First Quarter, 2022.  
[5] 6G Alliance of Network AI (6GANA), “From Cloud AI to Network AI, a View from 6GANA,” May 2021. Available at http://www.6gana.com/upload/file/20210619/6375969458505193666851527.pdf.   
[6] N. Chen, Y. Yang, T. Zhang, M. T. Zhou, X. L. Luo, and J. Zao, “Fog as a Service Technology,” IEEE Communications Magazine, Vol. 56, No. 11, pp. 95-101, Nov. 2018.  
[7] Y. Mao, J. Zhang, S. H. Song, and K. B. Letaief, “Stochastic Joint Radio and Computational Resource Management for Multi-User Mobile-Edge Computing Systems,” IEEE Transactions on Wireless Communications, Vol. 16, No. 9, pp. 5994-6009, Sept. 2017.  
      
由于对于文章中所说的网络AI架构以及其中的边缘AI和云AI等架构等不够详细看不明白，决定细读该文章引用的上述一些相关文献，弄清楚如何实现的网络AI架构，如何进行工作的。   
***  

<br/>  

<p id="3"></p>  

# **周报-Week 3**
## 2023.4.6 
## **一、6G network AI architecture for everyone-centric customized services 整体框架**
文章讲了三种人工智能体系结构和系统模型，分别是云AI架构、边缘AI架构和具有多层mNode的网络AI体系结构（是该文章提出的架构）。
- 其中具有多层mNode的网络AI体系结构中mNode作为关键的6G网元，不仅将像服务提供商对E2E服务拍卖那样协调本地资源，还将整合基础感知、存储、通信、计算、控制和人工智能的系统资源（system resources of Sensing, Storage, Communication, Computing, Control, and AI.  $S^2C^3A$ ）资源和多种功能，以支持QOE保证的、以每个人为中心的定制服务。与无线接入网(RAN)或核心网(CN)中专职和独立功能的传统硬性硬件部署不同，mNodes将采用先进的网络功能虚拟化(NFV)技术，并根据需要在6G移动网络中扮演不同的角色，如e/g节点基站(XNB)、P/S网关(XGW)、接入和移动性管理功能(AMF)以及边缘/雾服务节点。除通用计算单元外，预计将有越来越多的AI处理器被mNodes广泛集成和共享，提供6G原生AI服务平台。  
- 在图中，提出的网络AI架构由三个关键单元组成，并在6G中构建了一个全面、分布式和可扩展的AI即服务(AIaaS)平台。首先，网络基础设施由分散在多层移动网络中的mNode组成。其次，每个网络AI逻辑和控制(NALC)单元是面向任务的，并通过有效的信令方案管理特定本地/区域区域中的多层mNode。在6G移动网络中，NALC协调整合的 $S^2C^3A$ 资源和功能，以服务于实时和近实时应用中的每个任务，即E2E延迟范围从毫秒到几十毫秒。每项任务的定制服务流程和个人QOE都由相应的NALC持续监控和优化。第三，网络AI管理和协调(NAMO)单元管理具有多个NALC的AIaaS平台，通过跨域资源协调、服务协调和E2E QOE保证协议来支持广域应用。在6G系统中，NALC和NAMO应该紧密合作，有效平衡不同应用场景下E2E时延短和业务覆盖广的业务需求。对于其他IT供应商愿意贡献额外的云计算和边缘计算资源的情况，NAMO将协调多供应商资源，以支持跨不同AI架构的复杂应用。
- 在不失去通用性的情况下，我们考虑了一个具有三种类型的mNode的三层网络AI体系结构，这三种类型的mNode由蓝色矩形框表示。
- 对于任意任务T，对应的服务提供过程由特定的任务调度算法确定。在任务T到达时，其SRZ首先由位于边缘的附近的第一层mNode检查，该第一层mNode分析利用附近可用的网络资源满足该SRZ的可能性。如果本地资源充足，任务T将立即由该mNode提供服务。如果没有，将启动一个更强大的第二层mNode来领导在更大的邻居中识别可行的网络资源的努力。如果区域资源仍然不足，将要求更强大的第三层mNode在更广泛的区域内执行多域资源协调。在某些情况下，任务T非常复杂，不仅要收集和处理本地和区域数据，还要使用大量的网络资源来收集和处理全局数据。如果任务T可以被拆分成多个子任务，则水平或垂直方向上相同数量的mNode可以共享它们的资源和能力来共同服务于任务T。否则，任务T不能被拆分，而必须通过多层网络上传到云上，从而增加了端到端的传输延迟、能量消耗和总成本。   
(文中只考虑时延和能耗为某用户的KPI来进行仿真)在需求端，不同的用户每秒持续产生λ任务。假设不可拆分任务T具有𝑍字节大小和𝑈万亿次浮点运算的计算需求。为了在有限的空间内展示关键结果，只选择延迟和能耗作为服务KPI，用于构建每个任务的二维SRZ。当输入某用户的某个任务需求的SRZ时该网络AI架构资源分配的优化目标是能耗和时延：  
<div align=center>  

![D.jpg](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/D.jpg)
![E.jpg](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/E.jpg)
![t1](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/t1.jpg)   
![t2](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/t2.jpg)   
<div align=left>  

### **表1列出了有关任务、三种人工智能体系结构和两种任务调度算法的所有参数及其假设值，用于广泛的计算机模拟。**
![参数表](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/%E5%8F%82%E6%95%B0%E8%AE%BE%E8%AE%A1.jpg)   
之后以USR大小为判别标准，体现提出的网络AI架构的性能。 其中公平平等调度(FES)算法以随机方式分配所有任务，一半分配到边缘，另一半分配到云中提供服务。-Closerthe-Better(TCTB)算法遵循帕累托原则或80/20规则，因此所有任务的80%和20%分别流向边缘和云。FES和TCTB算法的使用将展示三种人工智能体系结构之间的根本差异，并为开发适用于复杂应用场景和动态网络条件的更复杂算法提供标准基准。
![f1](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/f1.jpg)   
![f2](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/f2.jpg)   
## **二、启发**
### 做基于聚类结果的6G按需服务，可参考文中的方法，文章仿真举例是只考虑了时延和能耗两个KPI做为服务的KPI，构建的是二维的SRZ。而我可以扩展一下，将考虑我所做的8个KPI的八维SRZ,并且利用聚类结果的11类场景知识，作为场景权重系数分配的条件，为每个不同场景设计一套不同KPI权重系数以及优先级的进一步的USR评判标准，去做一个资源分配来实现基于场景聚类的6G按需服务。
## **三、下一步工作计划**
### 构思该问题下我的聚类按需服务的问题建模  
  
    
<br/>  
    
***  
<p id="4"></p>  
    
# **周报-Week 4**
## 2023.4.13 
## **一、AI for network 调研**  
### **五类典型任务及其对应解决的AI模型：**
1.	计算机视觉任务：计算机视觉任务是指让计算机通过识别和理解图像或视频中的信息，如物体、人、场景等。对于这个任务，典型的AI模型包括卷积神经网络（CNN）、循环神经网络（RNN）、图像分割网络（U-Net）等。

2.	自然语言处理任务：自然语言处理任务是指让计算机能够理解和生成自然语言文本。对于这个任务，典型的AI模型包括循环神经网络（RNN）、长短时记忆网络（LSTM）、Transformer等。

3.	声音识别任务：声音识别任务是指让 计算机能够识别和理解语音信号，如语音识别和语音合成等。对于这个任务，典型的AI模型包括卷积神经网络（CNN）、长短时记忆网络（LSTM）、门控循环单元网络（GRU）等。

4.	强化学习任务：强化学习任务是指让计算机通过试错的方式来学习如何做出最优的决策。对于这个任务，典型的AI模型包括深度强化学习网络（DRL）等。

5.	推荐系统任务：推荐系统任务是指让计算机能够根据用户的历史行为和偏好，为用户推荐相似的产品或服务。对于这个任务，典型的AI模型包括协同过滤算法、基于内容的推荐算法、深度学习推荐算法等  
这五个任务和对应的AI模型在不同领域和应用场景中有广泛的应用。其中，计算机视觉任务和自然语言处理任务在人机交互、智能家居、自动驾驶等领域中有广泛应用；声音识别任务在语音识别、语音合成、音频处理等领域中有广泛应用；强化学习任务在机器人控制、游戏设计、金融预测等领域中有广泛应用；推荐系统任务在电商、社交网络、新闻推荐等领域中有广泛应用。
***
[1] Wu C, Peng Q, Xia Y, et al. Towards cost-effective and robust AI microservice deployment in edge computing environments[J]. Future Generation Computer Systems, 2023, 141: 129-142.      
二区期刊  
目的：在受限资源和高动态网络拓扑的移动边缘计算场景下实现经济高效、稳健的AI微服务的部署。  
解决的问题：  
1）多DNN模型编排问题：不同网络节点运行不同性能特征的DNN模型，一个边缘智能微服务由多个DNN模型组合完成，通过服务的QoS指标寻找合适的DNN模型选择编排方案。  
2）：保证已部署微服务的稳健性（服务的持续性）：微服务实例的放置问题，即选择哪个些具体的DNN节点完成服务。
解决方法：其中各个节点上的DNN模型均为离线训练，无具体的训练过程和数据来源，各模型的计算推理性能作为已知条件固定，围绕QoS设计一个优化问题。

[2] Bhandari G, Lyth A, Shalaginov A, et al. Distributed Deep Neural-Network-Based Middleware for Cyber-Attacks Detection in Smart IoT Ecosystem: A Novel Framework and Performance Evaluation Approach[J]. Electronics, 2023, 12(2): 298.  
三区期刊  
目的：检测分布式物联网场景下的多类恶意攻击。  
解决方法：提出了一种基于AI的物联网网络安全框架，并在多个实际场景下进行了仿真实验，包括数据的收集，AI模型的训练和AI模型的部署方法等。

[3] Yu H, Yu D, Wang C, et al. Edge intelligence-driven digital twin of CNC system: Architecture and deployment[J]. Robotics and Computer-Integrated Manufacturing, 2023, 79: 102418.    
一区期刊  
目的：解决数控系统DT模型的部署问题（包括任务的划分方法和模型的选择方法），并以机器加工过程中的工具磨损诊断及预测问题距离。  
解决方法：在云中选择和训练智能算法以及任务的划分方法，并将划分后的模型分别下载到边缘节点和边缘服务器进行数据的处理。具体根据DNN模型的准确率、时延要求、系统吞吐率、管道数量、准确度阈值建立AI模型的评估函数，在不同的场景任务下根据评估函数实时的选择不同的模型。但模型均为离线训练，其中并无模型的训练方法，有数据的收集方法。

[4] Lu B, Lai S, Tang Y, et al. Deep Model Training and Deployment in Heterogeneous IoT Networks[J]. EAI Endorsed Transactions on Mobile Communications and Applications, 2023, 7(3).   
仅从理论上给出了物联网设备中AI模型的训练和模型的部署的可行的解决方案。
  


## **二、想法**  
利用网络功能虚拟化（Network Function Virtualization, NFV）技术实现AI服务的弹性部署。将AI服务进行虚拟化，使其能够快速在网络中部署和迁移，根据实际的资源需求来调整部署位置和资源分配。  
将AI as a service与6G网络结合的第一步是要将AI服务部署到6G网络中，这可以通过在6G网络中设置AI服务节点来实现。AI服务节点通常需要高性能的计算和存储资源，以及专用的AI处理器和相关的软件框架。这些资源可以直接部署在6G基站、边缘服务器或云数据中心中，以实现对不同的AI服务的支持。在这些节点上，AI服务可以根据应用的不同，包括语音识别、图像处理、自然语言处理等，提供不同的AI算法和模型。

## **三、专利框图**  
![zhuanli](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-3/Ruqian-Zhang/pic/ai-network-%E6%A1%86%E6%9E%B6.png)   
 
<br/>  

***  
<p id="5"></p>        
    
# **周报-Week 5**    
## 2023.4.19     
## **本周工作是写专利，目前已写完专利内容，待系统评估后，和专利公司进行细节商讨修改**    
    
<br/> 
    
    
    
