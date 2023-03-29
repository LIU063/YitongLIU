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

***
  

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
$$ USR=\dfrac{N_s}{N_T} $$
其中$ N_s $是成功服务的计数器，$ N_T $是服务的总数计数器。   
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
[3] Y. Xiao, G. Shi, Y. Li, W. Saad, and H. V. Poor, “Toward Selflearning Edge Intelligence in 6G,” IEEE Communications 
Magazine, vol. 58, no. 12, pp. 34-40, Dec. 2020.  
[4] Y. Xiao, G. Shi, Y. Li, W. Saad, and H. V. Poor, “Toward Selflearning Edge Intelligence in 6G,” IEEE Communications 
Magazine, vol. 58, no. 12, pp. 34-40, Dec. 2020.  
[5]Y. Xiao, G. Shi, Y. Li, W. Saad, and H. V. Poor, “Toward Selflearning Edge Intelligence in 6G,” IEEE Communications 
Magazine, vol. 58, no. 12, pp. 34-40, Dec. 2020.   
[6] N. Chen, Y. Yang, T. Zhang, M. T. Zhou, X. L. Luo, and J. Zao, “Fog as a Service Technology,” IEEE Communications Magazine, Vol. 56, No. 11, pp. 95-101, Nov. 2018.  
[7] Y. Mao, J. Zhang, S. H. Song, and K. B. Letaief, “Stochastic Joint Radio and Computational Resource Management for Multi-User Mobile-Edge Computing Systems,” IEEE Transactions on Wireless Communications, Vol. 16, No. 9, pp. 5994-6009, Sept. 2017.  
***    
由于对于文章中所说的网络AI架构以及其中的边缘AI和云AI等架构等不够详细看不明白，决定细读该文章引用的上述一些相关文献，弄清楚如何实现的网络AI架构，如何进行工作的。

