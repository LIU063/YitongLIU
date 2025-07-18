# 20240129周报

## 上周工作： 撰写毕业设计、修改知识驱动综述

**1.毕业设计正文撰写**
   
   目前已完成第三章撰写
   
   ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/c3613931-b913-4255-a86c-b1d415afb085)
   
**2.修改知识驱动综述**
   
   目前已完成：文献按章节重新分类，Neural Network Model Customization章节内容修改

**3.回复审稿意见**
   
## 本周工作：

1.完成response letter撰写

# 20240115周报

## 上周工作： 撰写毕业设计、修改知识驱动综述

**1.毕业论文第二个研究点：考虑用多AP多用户的wifi场景，结合WMMSE算法，构建异构不动点图神经网络**
   
   目前已经完成场景搭建和WMMSE优化算法计算代码
   
   ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/38e7a5a5-baee-402e-898d-90362c57343e)
   
   难点：一是复数信道特征MLP不能直接处理。二是PYG库特征处理复杂，后续考虑还是用DGL库
   
**2.毕业设计正文撰写**
   
   从第三章开始撰写，目前已完成 3.1 问题建模 3.2 图神经网络建模

**3.修改知识驱动综述**
   
   需修改三章内容，压缩Algorithm Unfolding一章内容
   
   目前已完成：文献按章节重新分类，Neural Network Model Customization章节内容修改
   
## 本周工作：

1.完成毕设第三章内容撰写

2.完成修改知识驱动综述

3.年会汇报内容资料筛查调用


# 20231106周报

## 本周工作： 根据审稿意见修改论文

**1.修改第四章：深度展开有效性假设，新增引用内容**

**2.修改第五章：实验设置描述**

**3.重画实验图，统一横纵坐标格式**

**4.学习ROS2框架，硬件实现计算卸载的任务**
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/fe4c46ac-cbd7-478e-96a6-7a898dc96cac)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/cf9c6e5e-9065-486e-ad12-7cf16b32b54d)



# 20231030周报

## 本周工作： 根据审稿意见修改论文

**1.修改模型图，增加了节点消息传递流程**

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/e8a2a2cf-bd47-4f59-accf-c05056296610)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/ba0053f5-18db-443b-a75d-3e7b3b756834)

**2.修改收敛时间对比实验，小样本情况下性能占优**

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/96a12624-baf9-4acd-9e54-43b4e5c29173)

**3.新增推理时间实验，说明WMMSE及UWMMSE在大规模网络中推理时延难以满足要求**

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/590af83e-21ba-4a9f-855e-98959419feec)







# 20230918周报

## 本周工作： 根据审稿意见修改实验

![image](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Autumn/Group-4/Hao-Yang/Convergence%20Performance%20Comparison_K10.svg)

![image](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Autumn/Group-4/Hao-Yang/Average_Convergence_Performance_K10.svg)


# 20230905周报

## 本周工作： 根据审稿意见一一回复，并修改实验

审稿意见：

**副编辑评论**：

副编辑：Chen, Hongyang

**1.如何构建GNN不清晰。我看不出用GNN解决WMMSE问题的优点。**
```
考虑修改第三章模型图
加一个表格，描述面对大规模网络扩展时，WMMSE算法计算复杂劣势，并且无法解决CSI缺失等情况。
```
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/5f520bc5-2f78-4192-befe-cbb2e9b6f406)

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/df6364a1-981c-4587-9f73-db2dc3304cb5)

2.如果信道信息与边相关，我们看不到边特征和节点特征的含义。

3.GNN通常利用数据驱动。我们看不到与构建GNN相关的数据集。实验中使用了多少节点和边。使用了多少层。
```
修改第二章键图的描述，和第五章实验部分
```

**4.对于新颖性，NAS在深度学习中已经得到了深入的研究。我看不出网络架构搜索或新设计的相关贡献。**
```
思路是提一提NAS的劣势和Deep Unrolling的优势。

NAS相当于多次重复实验搜索出了一个优秀的框架，但存在以下主要缺点：

1. 计算成本高：尽管NAS可以自动搜索最佳架构，但每种架构都需要训练和验证，这需要大量的计算资源和时间。
   这导致了大部分的NAS技术需要高端的GPU集群进行数周甚至数月的搜索。

2. 过度拟合：有可能找到的架构过度优化了验证集，但在实际应用中性能不佳。

3. 不一定总是最佳选择：对于某些具体任务，手动设计或使用传统的神经网络模型可能更为合适。

4. 复杂性：自动生成的网络架构可能较为复杂，不易于理解和解释。

5. 迁移性问题：NAS为特定任务找到的架构可能不容易迁移到其他任务。

6. 资源限制：许多NAS方法主要关注准确性而不是效率。因此，找到的架构可能在有限资源的设备（如移动设备）上运行得不够快。
```

**审稿人：1**

**对作者的评论**：

1. 如何确定第6页第36行的一维变量u_i和w_i的维数。
 
**2. 我非常同意对收敛速度比较的重要性。但是，用于收敛的周期数只是一个方面。是否可以直接比较平均收敛时间消耗？在我看来，不同算法的每个周期的时间消耗可能并不一定相同。**

新增了一个收敛时延的实验：

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/cd5a929e-c07c-4409-9bb7-95f144543c53)

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/23f57fec-42f1-4a4f-b735-92f478e95a6e)
   
3. 为什么在这个模型中使用发射机的优先级？

**4. 如果可以，作者能否考虑增加更多关于图神经网络展开方法有效性的数学描述。**
```
把第四章标题里的理论去掉。
future work，数学上完全理解AI的是AI领域难题。但我们的两个思路，有证明的文章。
```

5. 在V.G节中，如果一个单天线收发器对中的发射机i和接收机i之间的距离大于1000m，h_ii是否设置为0？该文章如何考虑由于流动性引起的中断或切换？
```
future work，目前只考虑了D2D网络中一一对应通信，节点通信的切换更多在路由的MAC层，未来会考虑研究。
```

**审稿人：3**

**对作者的评论**：

**1. 本文的动机不够清晰。最好提供更多的细节，以显示现有基于GNN的D2D通信功率分配方案的缺点。**
```
主要根据Deep unrolling的优势，说明现有GNN设计的不足，比如泛化性不足，样本复杂度高，完全分布式运行时，GNN中间层过宽会带来通信开销。
```

2. 作者假设完整的信道状态信息（CSI）可以用于迭代。然而，通常很难获得完整的CSI，尤其是在超高密度和高动态场景中。
```
目前假设是基站辅助的D2D网络，下一步将考虑完全的分布式网络，CSI的获取机制会考虑在GNN消息传递的过程中。
```

**3. 图7中的仿真结果显示，WMMSE方案在总速率方面比提议的UWGNN方案表现得更好。请深入解释这一现象。**
```
图7是考虑到了拓扑的变化性，通信由全连接变为了稀疏矩阵，但WMMSE算法用的是矩阵乘法，只是将矩阵中的元素设置为0，代表连接边不存在。训练设置可能需要在确认一下。
```
4. 请添加一个表格，列出本文中使用的关键符号和变量。

## 下周工作：

1.根据模板撰写回复意见

2.进一步改进实验仿真





     

