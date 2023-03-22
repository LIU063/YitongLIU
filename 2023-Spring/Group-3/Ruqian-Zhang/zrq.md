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
