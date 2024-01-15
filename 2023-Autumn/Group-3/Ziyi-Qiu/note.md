<p id="table"></p>

# Table of Contents

- <a href="#1">Week 1 (2023.9.12)</a>
- <a href="#2">Week 2 (2023.9.18)</a>
- <a href="#3">Week 3 (2023.10.16)</a>
- <a href="#4">Week 4 (2023.10.30)</a>
- <a href="#5">Week 5 (2023.11.8)</a>
- <a href="#6">Week 6 (2024.1.15)</a>
<br/>

<p id="1"></p>  
# 9月12日周报

## 想法：
### 1.近场通信NFC 或许可能可以解决暴露站和隐私站的问题。


![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/a46cc952-9d27-4885-af20-4c617ba9fc03)





![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/2610649d-4a88-41a5-ad77-b13a4cd52b5b)



联邦学习的优势是：
1.保护隐私
2.降低通信负载
3.可随意增加节点，可扩展性强。


![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/7bbe5a70-7393-46dd-a923-e3295faa7164)




### 2.FL for Network
#### 2.1信道接入：
FL除了考虑其保护隐私的作用，还有考虑用户公平性的问题
因为CW过大，过小都会带来一定程度的不公平，故有种思路是通过考虑用户公平性来调整CW，为此，FL和Q神经网络（QNN）模型分别在AP和站中实现，作为分布式方法。当每个站随机初始化其QNN参数时，一些站将使用更积极的策略来接入信道（通过选择小CW）。然而，这样的行为将阻塞以较不积极的策略（具有大CW）初始化的站的传输。为了确保公平性，AP通过FL获得QNN的全局模型，并且稍后向站广播更新的CW值。一个AP和总数量高达50个站点的仿真结果表明，吞吐量相比DCF提高了20%。
#### 2.2链路配置：
物理层方面的话各种功能来提高高数据速率，信道绑定(想法：可不可以结合龙博那个ringsfl 选择最合适的几条信道进行绑定，然后提高速率)
mac层的话，帧聚合和块确认是用于提高最大链路吞吐量的两个主要特征。
帧聚合在有用的传输数据和开销方面直接影响通信效率，较大的帧能降低开销的影响，但是容易受到传输错误的影响，采用帧聚合来解决这种折衷，以导出最佳帧的最大化效率。802.11标准引入了两种基本的聚合方法：聚合MAC服务数据单元（A-MSDU）和聚合MAC协议数据单元（A-MPDU）[2]。这些聚合也可以一起使用[100]。（FL）
在每次链路配置中，给链路配置根据公平性选取合适的MCS值。（FL）
PHY和MAC层交互建模来提高吞吐量
#### 2.3开放性问题：
考虑更现实的设置（包括用户的移动性）
移动性的WiFi设备（手机平板甚至是车辆）如何更近一步的探讨或洞察表征他们的移动性对网络性能的影响。
减少分布式解决方案中代理的协调开销。
密集场景中的相关问题是用户站和AP之间的关联，尤其是为下一代站将具有多归属能力（及允许到多个AP的持续连接方法）这个是否可以解决本身FL的客户端移动问题呢？2
AP负载通常遵循长尾分布，及大部分Ap仅服务于少数用户，少数Ap服务于数百个用户，因此每个AP的利用率是不平衡的，有没有什么办法可以有效利用那些有少量负载Ap的资源，从而提高整体Ap的利用率？
#### 2.4 最近的WiFi特性相关的：
多用户通信（OFDMA，MU-MIMO），频谱聚合和机会性频谱接入（频谱绑定），多链路操作，空间重用和多AP协调
#### 多用户通信：
正交频分多址(OFDMA)把带宽化为不同的子信道（上次听会的时候基于空中计算的联邦学习就用到了OFDMA+FL）
相关的挑战：虽然大多数提出的用于跨网络优化的基于ML的解决方案（例如，由于信道分配）具有集中式操作，我们相信分布式方法更适合Wi-Fi部署的计划外和随机性质。此外，我们不能假设存在管理位于同一地点但单独拥有的Wi-Fi网络（例如，Wi-Fi网络）的集中式控制器。在典型的住宅Wi-Fi部署中）。注意，这样的中央控制器的潜在操作造成了显著的隐私威胁，因为它可能需要收集敏感的用户数据（例如，各个站的业务量）。——FL的场景
我们预计FL对于Wi-Fi网络的优化至关重要，因为它使用单个数据（例如，在站或AP处可用），同时还保护用户隐私。然而，如果FL将通过无线链路实现，则减轻无线通信对FL性能指标的不利影响变得不可避免。
此外，联合学习和迁移学习是最近在Wi-Fi领域引入的。我们预计，在不久的将来，它们将变得更受欢迎，因为它们提供了分配学习任务和提高训练速度的机会。

