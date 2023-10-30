### 2023.10.29
# 本周进展
1. 学习龙博和老师发的两篇文献中的方法

   1）UAV-enabled federated learning in Dynamic Environments：Efficiency and Security Trade-off

   2）Shrinking the Insecure Area  for Satellite Downlink using Multi-Beam Intersection
  
3. 和老师讨论了FL和PLS结合的具体解决方法，梳理出来了实现流程，正在修改代码
# 下周安排
1. 组会需要分享的文献阅读

2. 继续修改代码

### 2023.10.15
# 本周进展
1. 梳理了目前FL和PLS结合所遇到的主要问题

2. 阅读目前一些FL和PLS结合相关的文献：

1）J. Ahmed, T. N. Nguyen, B. Ali, M. A. Javed and J. Mirza, "On the Physical Layer Security of Federated Learning Based IoMT Networks," in IEEE Journal of Biomedical and Health Informatics

2）H. Zhang, C. Yang and B. Dai, "When Wireless Federated Learning Meets Physical Layer Security: The Fundamental Limits," IEEE INFOCOM 2022 - IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS)

![image](./github/1.png)

第一篇文献主要是其框架，将IoMT视作Client，将IoMT节点划分为各个集群，每个集群先在各自的中心进行聚合，然后各个集群中心共享参数更新

![image](./github/2.jpg)

第二篇文献是通过编码的方式在FL中实现物理层安全

问题在于PLS和FL的结合不够紧密，最后其考量的还是物理层安全的保密率和误码率的指标，联邦学习的性能没有讨论，还是割裂的两个问题。
# 下周安排
1. 和老师讨论FL和PLS结合的可行方法，然后进行实践

2. 继续阅读PLS和FL结合的相关论文

### 2023.9.5
# 本周进展
1.简化了联邦学习的模型，设计为20client，1server，信道建模为随距离变化的简单信道

2.在简化后的模型上对通信过程进行加噪，等效信道传输过程噪声对模型参数带来的影响
# 下周安排
阅读差分隐私和联邦学习结合的文章，寻求物理层安全方案和联邦学习模型训练效果之间的关系
