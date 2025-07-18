- [Week 1](#week1)
- [Week 2](#week2)
- [Week 3](#week-3)
- [Week 4](#week-4)
- [Week 5](#week-5)
- [Week 6-7](#week-6-7)
- [Week 8](#week-8)
- [Week 9](#week-9)
- [Week 10](#week-10)
- [Week 11](#week-11)
- [Week 12](#week-12)
- [Week 13-14](#week-13-14)
- [Week 15](#week-15)
- [Week 16](#week-16)

# Week1
- Picmrc: 写代码、调参、画图
# Week2
- Pimrc代码整理
- **Graph 与 transformer相关性的论文调研**
  - 1.https://graphdeeplearning.github.io/post/transformers-are-gnns/
  - 2.Ying C, Cai T, Luo S, et al. Do transformers really perform badly for graph representation?[J]. Advances in Neural Information Processing Systems, 2021, 34: 28877-28888.
![image](https://user-images.githubusercontent.com/90789521/228771067-5e7a526b-33e7-425b-a2be-e73bcf97a833.png)

  - 3.Zhang B, Luo S, Wang L, et al. Rethinking the expressive power of gnns via graph biconnectivity[J]. arXiv preprint arXiv:2301.09505, 2023.
  - 4.Liu Y, Wang W, Hu Y, et al. Multi-agent game abstraction via graph attention neural network[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2020, 34(05): 7211-7218.
- **Severless based computing 相关论文调研**
  - 1.Mohammad S. Aslanpour, Adel N. Toosi, Claudio Cicconetti, Bahman Javadi, Peter Sbarski, Davide Taibi, Marcos Assuncao, Sukhpal Singh Gill, Raj Gaire, and Schahram Dustdar. 2021. Serverless Edge Computing: Vision and Challenges. In Proceedings of the 2021 Australasian Computer Science Week Multiconference (ACSW '21). Association for Computing Machinery, New York, NY, USA, Article 10, 1–10. https://doi.org/10.1145/3437378.3444367
  - 2.Q. Tang et al., "Distributed Task Scheduling in Serverless Edge Computing Networks for the Internet of Things: A Learning Approach," in IEEE Internet of Things Journal, vol. 9, no. 20, pp. 19634-19648, 15 Oct.15, 2022, doi: 10.1109/JIOT.2022.3167417.
  - 3.Y. Li, D. Zeng, L. Gu, K. Wang and S. Guo, "On the Joint Optimization of Function Assignment and Communication Scheduling toward Performance Efficient Serverless Edge Computing," 2022 IEEE/ACM 30th International Symposium on Quality of Service (IWQoS), Oslo, Norway, 2022, pp. 1-9, doi: 10.1109/IWQoS54832.2022.9812887.
  - 4.Yao X, Chen N, Yuan X, et al. Performance optimization of serverless edge computing function offloading based on deep reinforcement learning[J]. Future Generation Computer Systems, 2023, 139: 74-86.
  - 5.Z. Gao, W. Hao, Z. Han and S. Yang, "Q-Learning-Based Task Offloading and Resources Optimization for a Collaborative Computing System," in IEEE Access, vol. 8, pp. 149011-149024, 2020, doi: 10.1109/ACCESS.2020.3015993.
  - 6.Y. Xu, L. Chen, Z. Lu, X. Du, J. Wu and P. C. K. Hung, "An Adaptive Mechanism for Dynamically Collaborative Computing Power and Task Scheduling in Edge Environment," in IEEE Internet of Things Journal, vol. 10, no. 4, pp. 3118-3129, 15 Feb.15, 2023, doi: 10.1109/JIOT.2021.3119181.
  - 7.R. Lin et al., "Energy-Efficient Computation Offloading in Collaborative Edge Computing," in IEEE Internet of Things Journal, vol. 9, no. 21, pp. 21305-21322, 1 Nov.1, 2022, doi: 10.1109/JIOT.2022.3179000.
  - 8.W. Fan et al., "Collaborative Service Placement, Task Scheduling, and Resource Allocation for Task Offloading with Edge-Cloud Cooperation," in IEEE Transactions on Mobile Computing, 2022, doi: 10.1109/TMC.2022.3219261.

- 相关源码阅读
- 审稿
# Week 3
- ServerLess Edge Computing程序仿真
https://github.com/LionelFu/ServerLess_Edge_Computing
- AI Course
- 毕设周报、中期报告
# Week 4
- ServerLess Edge Computing Bug解决与模型训练 https://github.com/LionelFu/ServerLess_Edge_Computing
- 对比试验调研

# Week 5
- Diffusion相关论文阅读：
  - Deep Unsupervised Learning using Nonequilibrium Thermodynamics
  - Denoising Diffusion Probabilistic Models
  - Understanding Diffusion Models: A Unified Perspective
- AI_Course更新
- ServerLess调参
- 服务器维修
# Week 6-7
- 毕业设计完成两个章节
  
# Week 8
- AI Course更新了速通教程，每部分都添加了对应的notebook代码，后续继续更新补全代码资源，增删教程知识点
- 毕业设计，预计所有材料下周周内完成

# Week 9
- 教程修改与学习路线制定
- 竞赛调研
- cuda的多进程学习

# Week 10
- 毕业设计
- ChatGLM-6B测试，demo
- LlaMA测试，demo，fine-tuning策略
- 竞赛代码分析
# Week 11
- 无线大数据竞赛
  - 基于相位差频谱与子载波选择，测试集RMSE约5左右
  - 基于神经网络的滤波算法，调试中
 
# Week 12
- 无线算法竞赛
  - 基于频谱特征RNN，
  - 基于注意力机制角度域特征
 
# Week 13-14
- 无线算法竞赛
  - 基于角度域特征注意力机制模型
  - 初赛与半决赛提交
- ServerLess
  - 构建新的完全图
# Week 15
- 无线算法竞赛
  - 基于神经网络随机森林模型：过拟合问题很难解决，主要是数据问题，数据质量不高且数据量太少，模型只能收敛到标签的分布
  - 基于规则的子载波选择，基于SVM的子载波选择
# Week 16
- 无线算法竞赛
  - 基于加权投票的子载波选择
  - 误差信号处理
  - 测试集结果：
    |测试集|RMSE|
    |:----------|---------:|
    |T1|	4.17|
    |T2|	1.356|
    |T3|	2.65|
    |T4|	7.921|
    |T5|	4.382|
    |T6|	1.803|
    |T7|	2.9824|
- 基于图同构的GNN表征能力论文阅读
  - EQUIVARIANT SUBGRAPH AGGREGATION NETWORKS
  - Improving Graph Neural Network Expressivity via Subgraph Isomorphism Counting
  - RETHINKING THE EXPRESSIVE POWER OF GNNS VIA GRAPH BICONNECTIVITY
- 基于GNN的MILP问题求解论文阅读
  - ON REPRESENTING MIXED-INTEGER LINEAR PROGRAMS BY GRAPH NEURAL NETWORKS
  <img width="1010" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/90789521/253d4244-05a5-4dbf-b0ab-963b7ebceb4e">