### 3.Network for FL
FL 里通信WiFi连接是否正常健康是不是可以用WiFi连接的健康预测来判定？
3.1：联邦优化几个考虑的点：
3.1.1通过改善wifi某些措施来最小化通信？
3.1.2通过改善WiFi性能来改善FL的挂钟时间？一轮通信的挂钟时间将受到算法设计选择以及系统属性的影响，包括编码/解码开销、固定网络延迟（例如，通信延迟）、通信延迟和系统性能。建立握手的时间，其独立于发送的比特数），以及每比特通信时间乘以模型大小。
### 4 一个主要问题：
4.1 联邦学习设置的最原始场景是不是就是基于WiFi实现的，也就是说它本身存在的价值就是移动客户端在连接到WiFi并正在充电时才可用这种成为客户端的不活动。
### 5.关于csma/ca的一些小思路
可不可以用transformer来学习信道特征，然后设置一个虚拟的主服务器来收集各个信道特征再根据一些情况进行信道绑定，绑定在一起的信道可以合作完成一个ML模型，然后不同绑定的信道完成的模型不同，加入一些多模态的数据和模型。
### 6.GCN图卷积神经网络相比与GNN的优势：
70%的还是选择使用图卷积在工业上，因为GCN相比GNN有一个独特的优势，但是学术论文创新点上很多还是采用GNN。



![微信图片_20230911091522](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/e2bd5039-367a-4c23-8760-6542d3e38a62)



























































![3eef61f5300371521ad824361dad492](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/c20b15fd-b0ad-498f-bde8-75a83325591e)




















<p id="2"></p>

###  9月28日

1.MYHT 预研申请书撰写

2.帮忙调研radio map的实际运用场景


<p id="3"></p> 

###  10月16日

1.做 AIGC PPT。

2.帮忙调研multi-AP相关工作。

3.查新报告

<p id="4"></p> 

###  10月30日

## 1.Enhancing WiFi Multiple Access Performance with Federated Deep Reinforcement Learning

论文动机：对于越来越多的用户，在单个WiFi小区/基本服务集标识符（BSSID）中增加网络吞吐量仍然是重要的资源分配问题。
为了实现基于DRL的分布式MAC协议的公平性，我们引入了联邦学习（FL）原则。AP实现联合学习（FL）以实现接入公平性和快速收敛。为了简单起见，只考虑上行链路通信，并且每个站总是处于饱和模式（总是有数据要发送到AP）。



![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/df65a522-5ac6-4f36-90d3-e562b70fffd8)





















![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/5505c765-fae2-4639-9b28-cdf5b1878743)












<p id="5"></p> 

###  11月8日

#### 1.读了两篇参考文献，但是帮助不大

#### 2.学了一下那个WiFi具体的书籍

<img width="993" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/62bd664c-53e0-44fc-b902-a841ff836f6f">



<img width="162" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/1b63853d-4390-4e42-8de4-12343fdcbfe5">



#### 信道绑定+ringsfl


![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/172cf733-cda5-459e-a9a1-59b6d595b79e)














![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/4658e1dc-5261-4fb6-b2aa-b9848deffd03)















![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/17373551-5944-4e0d-a025-8c73672ad9c0)
















![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/29358bd5-2f0c-41cb-82a9-cba393e77418)










#### FL 关键期＋WiFi省电模式管理







![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/19b2542a-bcc6-4e24-90c2-3c3490ba3d02)



![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/58f96db9-370c-4e34-8d56-d978971ae9fe)




![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/a508aa86-683f-450d-8331-6bb60fd48398)


#### 帧聚合






![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/8b870708-a5f7-447d-9db2-8a142c31b44d)












![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/3f38522a-bf47-4bf6-872d-86c69c9fdde1)







![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/405eea9a-5a0e-4c0d-8fb9-1f7f230fc620)









![image](https://github.com/UNIC-Lab/Weekly-Report/assets/122032188/dd9b6e2d-e04d-4af3-8817-66c6fcd846da






















# 2024 1.15
### 漫游下移动端的负载协调问题
联邦持续学习辅助下的WiFi多AP负载均衡

### WiFi中的省电模式引入→联邦学习中缓解用户能耗的问题，延长用户的使用时间
WiFi中省电模式（周期性唤醒，借鉴联邦学习的关键期，可以引入甘蔗理论）
