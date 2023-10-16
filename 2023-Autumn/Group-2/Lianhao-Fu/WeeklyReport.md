# Week 6
- 1.WiFi感知：按照(天线数，子载波数，时间索引)格式分割数据，基于CNN进行分类，训练集准确率约88.16%，测试集准确率约80.74%。![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90789521/9000a901-50a7-4575-aac4-4533b6637a85)，![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90789521/a09dd238-141d-486c-9fcc-660121c23cb9)
    - 仅2576条数据，数据量过少，存在过拟合；
    - 实际场景中高频噪声较多，但没有好的预处理办法可以去除噪声的同时不丢失信息；
    - 知识蒸馏可以一定程度上增加泛化性
    - 尝试few-shot learning
- 2.消化TDMA的通信机制，serverless代码移植




# Week 2
- 1.组会汇报准备：Learning Cooperative Policies with Graph Networks in Distributed Swarm Systems
- 2.Google Scholar爬虫，代码基本完成，但存在block问题
- 3.可生灭无人机的轨迹规划问题，采用curriculum learning训练（但存在部分idea重叠）


# Week 1
## 1. MEC系统中的CTDE多智能体决策系统如何完全scalable
- **观测角度**：环境中非agent本身的因素数量可变（如移动边缘计算中ES的上线、离线、移动等） --> 通过异构图方式观测编码环境（ICML23一篇文章也借鉴这种思想且作为其中较大的一个贡献）
- **Agent角度**：实现完全scalable必须通过参数共享。小规模情况参数共享反而提高网络收敛速度，但是agents数量变大共享参数后性能会变差
- **state角度**：以图的方式编码整个场景作为state，以ESAN的思想构建多个子图（每个子图的注意力权重不一样，有效且效果良好，但与其本质就是multihead-attention。或者使用gumble-softmax剪切一些边，但效果并不理想）
- state编码需要保持置换不变性
- 对于每个agent需要保持置换同变性 --> GNN本身具有置换同变性

## 2. 模型绘图
![23-9-5-模型绘图](https://github.com/UNIC-Lab/Weekly-Report/assets/90789521/bc7a2107-0a8e-466c-9772-aa65782dcbe5)

## 3.验证性实验
- 每个agent只有一个task且必须卸载到ES，只考虑卸载对象的选择，同一个ES接收到的信号之间才会相互干扰。基于QMIX进行训练。
- 表征能力良好，训练集中收敛结果基本接近理论最优
- 泛化性有调整空间。测试集相对于基于Greedy的方案优势约1到2个数量级
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90789521/d4dd5703-ad3f-4a1b-a86d-4d9b2096f434)

## 4. 场景确定
- Action: 选择卸载或者不卸载,选择卸载对象
- OFDM
- Possion流生成任务
- Reward：本地计算损失，传输损失，排队损失，边缘计算损失，是否丢包

## 5. Reference:
```
[1]Bevilacqua, Beatrice, Fabrizio Frasca, Derek Lim, Balasubramaniam Srinivasan, Chen Cai, Gopinath Balamurugan, Michael M. Bronstein和Haggai Maron. 《Equivariant Subgraph Aggregation Networks》. arXiv, 2022年3月16日. https://doi.org/10.48550/arXiv.2110.02910.

[2]Bouritsas, Giorgos, Fabrizio Frasca, Stefanos Zafeiriou和Michael M. Bronstein. 《Improving Graph Neural Network Expressivity via Subgraph Isomorphism Counting》. IEEE Transactions on Pattern Analysis and Machine Intelligence 45, 期 1 (2023年1月): 657–68. https://doi.org/10.1109/TPAMI.2022.3154319.

[3]Gao, Zhen, Lei Yang和Yu Dai. 《Large-Scale Computation Offloading Using a Multi-Agent Reinforcement Learning in Heterogeneous Multi-Access Edge Computing》. IEEE Transactions on Mobile Computing 22, 期 6 (2023年6月): 3425–43. https://doi.org/10.1109/TMC.2022.3141080.

[4]Ha, David, Andrew Dai和Quoc V. Le. 《HyperNetworks》. arXiv, 2016年12月1日. http://arxiv.org/abs/1609.09106.

[5]Kortvelesy, Ryan, 和Amanda Prorok. 《QGNN: Value Function Factorisation with Graph Neural Networks》. arXiv, 2023年6月20日. http://arxiv.org/abs/2205.13005.

[6]Papoudakis, Georgios, Filippos Christianos, Lukas Schäfer和Stefano V. Albrecht. 《Benchmarking Multi-Agent Deep Reinforcement Learning Algorithms in Cooperative Tasks》. arXiv, 2021年11月9日. https://doi.org/10.48550/arXiv.2006.07869.

[7]Phan, Thomy, Fabian Ritz, Philipp Altmann, Maximilian Zorn, Jonas Nüßlein, Michael Kölle, Thomas Gabor和Claudia Linnhoff-Popien. 《Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability》, 不详.

[8]Zaheer, Manzil, Satwik Kottur, Siamak Ravanbakhsh, Barnabas Poczos, Ruslan Salakhutdinov和Alexander Smola. 《Deep Sets》. arXiv, 2018年4月14日. https://doi.org/10.48550/arXiv.1703.06114.

[9]Nayak, Siddharth, Kenneth Choi, Wenqi Ding, Sydney Dolan, Karthik Gopalakrishnan和Hamsa Balakrishnan. 《Scalable Multi-Agent Reinforcement Learning through Intelligent Information Aggregation》. 收入 Proceedings of the 40th International Conference on Machine Learning, 25817–33. PMLR, 2023. https://proceedings.mlr.press/v202/nayak23a.html.
```

